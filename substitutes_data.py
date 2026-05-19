SUBSTITUTES = [
    # ── Dairy ──────────────────────────────────────────────────────
    {
        "id": "butter",
        "group": "dairy",
        "original": {"ko": "버터", "en": "Butter", "ja": "バター", "zh": "黄油"},
        "subs": [
            {
                "item": {"ko": "식물성 오일", "en": "Vegetable Oil", "ja": "植物油", "zh": "植物油"},
                "ratio": {"ko": "버터 100g → 오일 80ml", "en": "100g butter → 80ml oil", "ja": "バター100g → 油80ml", "zh": "黄油100g → 油80ml"},
                "note": {"ko": "수분이 없어 결이 달라질 수 있으나 촉촉함은 유지돼요.", "en": "No water content, so texture may differ slightly, but moisture is retained.", "ja": "水分がないため食感が変わることがありますが、しっとり感は保てます。", "zh": "无水分，口感可能略有不同，但湿润度能保持。"},
                "best_for": {"ko": "케이크, 머핀", "en": "Cakes, muffins", "ja": "ケーキ、マフィン", "zh": "蛋糕、松饼"},
            },
            {
                "item": {"ko": "코코넛오일", "en": "Coconut Oil", "ja": "ココナッツオイル", "zh": "椰子油"},
                "ratio": {"ko": "버터 100g → 코코넛오일 80g", "en": "100g butter → 80g coconut oil", "ja": "バター100g → ココナッツオイル80g", "zh": "黄油100g → 椰子油80g"},
                "note": {"ko": "특유의 향이 날 수 있어요. 냉각하면 굳어요.", "en": "May impart a faint coconut flavor. Solidifies when cooled.", "ja": "ほのかにコクの風味が出ることがあります。冷やすと固まります。", "zh": "可能带有椰子香味。冷却后会凝固。"},
                "best_for": {"ko": "베이킹 전반", "en": "General baking", "ja": "全般的なお菓子作り", "zh": "各类烘焙"},
            },
        ],
        "tip": {"ko": "버터의 풍미가 중요한 버터쿠키 등에는 대체재 사용을 피하는 게 좋아요.", "en": "For recipes where butter flavor is key (like butter cookies), substitutes are not ideal.", "ja": "バタークッキーなどバター風味が重要なレシピでは代替品の使用を避けた方がいいでしょう。", "zh": "对于黄油风味至关重要的食谱（如黄油饼干），最好避免使用替代品。"},
    },
    {
        "id": "heavy-cream",
        "group": "dairy",
        "original": {"ko": "생크림", "en": "Heavy Cream", "ja": "生クリーム", "zh": "淡奶油"},
        "subs": [
            {
                "item": {"ko": "코코넛크림", "en": "Coconut Cream", "ja": "ココナッツクリーム", "zh": "椰子奶油"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "휘핑 가능하고 비건 대체에 최적이에요.", "en": "Whippable and the best vegan substitute.", "ja": "ホイップでき、ビーガンの代替として最適です。", "zh": "可以打发，是最佳纯素替代品。"},
                "best_for": {"ko": "휘핑크림, 파스타 소스", "en": "Whipped cream, pasta sauce", "ja": "ホイップクリーム、パスタソース", "zh": "奶油、意面酱"},
            },
            {
                "item": {"ko": "우유 + 버터", "en": "Milk + Butter", "ja": "牛乳 + バター", "zh": "牛奶 + 黄油"},
                "ratio": {"ko": "우유 200ml + 버터 40g (1컵 대체)", "en": "200ml milk + 40g butter per cup", "ja": "牛乳200ml + バター40g（1カップ分）", "zh": "200ml牛奶 + 40g黄油（替换1杯）"},
                "note": {"ko": "휘핑은 안 되지만 요리·베이킹에 사용 가능해요.", "en": "Cannot be whipped but works in cooking and baking.", "ja": "ホイップはできませんが、料理やお菓子作りに使えます。", "zh": "无法打发，但可用于烹饪和烘焙。"},
                "best_for": {"ko": "소스, 수프, 케이크", "en": "Sauces, soups, cakes", "ja": "ソース、スープ、ケーキ", "zh": "酱汁、汤、蛋糕"},
            },
        ],
        "tip": {"ko": "휘핑이 필요한 경우엔 코코넛크림을 하루 전날 냉장 보관 후 윗부분만 사용하세요.", "en": "For whipping, refrigerate coconut cream overnight and use only the solid top layer.", "ja": "ホイップする場合は、ココナッツクリームを前日から冷蔵し、固形の上層だけを使いましょう。", "zh": "需要打发时，将椰子奶油冷藏一夜，只使用顶部固态部分。"},
    },
    {
        "id": "milk",
        "group": "dairy",
        "original": {"ko": "우유", "en": "Milk", "ja": "牛乳", "zh": "牛奶"},
        "subs": [
            {
                "item": {"ko": "두유", "en": "Soy Milk", "ja": "豆乳", "zh": "豆浆"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "무가당 두유를 사용하면 맛 차이가 거의 없어요.", "en": "Unsweetened soy milk tastes almost identical.", "ja": "無糖の豆乳を使えば味の差はほとんどありません。", "zh": "使用无糖豆浆几乎没有味道差异。"},
                "best_for": {"ko": "베이킹, 소스 전반", "en": "Baking, sauces", "ja": "お菓子作り、ソース全般", "zh": "烘焙、各类酱汁"},
            },
            {
                "item": {"ko": "귀리 우유", "en": "Oat Milk", "ja": "オーツミルク", "zh": "燕麦奶"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "단맛이 약간 있어요. 커피나 시리얼에 잘 어울려요.", "en": "Slightly sweet. Great with coffee or cereal.", "ja": "ほんのり甘みがあります。コーヒーやシリアルに合います。", "zh": "略带甜味，与咖啡或麦片搭配效果好。"},
                "best_for": {"ko": "음료, 팬케이크", "en": "Drinks, pancakes", "ja": "飲み物、パンケーキ", "zh": "饮品、煎饼"},
            },
        ],
        "tip": {"ko": "산이 있는 레시피(요거트 대신)에는 식물성 우유에 식초 1티스푼을 넣어 버터밀크 효과를 내세요.", "en": "For acidic recipes, add 1 tsp vinegar to plant milk to mimic buttermilk.", "ja": "酸性のレシピには、植物性ミルクに小さじ1の酢を加えてバターミルク効果を出しましょう。", "zh": "对于需要酸性的食谱，在植物奶中加1茶匙醋来模拟白脱牛奶效果。"},
    },
    {
        "id": "cream-cheese",
        "group": "dairy",
        "original": {"ko": "크림치즈", "en": "Cream Cheese", "ja": "クリームチーズ", "zh": "奶油芝士"},
        "subs": [
            {
                "item": {"ko": "그릭 요거트", "en": "Greek Yogurt", "ja": "ギリシャヨーグルト", "zh": "希腊酸奶"},
                "ratio": {"ko": "1:1 동량 대체 (물기 제거 후)", "en": "1:1 after draining excess liquid", "ja": "水気を切った後1:1で代替", "zh": "沥干水分后1:1替换"},
                "note": {"ko": "산미가 있고 더 가벼워요. 치즈케이크에 잘 맞아요.", "en": "More tangy and lighter. Works well in cheesecake.", "ja": "酸味があり、よりあっさりしています。チーズケーキに合います。", "zh": "更酸、更轻盈，适合芝士蛋糕。"},
                "best_for": {"ko": "치즈케이크, 디핑 소스", "en": "Cheesecake, dips", "ja": "チーズケーキ、ディップソース", "zh": "芝士蛋糕、蘸酱"},
            },
        ],
        "tip": {"ko": "크림치즈 프로스팅에는 마스카포네가 가장 유사한 대체재예요.", "en": "Mascarpone is the closest substitute for cream cheese frosting.", "ja": "クリームチーズのフロスティングには、マスカルポーネが最も近い代替品です。", "zh": "对于奶油芝士霜，马斯卡彭奶酪是最接近的替代品。"},
    },
    {
        "id": "parmesan",
        "group": "dairy",
        "original": {"ko": "파마산치즈", "en": "Parmesan", "ja": "パルメザンチーズ", "zh": "帕玛森芝士"},
        "subs": [
            {
                "item": {"ko": "페코리노 로마노", "en": "Pecorino Romano", "ja": "ペコリーノロマーノ", "zh": "佩科里诺罗马诺"},
                "ratio": {"ko": "동량 대체, 더 짤 수 있으니 양 조절", "en": "Use same amount, but it is saltier so adjust", "ja": "同量で代替。より塩辛いので量を調整", "zh": "等量替换，但更咸，需调整用量"},
                "note": {"ko": "양젖 치즈라 특유의 풍미가 있어요.", "en": "Made from sheep's milk with a distinct sharp flavor.", "ja": "羊乳のチーズで独特の風味があります。", "zh": "羊奶制成，有独特的浓郁风味。"},
                "best_for": {"ko": "파스타, 리조또", "en": "Pasta, risotto", "ja": "パスタ、リゾット", "zh": "意面、意式烩饭"},
            },
            {
                "item": {"ko": "영양효모 (비건)", "en": "Nutritional Yeast (vegan)", "ja": "ニュートリショナルイースト（ビーガン）", "zh": "营养酵母（纯素）"},
                "ratio": {"ko": "파마산 2큰술 → 영양효모 3큰술", "en": "2 tbsp parmesan → 3 tbsp nutritional yeast", "ja": "パルメザン大さじ2 → ニュートリショナルイースト大さじ3", "zh": "帕玛森2汤匙 → 营养酵母3汤匙"},
                "note": {"ko": "고소하고 치즈 풍미가 나지만 녹지는 않아요.", "en": "Nutty cheesy flavor but does not melt.", "ja": "ナッツのようなチーズ風味ですが、溶けません。", "zh": "有坚果奶酪风味，但不会融化。"},
                "best_for": {"ko": "파스타 토핑, 샐러드", "en": "Pasta topping, salad", "ja": "パスタのトッピング、サラダ", "zh": "意面配料、沙拉"},
            },
        ],
        "tip": {"ko": "카르보나라처럼 파마산이 핵심인 요리는 최대한 정석 재료를 써주세요.", "en": "For dishes like carbonara where parmesan is essential, try to use the real thing.", "ja": "カルボナーラのようにパルメザンが重要な料理には、できるだけ本物を使いましょう。", "zh": "对于卡邦拉等帕玛森芝士至关重要的菜肴，尽量使用真正的食材。"},
    },
    # ── Flour ──────────────────────────────────────────────────────
    {
        "id": "cake-flour",
        "group": "flour",
        "original": {"ko": "박력분", "en": "Cake Flour", "ja": "薄力粉", "zh": "低筋面粉"},
        "subs": [
            {
                "item": {"ko": "중력분 + 전분", "en": "All-purpose Flour + Cornstarch", "ja": "中力粉 + コーンスターチ", "zh": "中筋面粉 + 玉米淀粉"},
                "ratio": {"ko": "중력분 90g + 전분 10g = 박력분 100g", "en": "90g all-purpose + 10g cornstarch = 100g cake flour", "ja": "中力粉90g + コーンスターチ10g = 薄力粉100g", "zh": "中筋面粉90g + 玉米淀粉10g = 低筋面粉100g"},
                "note": {"ko": "단백질 함량을 낮춰 박력분과 유사한 효과를 내요.", "en": "Lowers protein content to mimic cake flour properties.", "ja": "たんぱく質含量を下げ、薄力粉に近い効果を出します。", "zh": "降低蛋白质含量，模拟低筋面粉的效果。"},
                "best_for": {"ko": "케이크, 쿠키", "en": "Cakes, cookies", "ja": "ケーキ、クッキー", "zh": "蛋糕、饼干"},
            },
        ],
        "tip": {"ko": "박력분은 글루텐 함량이 낮아 부드러운 식감을 만들어요. 중력분을 쓰면 더 쫄깃해질 수 있어요.", "en": "Cake flour has low gluten for a tender crumb. Using all-purpose flour will make the texture chewier.", "ja": "薄力粉はグルテン含量が低く、柔らかい食感を作ります。中力粉を使うと食感がもちもちになることがあります。", "zh": "低筋面粉面筋含量低，能产生酥软口感。使用中筋面粉会使口感更有嚼劲。"},
    },
    {
        "id": "starch",
        "group": "flour",
        "original": {"ko": "전분", "en": "Cornstarch", "ja": "コーンスターチ", "zh": "淀粉"},
        "subs": [
            {
                "item": {"ko": "쌀가루", "en": "Rice Flour", "ja": "米粉", "zh": "米粉"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "무색 투명하게 걸쭉해져요. 냉동 후에도 잘 유지돼요.", "en": "Thickens clear and stable. Holds up well after freezing.", "ja": "透明にとろみがつきます。冷凍後も安定しています。", "zh": "会变得透明浓稠，冷冻后依然稳定。"},
                "best_for": {"ko": "소스, 수프 농도 조절", "en": "Sauces, soups", "ja": "ソース、スープのとろみ付け", "zh": "酱汁、汤的浓稠度调节"},
            },
            {
                "item": {"ko": "감자전분", "en": "Potato Starch", "ja": "片栗粉", "zh": "土豆淀粉"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "더 강한 점성. 한식에서 많이 씀.", "en": "Stronger thickening power. Common in Korean cooking.", "ja": "より強いとろみ。韓国料理でよく使われます。", "zh": "增稠效果更强，在韩国烹饪中常用。"},
                "best_for": {"ko": "탕수육, 잡채", "en": "Sweet and sour dishes, japchae", "ja": "酢豚、チャプチェ", "zh": "糖醋菜肴、杂菜"},
            },
        ],
        "tip": {"ko": "전분을 찬물에 먼저 풀어야 뭉치지 않아요.", "en": "Always dissolve starch in cold water first to prevent lumps.", "ja": "澱粉はまず冷水で溶かすことで、ダマになりません。", "zh": "淀粉要先用冷水溶解，防止结块。"},
    },
    {
        "id": "baking-powder",
        "group": "flour",
        "original": {"ko": "베이킹파우더", "en": "Baking Powder", "ja": "ベーキングパウダー", "zh": "泡打粉"},
        "subs": [
            {
                "item": {"ko": "베이킹소다 + 크림 오브 타르타르", "en": "Baking Soda + Cream of Tartar", "ja": "重曹 + クリームオブタータ", "zh": "小苏打 + 塔塔粉"},
                "ratio": {"ko": "베이킹파우더 1작은술 → 소다 1/4 + 타르타르 1/2 작은술", "en": "1 tsp baking powder → 1/4 tsp soda + 1/2 tsp cream of tartar", "ja": "ベーキングパウダー小さじ1 → 重曹1/4 + タータール1/2小さじ", "zh": "泡打粉1茶匙 → 小苏打1/4 + 塔塔粉1/2茶匙"},
                "note": {"ko": "산성 성분이 없는 레시피에 적합해요.", "en": "Best for recipes without acidic ingredients.", "ja": "酸性成分がないレシピに最適です。", "zh": "适合不含酸性成分的食谱。"},
                "best_for": {"ko": "케이크, 머핀, 팬케이크", "en": "Cakes, muffins, pancakes", "ja": "ケーキ、マフィン、パンケーキ", "zh": "蛋糕、松饼、煎饼"},
            },
        ],
        "tip": {"ko": "베이킹파우더는 습기를 흡수하므로 서늘한 곳에 밀봉 보관하세요.", "en": "Keep baking powder sealed in a cool, dry place as it absorbs moisture.", "ja": "ベーキングパウダーは湿気を吸収するので、涼しい場所に密封保存しましょう。", "zh": "泡打粉会吸收湿气，请密封保存在阴凉干燥处。"},
    },
    {
        "id": "baking-soda",
        "group": "flour",
        "original": {"ko": "베이킹소다", "en": "Baking Soda", "ja": "重曹", "zh": "小苏打"},
        "subs": [
            {
                "item": {"ko": "베이킹파우더", "en": "Baking Powder", "ja": "ベーキングパウダー", "zh": "泡打粉"},
                "ratio": {"ko": "베이킹소다 1 → 베이킹파우더 3", "en": "1 part baking soda → 3 parts baking powder", "ja": "重曹1 → ベーキングパウダー3", "zh": "小苏打1 → 泡打粉3"},
                "note": {"ko": "팽창력이 약해서 더 많이 써야 해요. 짠맛이 날 수 있어요.", "en": "Weaker lift, so more is needed. May taste slightly salty.", "ja": "膨張力が弱いので多く使う必要があります。少し塩味がでることも。", "zh": "膨发力较弱，需要用更多。可能略带咸味。"},
                "best_for": {"ko": "베이킹 전반 (급할 때)", "en": "General baking (in a pinch)", "ja": "全般的なお菓子作り（緊急時）", "zh": "各类烘焙（紧急情况）"},
            },
        ],
        "tip": {"ko": "베이킹소다는 산성 재료(레몬즙, 식초, 요거트)와 반응해야 효과가 나요.", "en": "Baking soda needs an acidic ingredient (lemon juice, vinegar, yogurt) to activate.", "ja": "重曹はレモン汁・酢・ヨーグルトなどの酸性食材と反応して効果が出ます。", "zh": "小苏打需要与酸性食材（柠檬汁、醋、酸奶）反应才能起效。"},
    },
    # ── Sauce ──────────────────────────────────────────────────────
    {
        "id": "mirin",
        "group": "sauce",
        "original": {"ko": "미림", "en": "Mirin", "ja": "みりん", "zh": "味醂"},
        "subs": [
            {
                "item": {"ko": "청주 + 설탕", "en": "Sake + Sugar", "ja": "酒 + 砂糖", "zh": "清酒 + 砂糖"},
                "ratio": {"ko": "미림 1큰술 → 청주 1큰술 + 설탕 1작은술", "en": "1 tbsp mirin → 1 tbsp sake + 1 tsp sugar", "ja": "みりん大さじ1 → 酒大さじ1 + 砂糖小さじ1", "zh": "味醂1汤匙 → 清酒1汤匙 + 白砂糖1茶匙"},
                "note": {"ko": "단맛과 윤기가 비슷하게 나요.", "en": "Gives similar sweetness and glaze.", "ja": "甘みと艶が似たような仕上がりになります。", "zh": "能产生相似的甜味和光泽。"},
                "best_for": {"ko": "데리야끼, 조림, 볶음", "en": "Teriyaki, braised dishes, stir-fry", "ja": "照り焼き、煮物、炒め物", "zh": "照烧、红烧、炒菜"},
            },
        ],
        "tip": {"ko": "미림은 알코올이 있어 고기 잡내를 잡는 효과도 있어요. 청주 대신 쓸 때 단맛이 더해진다는 것을 기억하세요.", "en": "Mirin has alcohol that removes meaty odors. Remember it adds sweetness when substituting sake.", "ja": "みりんはアルコールが含まれており、肉の臭み消しの効果もあります。酒の代わりに使うと甘みが増すことを覚えておきましょう。", "zh": "味醂含有酒精，有去腥效果。用来替代清酒时，记住它会增加甜味。"},
    },
    {
        "id": "oyster-sauce",
        "group": "sauce",
        "original": {"ko": "굴소스", "en": "Oyster Sauce", "ja": "オイスターソース", "zh": "蚝油"},
        "subs": [
            {
                "item": {"ko": "간장 + 설탕 + 전분물", "en": "Soy Sauce + Sugar + Starch Water", "ja": "醤油 + 砂糖 + 水溶き片栗粉", "zh": "酱油 + 砂糖 + 淀粉水"},
                "ratio": {"ko": "간장 1큰술 + 설탕 1작은술 + 전분물 1작은술", "en": "1 tbsp soy + 1 tsp sugar + 1 tsp starch water", "ja": "醤油大さじ1 + 砂糖小さじ1 + 水溶き片栗粉小さじ1", "zh": "酱油1汤匙 + 砂糖1茶匙 + 淀粉水1茶匙"},
                "note": {"ko": "굴향은 없지만 감칠맛과 색은 비슷해요.", "en": "No oyster aroma but similar umami and color.", "ja": "カキの風味はありませんが、旨みと色は似ています。", "zh": "没有蚝香，但鲜味和颜色相近。"},
                "best_for": {"ko": "볶음 요리", "en": "Stir-fried dishes", "ja": "炒め物", "zh": "炒菜"},
            },
            {
                "item": {"ko": "버섯소스 (비건)", "en": "Mushroom Sauce (vegan)", "ja": "マッシュルームソース（ビーガン）", "zh": "蘑菇酱（纯素）"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "채식주의자에게 최고의 대안이에요.", "en": "Best vegan alternative for oyster sauce.", "ja": "ビーガンにとって最高の代替品です。", "zh": "最佳纯素替代品。"},
                "best_for": {"ko": "볶음, 소스", "en": "Stir-fry, sauces", "ja": "炒め物、ソース", "zh": "炒菜、酱汁"},
            },
        ],
        "tip": {"ko": "굴소스는 개봉 후 냉장 보관하고 3개월 내 사용하세요.", "en": "After opening, refrigerate oyster sauce and use within 3 months.", "ja": "オイスターソースは開封後に冷蔵保存し、3ヶ月以内に使いましょう。", "zh": "蚝油开封后冷藏保存，3个月内使用完。"},
    },
    {
        "id": "tsuyu",
        "group": "sauce",
        "original": {"ko": "쯔유", "en": "Tsuyu (Mentsuyu)", "ja": "つゆ（めんつゆ）", "zh": "白汁（面酱）"},
        "subs": [
            {
                "item": {"ko": "간장 + 미림 + 가쓰오다시", "en": "Soy Sauce + Mirin + Dashi", "ja": "醤油 + みりん + だし", "zh": "酱油 + 味醂 + 高汤"},
                "ratio": {"ko": "간장 3 + 미림 2 + 다시 1 비율로 혼합", "en": "Mix soy 3 : mirin 2 : dashi 1", "ja": "醤油3 + みりん2 + だし1の割合で混ぜる", "zh": "按酱油3 : 味醂2 : 高汤1的比例混合"},
                "note": {"ko": "가쓰오 향이 나는 일본식 간장 소스가 돼요.", "en": "Creates a Japanese soy-based sauce with dashi aroma.", "ja": "かつおの香りがする和風醤油ソースになります。", "zh": "制成带有木鱼高汤香气的日式酱汁。"},
                "best_for": {"ko": "우동, 소바, 덮밥", "en": "Udon, soba, rice bowls", "ja": "うどん、そば、丼", "zh": "乌冬面、荞麦面、盖饭"},
            },
        ],
        "tip": {"ko": "쯔유는 농축 정도에 따라 희석 비율이 다르니 제품 뒷면을 확인하세요.", "en": "Tsuyu concentration varies by product — check the label for dilution ratio.", "ja": "つゆは製品によって濃縮度が異なるので、パッケージ裏面で希釈の割合を確認しましょう。", "zh": "白汁浓缩度因产品而异，请查看包装背面的稀释比例。"},
    },
    {
        "id": "doubanjiang",
        "group": "sauce",
        "original": {"ko": "두반장", "en": "Doubanjiang", "ja": "豆板醤", "zh": "豆瓣酱"},
        "subs": [
            {
                "item": {"ko": "고추장 + 된장 (한식버전)", "en": "Gochujang + Doenjang (Korean version)", "ja": "コチュジャン + テンジャン（韓国版）", "zh": "辣酱 + 大酱（韩式版本）"},
                "ratio": {"ko": "두반장 1큰술 → 고추장 1/2 + 된장 1/2 큰술", "en": "1 tbsp doubanjiang → 1/2 tbsp gochujang + 1/2 tbsp doenjang", "ja": "豆板醤大さじ1 → コチュジャン1/2 + テンジャン1/2大さじ", "zh": "豆瓣酱1汤匙 → 辣酱1/2 + 大酱1/2汤匙"},
                "note": {"ko": "발효 향과 감칠맛은 비슷하지만 맵기가 다를 수 있어요.", "en": "Similar fermented aroma and umami, but spice level may differ.", "ja": "発酵の香りと旨みは似ていますが、辛さが異なる場合があります。", "zh": "发酵香味和鲜味相似，但辣度可能不同。"},
                "best_for": {"ko": "마파두부, 볶음요리", "en": "Mapo tofu, stir-fry", "ja": "麻婆豆腐、炒め物", "zh": "麻婆豆腐、炒菜"},
            },
        ],
        "tip": {"ko": "두반장은 볶아야 제 맛이 나요. 기름에 먼저 볶은 뒤 다른 재료를 넣으세요.", "en": "Doubanjiang must be stir-fried in oil first to develop its full flavor before adding other ingredients.", "ja": "豆板醤は油で炒めてこそ本来の味が出ます。まず油で炒めてから他の食材を加えましょう。", "zh": "豆瓣酱需要先在油中炒香才能发挥全部风味，之后再加入其他食材。"},
    },
    # ── Egg ────────────────────────────────────────────────────────
    {
        "id": "egg-baking",
        "group": "egg",
        "original": {"ko": "계란 (베이킹용)", "en": "Egg (for baking)", "ja": "卵（お菓子作り用）", "zh": "鸡蛋（烘焙用）"},
        "subs": [
            {
                "item": {"ko": "아마씨 + 물 (플랙스에그)", "en": "Flaxseed + Water (flax egg)", "ja": "亜麻仁 + 水（フラックスエッグ）", "zh": "亚麻籽 + 水（亚麻蛋）"},
                "ratio": {"ko": "아마씨 1큰술 + 물 3큰술 → 계란 1개", "en": "1 tbsp ground flaxseed + 3 tbsp water = 1 egg", "ja": "亜麻仁大さじ1 + 水大さじ3 → 卵1個分", "zh": "亚麻籽粉1汤匙 + 水3汤匙 → 1个鸡蛋"},
                "note": {"ko": "5분 불린 뒤 사용하세요. 결합력이 좋아요.", "en": "Let sit 5 minutes before using. Good binding power.", "ja": "5分ふやかしてから使用します。結合力が良いです。", "zh": "静置5分钟后使用，结合力好。"},
                "best_for": {"ko": "쿠키, 머핀, 팬케이크", "en": "Cookies, muffins, pancakes", "ja": "クッキー、マフィン、パンケーキ", "zh": "饼干、松饼、煎饼"},
            },
            {
                "item": {"ko": "바나나 (으깬 것)", "en": "Mashed Banana", "ja": "マッシュバナナ", "zh": "香蕉泥"},
                "ratio": {"ko": "바나나 1/4개 으깬 것 → 계란 1개", "en": "1/4 mashed banana = 1 egg", "ja": "バナナ1/4個を潰したもの → 卵1個分", "zh": "1/4根香蕉泥 → 1个鸡蛋"},
                "note": {"ko": "바나나 향이 나요. 결합력과 수분 모두 제공해요.", "en": "Adds banana flavor. Provides both binding and moisture.", "ja": "バナナの風味が加わります。結合力と水分の両方を提供します。", "zh": "会带来香蕉风味，同时提供结合力和水分。"},
                "best_for": {"ko": "바나나 빵, 머핀", "en": "Banana bread, muffins", "ja": "バナナブレッド、マフィン", "zh": "香蕉面包、松饼"},
            },
            {
                "item": {"ko": "사과 소스 (무가당)", "en": "Unsweetened Applesauce", "ja": "無糖アップルソース", "zh": "无糖苹果酱"},
                "ratio": {"ko": "3큰술 → 계란 1개", "en": "3 tbsp = 1 egg", "ja": "大さじ3 → 卵1個分", "zh": "3汤匙 → 1个鸡蛋"},
                "note": {"ko": "수분과 단맛을 추가해요. 팽창력은 없어요.", "en": "Adds moisture and mild sweetness. No leavening.", "ja": "水分と甘みを加えます。膨張力はありません。", "zh": "增加水分和淡淡甜味，无膨发效果。"},
                "best_for": {"ko": "케이크, 브라우니", "en": "Cakes, brownies", "ja": "ケーキ、ブラウニー", "zh": "蛋糕、布朗尼"},
            },
        ],
        "tip": {"ko": "계란의 역할이 주로 팽창이라면 아마씨에그, 구조 형성이라면 두부가 좋아요.", "en": "If the egg's main role is leavening, use flax egg. If structure, use silken tofu.", "ja": "卵の主な役割が膨張なら亜麻仁エッグ、構造形成なら絹豆腐が向いています。", "zh": "如果鸡蛋主要起膨发作用，用亚麻蛋；如果是结构作用，用嫩豆腐。"},
    },
    # ── Other ──────────────────────────────────────────────────────
    {
        "id": "mascarpone",
        "group": "other",
        "original": {"ko": "마스카포네", "en": "Mascarpone", "ja": "マスカルポーネ", "zh": "马斯卡彭"},
        "subs": [
            {
                "item": {"ko": "크림치즈 + 생크림", "en": "Cream Cheese + Heavy Cream", "ja": "クリームチーズ + 生クリーム", "zh": "奶油芝士 + 淡奶油"},
                "ratio": {"ko": "크림치즈 200g + 생크림 2큰술을 부드럽게 섞기", "en": "200g cream cheese + 2 tbsp heavy cream blended smooth", "ja": "クリームチーズ200g + 生クリーム大さじ2を滑らかに混ぜる", "zh": "200g奶油芝士 + 2汤匙淡奶油搅拌至顺滑"},
                "note": {"ko": "마스카포네보다 산미가 살짝 강해요.", "en": "Slightly more tangy than mascarpone.", "ja": "マスカルポーネより少し酸味が強いです。", "zh": "比马斯卡彭略带更多酸味。"},
                "best_for": {"ko": "티라미수, 파스타 소스", "en": "Tiramisu, pasta sauce", "ja": "ティラミス、パスタソース", "zh": "提拉米苏、意面酱"},
            },
        ],
        "tip": {"ko": "티라미수의 경우 크림치즈 + 생크림 조합이 가장 가까운 맛을 내요.", "en": "For tiramisu, the cream cheese + heavy cream combo comes closest to the real thing.", "ja": "ティラミスには、クリームチーズ＋生クリームの組み合わせが最も近い味になります。", "zh": "做提拉米苏时，奶油芝士+淡奶油的组合最接近原味。"},
    },
    {
        "id": "silken-tofu",
        "group": "other",
        "original": {"ko": "연두부 (부드러운 두부)", "en": "Silken Tofu", "ja": "絹豆腐", "zh": "嫩豆腐"},
        "subs": [
            {
                "item": {"ko": "두부 + 소량의 물", "en": "Firm Tofu + Water", "ja": "木綿豆腐 + 少量の水", "zh": "老豆腐 + 少量水"},
                "ratio": {"ko": "단단한 두부를 믹서로 곱게 갈 때 물을 조금씩 추가", "en": "Blend firm tofu smooth, adding small amounts of water", "ja": "木綿豆腐をミキサーで細かく砕き、少しずつ水を加える", "zh": "将老豆腐用搅拌机打碎，逐渐加入少量水"},
                "note": {"ko": "맛은 같지만 질감이 약간 다를 수 있어요.", "en": "Same taste but texture may differ slightly.", "ja": "味は同じですが、食感が少し異なる場合があります。", "zh": "口感相同，但质地可能略有不同。"},
                "best_for": {"ko": "스무디, 소스, 드레싱", "en": "Smoothies, sauces, dressings", "ja": "スムージー、ソース、ドレッシング", "zh": "冰沙、酱汁、沙拉酱"},
            },
        ],
        "tip": {"ko": "연두부는 수분이 많아 요리에 넣기 전 체에 밭쳐 잠깐 물기를 빼주면 좋아요.", "en": "Silken tofu has high water content — drain briefly through a sieve before using.", "ja": "絹豆腐は水分が多いので、料理に加える前に少しの間ざるに乗せて水気を切るといいでしょう。", "zh": "嫩豆腐水分多，加入菜肴前最好用网筛短暂沥干水分。"},
    },
    {
        "id": "sake",
        "group": "other",
        "original": {"ko": "청주", "en": "Sake (Cooking)", "ja": "料理酒", "zh": "清酒（料理用）"},
        "subs": [
            {
                "item": {"ko": "미림 (단맛 고려)", "en": "Mirin (note added sweetness)", "ja": "みりん（甘みに注意）", "zh": "味醂（注意额外甜度）"},
                "ratio": {"ko": "1:1 대체, 설탕 양 줄이기", "en": "1:1, reduce sugar in recipe", "ja": "1:1で代替、砂糖量を減らす", "zh": "1:1替换，减少食谱中的糖量"},
                "note": {"ko": "단맛이 추가돼요. 조림이나 볶음에 잘 맞아요.", "en": "Adds sweetness. Works well in braised and stir-fried dishes.", "ja": "甘みが加わります。煮物や炒め物に向いています。", "zh": "会增加甜味，适合红烧和炒菜。"},
                "best_for": {"ko": "고기 요리, 조림", "en": "Meat dishes, braised foods", "ja": "肉料理、煮物", "zh": "肉类菜肴、红烧菜"},
            },
            {
                "item": {"ko": "물 (향 없앨 때)", "en": "Water (to omit alcohol)", "ja": "水（アルコールなし）", "zh": "水（不需要酒精时）"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "잡내 제거 효과는 없지만 수분 보충용으로는 OK.", "en": "No deodorizing effect but fine for moisture.", "ja": "臭み消しの効果はありませんが、水分補給には使えます。", "zh": "没有去腥效果，但可以补充水分。"},
                "best_for": {"ko": "수프, 밥 짓기", "en": "Soups, cooking rice", "ja": "スープ、ご飯", "zh": "汤、煮饭"},
            },
        ],
        "tip": {"ko": "청주는 고기 잡내 제거와 풍미 향상 두 가지 역할을 해요. 대체재는 향 측면에선 미림이 더 좋아요.", "en": "Sake deodorizes meat and adds flavor. For aroma, mirin is the better substitute.", "ja": "料理酒は肉の臭み消しと風味アップの両方の役割があります。香りの面ではみりんの方が優れた代替品です。", "zh": "清酒有去腥和增香两个作用，在香气方面，味醂是更好的替代品。"},
    },
    {
        "id": "honey",
        "group": "other",
        "original": {"ko": "꿀", "en": "Honey", "ja": "はちみつ", "zh": "蜂蜜"},
        "subs": [
            {
                "item": {"ko": "메이플 시럽", "en": "Maple Syrup", "ja": "メープルシロップ", "zh": "枫糖浆"},
                "ratio": {"ko": "1:1 동량 대체", "en": "1:1 replacement", "ja": "1:1の等量で代替", "zh": "1:1等量替换"},
                "note": {"ko": "메이플 향이 나지만 단맛과 점도가 비슷해요.", "en": "Adds maple flavor but similar sweetness and viscosity.", "ja": "メープルの風味がありますが、甘みと粘度は似ています。", "zh": "带有枫糖香味，但甜度和粘度相近。"},
                "best_for": {"ko": "드레싱, 소스, 베이킹", "en": "Dressings, sauces, baking", "ja": "ドレッシング、ソース、お菓子作り", "zh": "沙拉酱、酱汁、烘焙"},
            },
            {
                "item": {"ko": "설탕 + 물", "en": "Sugar + Water", "ja": "砂糖 + 水", "zh": "砂糖 + 水"},
                "ratio": {"ko": "꿀 1큰술 → 설탕 1큰술 + 물 1/4작은술", "en": "1 tbsp honey → 1 tbsp sugar + 1/4 tsp water", "ja": "はちみつ大さじ1 → 砂糖大さじ1 + 水小さじ1/4", "zh": "蜂蜜1汤匙 → 砂糖1汤匙 + 水1/4茶匙"},
                "note": {"ko": "수분감이 약간 달라요. 꿀 특유의 풍미는 없어요.", "en": "Slightly different moisture. No honey flavor.", "ja": "水分感が少し異なります。はちみつ特有の風味はありません。", "zh": "水分略有不同，没有蜂蜜特有的风味。"},
                "best_for": {"ko": "베이킹, 음료", "en": "Baking, drinks", "ja": "お菓子作り、飲み物", "zh": "烘焙、饮品"},
            },
        ],
        "tip": {"ko": "꿀은 천연 항균 성분이 있어 장기 보관 가능해요. 결정화되면 따뜻한 물에 중탕하면 돌아와요.", "en": "Honey has natural antibacterial properties and keeps indefinitely. If crystallized, warm in a water bath to restore.", "ja": "はちみつは天然の抗菌成分があり長期保存できます。結晶化したら湯煎で元に戻せます。", "zh": "蜂蜜含有天然抗菌成分，可长期保存。结晶后用温水隔水加热即可恢复。"},
    },
]

