import os
from datetime import datetime, timezone


def _now():
    return datetime.now(timezone.utc)
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_login import LoginManager, current_user, login_required
from models import db, User, Favorite, CookingLog, RecipeNote, CourseProgress
from recipe_data import CATEGORIES, UI_TEXT
from recipes_kr import RECIPES_KR
from recipes_cn import RECIPES_CN
from recipes_west import RECIPES_WEST
from recipes_jp import RECIPES_JP
from recipes_extra import RECIPES_EXTRA
from recipes_extra2 import RECIPES_EXTRA2
from recipes_extra3 import RECIPES_EXTRA3
from tools_data import TOOL_CATEGORIES, TOOLS_UI
from substitutes_data import SUBSTITUTES, SUBS_UI
from course_data import COURSE, COURSE_UI
from seasonal_data import SEASONAL, SEASONAL_UI
from ingredient_i18n import translate_ing_name, translate_amount
from auth import auth_bp

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "easyrecipe-dev-2026")

_db_url = os.environ.get("DATABASE_URL", "sqlite:///easyrecipe.db")
if _db_url.startswith("postgres://"):
    _db_url = _db_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = _db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

app.register_blueprint(auth_bp)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


def _merge(base, extra):
    result = {k: list(v) for k, v in base.items()}
    for k, v in extra.items():
        result.setdefault(k, []).extend(v)
    return result


RECIPES = _merge(
    _merge(
        _merge({**RECIPES_KR, **RECIPES_CN, **RECIPES_WEST, **RECIPES_JP}, RECIPES_EXTRA),
        RECIPES_EXTRA2
    ),
    RECIPES_EXTRA3
)
LANGS = ["ko", "en", "ja", "zh"]

DIFFICULTY = {
    1: {"ko": "쉬움", "en": "Easy", "ja": "かんたん", "zh": "简单"},
    2: {"ko": "보통", "en": "Medium", "ja": "ふつう", "zh": "中等"},
    3: {"ko": "어려움", "en": "Hard", "ja": "むずかしい", "zh": "较难"},
}

SEARCH_PLACEHOLDER = {
    "ko": "재료나 요리 이름으로 검색",
    "en": "Search by ingredient or recipe name",
    "ja": "食材や料理名で検索",
    "zh": "按食材或菜名搜索",
}

SEARCH_BTN = {
    "ko": "검색",
    "en": "Search",
    "ja": "検索",
    "zh": "搜索",
}


def get_lang():
    lang = request.args.get("lang", "ko")
    return lang if lang in LANGS else "ko"


@app.template_global()
def trans_ing(name, lang):
    return translate_ing_name(name, lang)


@app.template_global()
def trans_amt(amount, lang):
    return translate_amount(amount, lang)



@app.context_processor
def inject_globals():
    lang = get_lang()
    return dict(
        categories=CATEGORIES,
        ui=UI_TEXT,
        langs=LANGS,
        lang=lang,
        difficulty=DIFFICULTY,
        current_user=current_user,
    )


with app.app_context():
    db.create_all()


# ── Page routes ───────────────────────────────────────────────

@app.route("/")
def index():
    lang = get_lang()
    return render_template(
        "index.html",
        search_placeholder=SEARCH_PLACEHOLDER[lang],
        search_btn=SEARCH_BTN[lang],
    )


@app.route("/category/<cat_id>")
def category(cat_id):
    cat = CATEGORIES.get(cat_id)
    if not cat:
        return redirect(url_for("index"))
    return render_template("category.html", cat=cat, cat_id=cat_id)


@app.route("/category/<cat_id>/<sub_id>")
def recipes(cat_id, sub_id):
    cat = CATEGORIES.get(cat_id)
    if not cat:
        return redirect(url_for("index"))
    sub = next((s for s in cat["sub"] if s["id"] == sub_id), None)
    if not sub:
        return redirect(url_for("category", cat_id=cat_id))
    recipe_list = RECIPES.get(f"{cat_id}/{sub_id}", [])
    return render_template("recipes.html", cat=cat, cat_id=cat_id, sub=sub,
                           recipe_list=recipe_list)


