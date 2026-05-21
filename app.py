import os
from flask import Flask, render_template, redirect, url_for, request, Response
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

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "easyrecipe-dev-2026")

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
    )


# ── Page routes ───────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


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
    return render_template(
        "recipe_detail.html",
        cat=cat, cat_id=cat_id, sub=sub, sub_id=sub_id,
        recipe=recipe,
        recipe_path=recipe_path,
    )


@app.route("/tools")
def tools():
    return render_template("tools.html", tool_categories=TOOL_CATEGORIES, tools_ui=TOOLS_UI)


@app.route("/search")
def search():
    lang = get_lang()
    all_recipes = []
    for key, recipe_list in RECIPES.items():
        cat_id, sub_id = key.split("/")
        cat = CATEGORIES.get(cat_id)
        if not cat:
            continue
        sub = next((s for s in cat["sub"] if s["id"] == sub_id), None)
        for recipe in recipe_list:
            all_recipes.append({
                "cat_id": cat_id, "sub_id": sub_id,
                "recipe_id": recipe["id"],
                "name": recipe["name"],
                "desc": recipe.get("desc", {}),
                "time": recipe["time"],
                "difficulty": recipe["difficulty"],
                "cat_name": cat["name"],
                "cat_color": cat["color"],
                "sub_name": sub["name"] if sub else {"ko": "", "en": "", "ja": "", "zh": ""},
                "ingredients": [i["name"] for i in recipe.get("ingredients", [])],
            })
    return render_template(
        "search.html",
        all_recipes=all_recipes,
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
    weeks = []
    for week in COURSE:
        enriched_recipes = []
        for ref in week["recipes"]:
            key = f"{ref['cat']}/{ref['sub']}"
            recipe_list = RECIPES.get(key, [])
            recipe = next((r for r in recipe_list if r["id"] == ref["id"]), None)
            cat = CATEGORIES.get(ref["cat"])
            sub = next((s for s in cat["sub"] if s["id"] == ref["sub"]), None) if cat else None
            enriched_recipes.append({
                "recipe": recipe,
                "cat_id": ref["cat"],
                "sub_id": ref["sub"],
                "cat": cat,
                "sub": sub,
            })
        weeks.append({**week, "enriched_recipes": enriched_recipes})
    return render_template("course.html", weeks=weeks, course_ui=COURSE_UI)


@app.route("/favorites")
def favorites():
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
    return render_template("favorites.html", all_recipes=all_recipes)


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


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/profile")
def profile():
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
    return render_template("profile.html", all_recipes=all_recipes)


@app.route("/robots.txt")
def robots():
    return Response("User-agent: *\nAllow: /\n", mimetype="text/plain")


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