SUBS_UI = {
    "page_title": {"ko": "대체 재료 가이드", "en": "Ingredient Substitutes", "ja": "代替食材ガイド", "zh": "替代食材指南"},
    "page_subtitle": {
        "ko": "재료가 없을 때 당황하지 마세요. 집에 있는 것으로 충분히 대체할 수 있어요.",
        "en": "Don't panic when you're missing an ingredient. You can substitute with what you have at home.",
        "ja": "食材がないときは慌てないで。家にあるもので十分代替できます。",
        "zh": "没有某种食材时不要慌，用家里现有的就能替代。",
    },
    "groups": {
        "dairy": {"ko": "유제품", "en": "Dairy", "ja": "乳製品", "zh": "乳制品"},
        "flour": {"ko": "가루·전분", "en": "Flour & Starch", "ja": "粉類・でんぷん", "zh": "面粉·淀粉"},
        "sauce": {"ko": "소스·조미료", "en": "Sauces & Seasonings", "ja": "ソース・調味料", "zh": "酱汁·调味料"},
        "egg": {"ko": "달걀", "en": "Eggs", "ja": "卵", "zh": "鸡蛋"},
        "other": {"ko": "기타", "en": "Other", "ja": "その他", "zh": "其他"},
    },
    "ratio_label": {"ko": "비율", "en": "Ratio", "ja": "割合", "zh": "比例"},
    "best_for_label": {"ko": "적합한 요리", "en": "Best for", "ja": "向いている料理", "zh": "适合菜肴"},
    "tip_label": {"ko": "팁", "en": "Tip", "ja": "コツ", "zh": "小贴士"},
}