@app.route("/category/<cat_id>/<sub_id>/<recipe_id>")
def recipe_detail(cat_id, sub_id, recipe_id):
    cat = CATEGORIES.get(cat_id)
    if not cat:
        return redirect(url_for("index"))
    sub = next((s for s in cat["sub"] if s["id"] == sub_id), None)
    recipe_list = RECIPES.get(f"{cat_id}/{sub_id}", [])
    recipe = next((r for r in recipe_list if r["id"] == recipe_id), None)
    if not recipe:
        return redirect(url_for("recipes", cat_id=cat_id, sub_id=sub_id))

    recipe_path = f"{cat_id}/{sub_id}/{recipe_id}"
    is_fav = False
    cook_log = None
    note_content = ""

    if current_user.is_authenticated:
        is_fav = Favorite.query.filter_by(
            user_id=current_user.id, recipe_path=recipe_path).first() is not None
        cook_log = CookingLog.query.filter_by(
            user_id=current_user.id, recipe_path=recipe_path).first()
        note_row = RecipeNote.query.filter_by(
            user_id=current_user.id, recipe_path=recipe_path).first()
        note_content = note_row.content if note_row else ""

    return render_template(
        "recipe_detail.html",
        cat=cat, cat_id=cat_id, sub=sub, sub_id=sub_id,
        recipe=recipe,
        recipe_path=recipe_path,
        is_fav=is_fav,
        cook_log=cook_log,
        note_content=note_content,
    )


@app.route("/tools")
def tools():
    return render_template("tools.html", tool_categories=TOOL_CATEGORIES, tools_ui=TOOLS_UI)


@app.route("/search")
def search():
    lang = get_lang()
    q = request.args.get("q", "").strip().lower()
    results = []
    if q:
        for key, recipe_list in RECIPES.items():
            cat_id, sub_id = key.split("/")
            cat = CATEGORIES.get(cat_id)
            if not cat:
                continue
            sub = next((s for s in cat["sub"] if s["id"] == sub_id), None)
            for recipe in recipe_list:
                name_match = any(q in recipe["name"].get(l, "").lower() for l in LANGS)
                ing_match = any(q in ing["name"].lower() for ing in recipe.get("ingredients", []))
                if name_match or ing_match:
                    results.append({
                        "recipe": recipe,
                        "cat_id": cat_id,
                        "sub_id": sub_id,
                        "cat": cat,
                        "sub": sub,
                    })
    return render_template(
        "search.html",
        results=results, q=q,
        search_placeholder=SEARCH_PLACEHOLDER[lang],
        search_btn=SEARCH_BTN[lang],
    )


@app.route("/substitutes")
def substitutes():
    groups_order = ["dairy", "flour", "sauce", "egg", "other"]
    return render_template("substitutes.html", substitutes=SUBSTITUTES,
                           subs_ui=SUBS_UI, groups_order=groups_order)


@app.route("/course")
def course():
    lang = get_lang()
    completed_paths = set()
    if current_user.is_authenticated:
        rows = CourseProgress.query.filter_by(user_id=current_user.id).all()
        completed_paths = {r.recipe_path for r in rows}

    weeks = []
    for week in COURSE:
        enriched_recipes = []
        for ref in week["recipes"]:
            key = f"{ref['cat']}/{ref['sub']}"
            recipe_list = RECIPES.get(key, [])
            recipe = next((r for r in recipe_list if r["id"] == ref["id"]), None)
            cat = CATEGORIES.get(ref["cat"])
            sub = next((s for s in cat["sub"] if s["id"] == ref["sub"]), None) if cat else None
            rpath = f"{ref['cat']}/{ref['sub']}/{ref['id']}"
            enriched_recipes.append({
                "recipe": recipe,
                "cat_id": ref["cat"],
                "sub_id": ref["sub"],
                "cat": cat,
                "sub": sub,
                "recipe_path": rpath,
                "completed": rpath in completed_paths,
            })
        weeks.append({**week, "enriched_recipes": enriched_recipes})

    return render_template("course.html", weeks=weeks, course_ui=COURSE_UI)


