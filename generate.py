import os
import re
import shutil
import json

os.environ['DATABASE_URL'] = 'sqlite:///build.db'
os.environ['SECRET_KEY'] = 'build-static-key'

from app import app
from recipe_data import CATEGORIES
from recipes_kr import RECIPES_KR
from recipes_jp import RECIPES_JP
from recipes_cn import RECIPES_CN
from recipes_west import RECIPES_WEST
from recipes_extra import RECIPES_EXTRA
from recipes_extra2 import RECIPES_EXTRA2
from recipes_extra3 import RECIPES_EXTRA3

def _merge(base, extra):
    result = {k: list(v) for k, v in base.items()}
    for k, v in extra.items():
        result.setdefault(k, []).extend(v)
    return result

RECIPES = _merge(_merge(_merge(
    {**RECIPES_KR, **RECIPES_CN, **RECIPES_WEST, **RECIPES_JP},
    RECIPES_EXTRA), RECIPES_EXTRA2), RECIPES_EXTRA3)

LANGS = ['ko', 'en', 'ja', 'zh']
BUILD = 'build'


def fix_urls(html_bytes):
    """Replace ?lang=xx query params with /xx/ prefix in href attributes."""
    html = html_bytes.decode('utf-8', errors='replace')

    def repl(m):
        url = m.group(1)
        if url.startswith('/') and 'lang=' in url:
            lm = re.search(r'lang=([a-z]{2})', url)
            if lm:
                lang = lm.group(1)
                path = url.split('?')[0].rstrip('/')
                new = f'/{lang}{path}/' if path else f'/{lang}/'
                return f'href="{new}"'
        return m.group(0)

    html = re.sub(r'href="([^"]*)"', repl, html)
    return html.encode('utf-8')


def save(path, data):
    fp = os.path.join(BUILD, path.lstrip('/'), 'index.html')
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, 'wb') as f:
        f.write(fix_urls(data))
    print(f'  {fp}')


# ── Prepare build directory ───────────────────────────────────
shutil.rmtree(BUILD, ignore_errors=True)
os.makedirs(BUILD)

shutil.copytree('static', os.path.join(BUILD, 'static'))
print('Copied static/')

# Language-detection redirect at root
with open(os.path.join(BUILD, 'index.html'), 'w', encoding='utf-8') as f:
    f.write("""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<script>
var l=(navigator.language||navigator.userLanguage||'ko').toLowerCase();
var t='/ko/';
if(l.startsWith('ja'))t='/ja/';
else if(l.startsWith('zh'))t='/zh/';
else if(l.startsWith('en'))t='/en/';
window.location.replace(t);
</script>
</head><body></body></html>""")

# ── Generate search data JSON for client-side search ─────────
search_data = []
for key, recipe_list in RECIPES.items():
    cat_id, sub_id = key.split('/')
    for recipe in recipe_list:
        search_data.append({
            'id': recipe['id'],
            'cat_id': cat_id,
            'sub_id': sub_id,
            'name': recipe['name'],
            'ingredients': [i['name'] for i in recipe.get('ingredients', [])],
        })

with open(os.path.join(BUILD, 'search_data.json'), 'w', encoding='utf-8') as f:
    json.dump(search_data, f, ensure_ascii=False)
print('Generated search_data.json')

# ── Generate all pages ────────────────────────────────────────
with app.test_client() as c:
    for lang in LANGS:
        print(f'\n[{lang}]')

        # Index
        save(f'/{lang}', c.get(f'/?lang={lang}').data)

        # Category / sub-category / recipe pages
        for cat_id, cat in CATEGORIES.items():
            save(f'/{lang}/category/{cat_id}',
                 c.get(f'/category/{cat_id}?lang={lang}').data)
            for sub in cat['sub']:
                sub_id = sub['id']
                save(f'/{lang}/category/{cat_id}/{sub_id}',
                     c.get(f'/category/{cat_id}/{sub_id}?lang={lang}').data)
                for recipe in RECIPES.get(f'{cat_id}/{sub_id}', []):
                    save(f'/{lang}/category/{cat_id}/{sub_id}/{recipe["id"]}',
                         c.get(f'/category/{cat_id}/{sub_id}/{recipe["id"]}?lang={lang}').data)

        # Static-ish pages
        for page in ['tools', 'substitutes', 'course', 'seasonal', 'favorites']:
            save(f'/{lang}/{page}',
                 c.get(f'/{page}?lang={lang}').data)

        # Search page (empty — client-side search via search_data.json)
        save(f'/{lang}/search',
             c.get(f'/search?lang={lang}').data)

print('\nBuild complete!')
