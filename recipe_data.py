CATEGORIES = {
    "korean": {
        "name": {"ko": "한식", "en": "Korean", "ja": "韓国料理", "zh": "韩餐"},
        "color": "#c0392b",
        "sub": [
            {"id": "rice",   "name": {"ko": "밥·죽",     "en": "Rice & Porridge", "ja": "ご飯・お粥",   "zh": "米饭·粥"}},
            {"id": "soup",   "name": {"ko": "국·찌개",   "en": "Soups & Stews",   "ja": "スープ・チゲ", "zh": "汤·火锅"}},
            {"id": "grill",  "name": {"ko": "구이·볶음", "en": "Grill & Stir-fry", "ja": "焼き物・炒め",  "zh": "烤·炒"}},
            {"id": "kimchi", "name": {"ko": "김치·반찬", "en": "Kimchi & Sides",   "ja": "キムチ・おかず","zh": "泡菜·小菜"}},
            {"id": "noodle", "name": {"ko": "면·만두",   "en": "Noodles & Dumplings","ja": "麺・餃子",  "zh": "面条·饺子"}},
        ],
    },
    "chinese": {
        "name": {"ko": "중식", "en": "Chinese", "ja": "中華料理", "zh": "中餐"},
        "color": "#e67e22",
        "sub": [
            {"id": "noodle",  "name": {"ko": "면·만두",   "en": "Noodles & Dumplings","ja": "麺・餃子",   "zh": "面条·饺子"}},
            {"id": "rice",    "name": {"ko": "밥·볶음밥", "en": "Rice & Fried Rice",   "ja": "ご飯・炒飯", "zh": "米饭·炒饭"}},
            {"id": "stirfry", "name": {"ko": "볶음·튀김", "en": "Stir-fry & Deep-fry", "ja": "炒め物・揚げ物","zh": "炒菜·炸菜"}},
            {"id": "soup",    "name": {"ko": "탕·수프",   "en": "Soups & Hot Pot",     "ja": "スープ・鍋",  "zh": "汤·火锅"}},
            {"id": "dim",     "name": {"ko": "딤섬·간식", "en": "Dim Sum & Snacks",     "ja": "点心・おやつ","zh": "点心·小吃"}},
        ],
    },
    "western": {
        "name": {"ko": "양식", "en": "Western", "ja": "洋食", "zh": "西餐"},
        "color": "#2980b9",
        "sub": [
            {"id": "pasta",  "name": {"ko": "파스타",    "en": "Pasta",          "ja": "パスタ",       "zh": "意面"}},
            {"id": "meat",   "name": {"ko": "스테이크·육류","en": "Steak & Meat", "ja": "ステーキ・肉",  "zh": "牛排·肉类"}},
            {"id": "salad",  "name": {"ko": "샐러드·수프","en": "Salad & Soup",  "ja": "サラダ・スープ","zh": "沙拉·汤"}},
            {"id": "bread",  "name": {"ko": "빵·샌드위치","en": "Bread & Sandwich","ja": "パン・サンドイッチ","zh": "面包·三明治"}},
            {"id": "baking", "name": {"ko": "베이킹·디저트","en": "Baking & Dessert","ja": "ベーキング・デザート","zh": "烘焙·甜点"}},
        ],
    },
    "japanese": {
        "name": {"ko": "일식", "en": "Japanese", "ja": "和食", "zh": "日餐"},
        "color": "#8e44ad",
        "sub": [
            {"id": "sushi",  "name": {"ko": "초밥·회",   "en": "Sushi & Sashimi", "ja": "寿司・刺身",   "zh": "寿司·刺身"}},
            {"id": "ramen",  "name": {"ko": "라멘·우동", "en": "Ramen & Udon",    "ja": "ラーメン・うどん","zh": "拉面·乌冬"}},
            {"id": "donburi","name": {"ko": "덮밥·정식", "en": "Rice Bowls",      "ja": "丼・定食",      "zh": "盖饭·套餐"}},
            {"id": "tempura","name": {"ko": "튀김·구이", "en": "Tempura & Grill", "ja": "天ぷら・焼き物","zh": "天妇罗·烤物"}},
            {"id": "miso",   "name": {"ko": "국·찜",     "en": "Soup & Steamed",  "ja": "汁物・蒸し物",  "zh": "汤·蒸菜"}},
        ],
    },
}

UI_TEXT = {
    "site_title": {"ko": "Basic Cook", "en": "Basic Cook", "ja": "Basic Cook", "zh": "Basic Cook"},
    "tagline":    {
        "ko": "요리를 처음 시작하는 당신을 위한 레시피",
        "en": "Simple recipes for everyone",
        "ja": "はじめての料理に、やさしいレシピ",
        "zh": "为厨房新手准备的简单食谱",
    },
    "explore":    {"ko": "메뉴 둘러보기", "en": "Explore Menus", "ja": "メニューを見る", "zh": "浏览菜单"},
    "categories": {"ko": "카테고리",      "en": "Categories",    "ja": "カテゴリー",     "zh": "分类"},
    "recipes":    {"ko": "레시피",        "en": "Recipes",        "ja": "レシピ",         "zh": "食谱"},
    "back":       {"ko": "← 뒤로",       "en": "← Back",         "ja": "← 戻る",         "zh": "← 返回"},
    "footer":     {
        "ko": "© 2026 Basic Cook — 누구나 쉽게 만드는 맛있는 요리",
        "en": "© 2026 Basic Cook — Delicious food made simple",
        "ja": "© 2026 Basic Cook — だれでも作れる美味しい料理",
        "zh": "© 2026 Basic Cook — 人人都能做的美味料理",
    },
    "story_label": {"ko": "만들게 된 이유", "en": "Why I Made This", "ja": "作った理由", "zh": "创作缘由"},
    "story": {
        "ko": (
            "이 페이지를 만든 저 또한 요리를 잘 알지 못하던 시절이 있었고, "
            "혼자 거진 10년을 살면서 느낀 요리하면서 레시피 노하우 등을 담고 싶었습니다.\n"
            "요리를 못하는 것이 잘못은 아닙니다. "
            "허나 요리를 잘함으로써 이걸 읽고 있는 여러분에게 매력포인트를 하나 더 얹게 되는 그 점이 마음에 들어 만들게 되었습니다."
        ),
        "en": (
            "I too had a time when I knew very little about cooking. "
            "After living alone for nearly ten years, I wanted to put together the recipe know-how and lessons I picked up along the way.\n"
            "Not being able to cook is nothing to be ashamed of. "
            "But learning to cook well adds one more thing that makes you genuinely attractive — and that thought is what drove me to build this."
        ),
        "ja": (
            "このページを作った私自身も、料理をよく知らなかった時期がありました。"
            "一人暮らしをほぼ10年続ける中で感じた料理のノウハウやコツを残したいと思いました。\n"
            "料理ができないことは恥ずかしいことではありません。"
            "ただ、料理が上手になることで、これを読んでいるあなたの魅力がひとつ増える。その点が気に入って、このサイトを作りました。"
        ),
        "zh": (
            "制作这个页面的我，也曾经历过对烹饪一无所知的时期。"
            "一个人生活了将近十年，我想把这些年积累的烹饪心得与食谱技巧整理下来。\n"
            "不会做饭并不是什么过错。"
            "但学会做菜，会让正在读这篇文章的你多一个让人眼前一亮的魅力点——正是这一点打动了我，让我决定做这个网站。"
        ),
    },
}