@app.route("/favorites")
def favorites():
    lang = get_lang()
    if current_user.is_authenticated:
        fav_rows = Favorite.query.filter_by(
            user_id=current_user.id).order_by(Favorite.created_at.desc()).all()
        fav_recipes = []
        for fav in fav_rows:
            parts = fav.recipe_path.split("/")
            if len(parts) != 3:
                continue
            cat_id, sub_id, recipe_id = parts
            cat = CATEGORIES.get(cat_id)
            sub = next((s for s in cat["sub"] if s["id"] == sub_id), None) if cat else None
            recipe_list = RECIPES.get(f"{cat_id}/{sub_id}", [])
            recipe = next((r for r in recipe_list if r["id"] == recipe_id), None)
            if recipe:
                fav_recipes.append({
                    "recipe": recipe, "cat_id": cat_id,
                    "sub_id": sub_id, "cat": cat, "sub": sub,
                })
        return render_template("favorites.html", fav_recipes=fav_recipes,
                               server_mode=True, all_recipes=None)

    # Guest: pass all recipes for localStorage matching
    all_recipes = []
    for key, recipe_list in RECIPES.items():
        cat_id, sub_id = key.split("/")
        cat = CATEGORIES.get(cat_id)
        if not cat:
            continue
        sub = next((s for s in cat["sub"] if s["id"] == sub_id), None)
        for recipe in recipe_list:
            all_recipes.append({
                "path": f"{cat_id}/{sub_id}/{recipe['id']}",
                "cat_id": cat_id, "sub_id": sub_id,
                "recipe_id": recipe["id"],
                "name": recipe["name"],
                "desc": recipe.get("desc", {}),
                "time": recipe["time"],
                "difficulty": recipe["difficulty"],
                "cat_name": cat["name"],
                "cat_color": cat["color"],
                "sub_name": sub["name"] if sub else {"ko": "", "en": "", "ja": "", "zh": ""},
            })
    return render_template("favorites.html", fav_recipes=None,
                           server_mode=False, all_recipes=all_recipes)


@app.route("/seasonal")
def seasonal():
    seasons_order = ["spring", "summer", "fall", "winter"]
    enriched_seasons = {}
    for key, season in SEASONAL.items():
        enriched_recipes = []
        for ref in season["recipes"]:
            path_key = f"{ref['cat']}/{ref['sub']}"
            recipe_list = RECIPES.get(path_key, [])
            recipe = next((r for r in recipe_list if r["id"] == ref["id"]), None)
            cat = CATEGORIES.get(ref["cat"])
            sub = next((s for s in cat["sub"] if s["id"] == ref["sub"]), None) if cat else None
            if recipe:
                enriched_recipes.append({
                    "recipe": recipe, "cat_id": ref["cat"],
                    "sub_id": ref["sub"], "cat": cat, "sub": sub,
                })
        enriched_seasons[key] = {**season, "enriched_recipes": enriched_recipes}
    return render_template("seasonal.html", seasonal=enriched_seasons,
                           seasons_order=seasons_order, seasonal_ui=SEASONAL_UI)


@app.route("/profile")
@login_required
def profile():
    lang = get_lang()
    fav_rows = Favorite.query.filter_by(
        user_id=current_user.id).order_by(Favorite.created_at.desc()).all()
    log_rows = CookingLog.query.filter_by(
        user_id=current_user.id).order_by(CookingLog.last_cooked.desc()).all()

    def enrich(recipe_path):
        parts = recipe_path.split("/")
        if len(parts) != 3:
            return None
        cat_id, sub_id, recipe_id = parts
        cat = CATEGORIES.get(cat_id)
        sub = next((s for s in cat["sub"] if s["id"] == sub_id), None) if cat else None
        recipe_list = RECIPES.get(f"{cat_id}/{sub_id}", [])
        recipe = next((r for r in recipe_list if r["id"] == recipe_id), None)
        if not recipe:
            return None
        return {"recipe": recipe, "cat_id": cat_id, "sub_id": sub_id, "cat": cat, "sub": sub}

    fav_recipes = [e for e in (enrich(r.recipe_path) for r in fav_rows) if e]
    cooked_items = []
    for row in log_rows:
        e = enrich(row.recipe_path)
        if e:
            cooked_items.append({**e, "count": row.count, "last_cooked": row.last_cooked})

    return render_template("profile.html", fav_recipes=fav_recipes,
                           cooked_items=cooked_items)


