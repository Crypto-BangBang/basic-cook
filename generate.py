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

        # Auth pages
        for page in ['login', 'register', 'profile', 'forgot-password', 'reset-password']:
            save(f'/{lang}/{page}', c.get(f'/{page}?lang={lang}').data)

        # Search page (empty — client-side search via search_data.json)
        save(f'/{lang}/search',
             c.get(f'/search?lang={lang}').data)

# ── Generate sitemap.xml ──────────────────────────────────────
SITE_URL = 'https://basic-cook.netlify.app'
urls = []
for lang in LANGS:
    urls.append(f'{SITE_URL}/{lang}/')
    for page in ['tools', 'substitutes', 'course', 'seasonal', 'favorites', 'search']:
        urls.append(f'{SITE_URL}/{lang}/{page}/')
    for cat_id, cat in CATEGORIES.items():
        urls.append(f'{SITE_URL}/{lang}/category/{cat_id}/')
        for sub in cat['sub']:
            sub_id = sub['id']
            urls.append(f'{SITE_URL}/{lang}/category/{cat_id}/{sub_id}/')
            for recipe in RECIPES.get(f'{cat_id}/{sub_id}', []):
                urls.append(f'{SITE_URL}/{lang}/category/{cat_id}/{sub_id}/{recipe["id"]}/')

with open(os.path.join(BUILD, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write(f'  <url><loc>{url}</loc></url>\n')
    f.write('</urlset>')
print('Generated sitemap.xml')

# ── Generate standalone 404.html for Netlify ─────────────────
with open(os.path.join(BUILD, '404.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>404 — Basic Cook</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>\U0001f373</text></svg>">
  <style>
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:#0f0d0a;color:#e8e0d0;font-family:-apple-system,sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;padding:24px}
    .card{text-align:center;max-width:400px}
    .code{font-size:6rem;font-weight:800;color:#c9a84c;line-height:1}
    .title{font-size:1.4rem;margin:20px 0 10px}
    .msg{color:#a09080;margin-bottom:32px;line-height:1.6}
    .btn{display:inline-block;padding:12px 32px;background:#c9a84c;color:#1a1612;border-radius:50px;text-decoration:none;font-weight:700;transition:background .2s}
    .btn:hover{background:#d4b86a}
  </style>
</head>
<body>
  <div class="card">
    <p class="code">404</p>
    <h1 class="title" id="t">페이지를 찾을 수 없어요</h1>
    <p class="msg" id="m">주소가 잘못됐거나 삭제된 페이지예요.</p>
    <a href="/ko/" class="btn" id="b">홈으로 돌아가기</a>
  </div>
  <script>
    var p=window.location.pathname,lang='ko';
    if(p.startsWith('/en/'))lang='en';
    else if(p.startsWith('/ja/'))lang='ja';
    else if(p.startsWith('/zh/'))lang='zh';
    var msgs={ko:{t:'페이지를 찾을 수 없어요',m:'주소가 잘못됐거나 삭제된 페이지예요.',b:'홈으로 돌아가기'},
              en:{t:'Page Not Found',m:"The page you're looking for doesn't exist.",b:'Back to Home'},
              ja:{t:'ページが見つかりません',m:'URLが間違っているか、削除されたページです。',b:'ホームに戻る'},
              zh:{t:'页面未找到',m:'您访问的页面不存在或已被删除。',b:'返回首页'}};
    var d=msgs[lang];
    document.getElementById('t').textContent=d.t;
    document.getElementById('m').textContent=d.m;
    var btn=document.getElementById('b');
    btn.textContent=d.b;btn.href='/'+lang+'/';
  </script>
</body>
</html>''')
print('Generated 404.html')

print('\nBuild complete!')