# ── API routes ────────────────────────────────────────────────

@app.route("/api/favorite", methods=["POST"])
@login_required
def api_favorite():
    data = request.get_json(silent=True) or {}
    path = data.get("path", "")
    if not path:
        return jsonify({"error": "missing path"}), 400
    fav = Favorite.query.filter_by(user_id=current_user.id, recipe_path=path).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"favorited": False})
    db.session.add(Favorite(user_id=current_user.id, recipe_path=path))
    db.session.commit()
    return jsonify({"favorited": True})


@app.route("/api/cook", methods=["POST"])
@login_required
def api_cook():
    data = request.get_json(silent=True) or {}
    path = data.get("path", "")
    if not path:
        return jsonify({"error": "missing path"}), 400
    log = CookingLog.query.filter_by(user_id=current_user.id, recipe_path=path).first()
    if log:
        log.count += 1
        log.last_cooked = _now()
    else:
        log = CookingLog(user_id=current_user.id, recipe_path=path)
        db.session.add(log)
    db.session.commit()
    return jsonify({"count": log.count, "last_cooked": log.last_cooked.strftime("%Y.%m.%d")})


@app.route("/api/note", methods=["POST"])
@login_required
def api_note():
    data = request.get_json(silent=True) or {}
    path = data.get("path", "")
    content = data.get("content", "")
    if not path:
        return jsonify({"error": "missing path"}), 400
    note = RecipeNote.query.filter_by(user_id=current_user.id, recipe_path=path).first()
    if note:
        note.content = content
        note.updated_at = _now()
    else:
        note = RecipeNote(user_id=current_user.id, recipe_path=path, content=content)
        db.session.add(note)
    db.session.commit()
    return jsonify({"saved": True})


@app.route("/api/course-progress", methods=["POST"])
@login_required
def api_course_progress():
    data = request.get_json(silent=True) or {}
    path = data.get("path", "")
    completed = data.get("completed", True)
    if not path:
        return jsonify({"error": "missing path"}), 400
    row = CourseProgress.query.filter_by(user_id=current_user.id, recipe_path=path).first()
    if completed and not row:
        db.session.add(CourseProgress(user_id=current_user.id, recipe_path=path))
        db.session.commit()
    elif not completed and row:
        db.session.delete(row)
        db.session.commit()
    return jsonify({"completed": completed})


@app.route("/random")
def random_recipe():
    import random
    lang = get_lang()
    all_items = []
    for key, recipe_list in RECIPES.items():
        cat_id, sub_id = key.split("/")
        for recipe in recipe_list:
            all_items.append((cat_id, sub_id, recipe["id"]))
    if not all_items:
        return redirect(url_for("index", lang=lang))
    cat_id, sub_id, recipe_id = random.choice(all_items)
    return redirect(url_for("recipe_detail", cat_id=cat_id, sub_id=sub_id,
                            recipe_id=recipe_id, lang=lang))


@app.route("/robots.txt")
def robots():
    from flask import Response
    return Response("User-agent: *\nAllow: /\nDisallow: /api/\n", mimetype="text/plain")


@app.errorhandler(404)
def page_not_found(e):
    lang = get_lang()
    return render_template("404.html", lang=lang), 404


@app.errorhandler(500)
def server_error(e):
    lang = get_lang()
    return render_template("500.html", lang=lang), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, host="0.0.0.0", port=port)
