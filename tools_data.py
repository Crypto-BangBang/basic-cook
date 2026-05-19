TOOL_CATEGORIES = [
    {
        "id": "knives",
        "name": {"ko": "칼과 도마", "en": "Knives & Boards", "ja": "包丁・まな板", "zh": "刀具与砧板"},
        "color": "#c0392b",
        "tools": [
            {
                "id": "chef-knife",
                "name": {"ko": "셰프 나이프 (만능칼)", "en": "Chef's Knife", "ja": "牛刀（万能包丁）", "zh": "厨师刀"},
                "desc": {
                    "ko": "주방에서 가장 많이 쓰는 칼로, 채소 썰기부터 고기 손질까지 거의 모든 작업에 사용합니다. 칼날 길이는 보통 18-25cm이며, 초보자라면 20cm 정도가 적당합니다.",
                    "en": "The most-used knife in any kitchen, handling everything from vegetables to meat. Blade length is usually 18-25cm; 20cm is ideal for beginners.",
                    "ja": "野菜の下ごしらえから肉の処理まで、あらゆる調理に使える万能包丁。刃渡りは18〜25cmが一般的で、初心者には20cmがおすすめ。",
                    "zh": "厨房中用途最广的刀，从切蔬菜到处理肉类样样行。刀身长度一般18-25cm，新手用20cm的比较顺手。",
                },
                "tips": {
                    "ko": ["칼을 쥘 때는 엄지와 검지로 칼날 뒷부분을 잡아야 안전하고 힘이 잘 들어가요.", "도마 위에서 칼끝을 들지 말고 칼 앞부분을 축으로 흔들듯이 썰면 훨씬 빨라요.", "사용 후 손으로 씻고 물기를 바로 닦아야 녹슬지 않아요."],
                    "en": ["Grip the blade heel between thumb and index finger for control and safety.", "Rock the knife tip on the board rather than lifting it for faster chopping.", "Hand wash and dry immediately after use to prevent rust."],
                    "ja": ["親指と人差し指で刃のあごを挟んで持つと安定します。", "刃先を支点に前後に動かすと素早く切れます。", "使用後は手洗いしてすぐに水気を拭いてください。"],
                    "zh": ["用拇指和食指夹住刀跟，这样既安全又有力。", "以刀尖为支点前后摇摆切菜，速度更快。", "用完手洗并立即擦干，防止生锈。"],
                },
            },
            {
                "id": "paring-knife",
                "name": {"ko": "페어링 나이프 (소형 칼)", "en": "Paring Knife", "ja": "ペティナイフ", "zh": "水果刀"},
                "desc": {
                    "ko": "손에 들고 쓰는 작은 칼로, 과일 껍질 벗기기, 작은 채소 손질, 섬세한 칼집 넣기에 적합합니다. 칼날 길이는 8-10cm 정도예요.",
                    "en": "A small handheld knife for peeling fruit, trimming vegetables, and detailed work. Blade length is around 8-10cm.",
                    "ja": "果物の皮むきや小さな野菜の下ごしらえに使う小型の包丁。刃渡りは8〜10cmほど。",
                    "zh": "用于削皮、修整蔬菜和细致处理的小刀，刀身约8-10cm。",
                },
                "tips": {
                    "ko": ["마늘 껍질 벗길 때 칼 옆면으로 눌러 으깨면 훨씬 쉬워요.", "생강 껍질은 이 칼 뒷면(쇠 부분)으로 긁으면 깔끔하게 벗겨져요."],
                    "en": ["Crush garlic by pressing with the flat side of the blade — the skin peels off easily.", "Scrape ginger skin with the back of the blade for clean peeling."],
                    "ja": ["にんにくは刃の平らな部分で押しつぶすと皮が剥きやすくなります。", "しょうがの皮は刃の背でこそぎ取ると綺麗に剥けます。"],
                    "zh": ["用刀面拍压大蒜，皮就容易剥掉了。", "用刀背刮生姜皮，既快又干净。"],
                },
            },
            {
                "id": "cutting-board",
                "name": {"ko": "도마", "en": "Cutting Board", "ja": "まな板", "zh": "砧板"},
                "desc": {
                    "ko": "식재료를 자르는 작업대입니다. 나무, 플라스틱, 실리콘 재질이 있으며, 식재료별로 구분해서 쓰면 위생적입니다. 채소용·고기용·생선용을 따로 두는 게 이상적이에요.",
                    "en": "The surface you cut on. Available in wood, plastic, and silicone. Using separate boards for meat, fish, and vegetables is ideal for hygiene.",
                    "ja": "食材を切るための台。木製・プラスチック・シリコン製があります。衛生面から肉・魚・野菜用を分けて使うのが理想的。",
                    "zh": "切食材用的台面，有木制、塑料和硅胶材质。最好分开使用肉类、鱼类和蔬菜专用砧板。",
                },
                "tips": {
                    "ko": ["도마 아래에 젖은 행주를 깔면 미끄러지지 않아요.", "나무 도마는 사용 후 세제로 씻고 세워서 건조해야 곰팡이가 생기지 않아요.", "플라스틱 도마는 식기세척기에 넣어도 돼요."],
                    "en": ["Place a damp towel under the board to prevent slipping.", "Wash wooden boards with soap and stand upright to dry — laying flat causes mold.", "Plastic boards are dishwasher safe."],
                    "ja": ["濡れたふきんを下に敷くと滑り止めになります。", "木製まな板は使用後に立てて乾かすとカビが生えにくいです。", "プラスチック製は食洗機で洗えます。"],
                    "zh": ["底部垫湿布防滑效果很好。", "木质砧板洗后要竖起来晾干，平放容易发霉。", "塑料砧板可以放洗碗机清洗。"],
                },
            },
        ],
    },
    {
        "id": "pans",
        "name": {"ko": "가열 도구", "en": "Pots & Pans", "ja": "加熱調理器具", "zh": "锅具"},
        "color": "#e67e22",
        "tools": [
            {
                "id": "frying-pan",
                "name": {"ko": "프라이팬", "en": "Frying Pan", "ja": "フライパン", "zh": "平底锅"},
                "desc": {
                    "ko": "볶음, 구이, 부침 등 대부분의 조리에 사용하는 필수 도구입니다. 코팅 프라이팬(테프론)은 달라붙지 않아 초보자에게 적합하고, 주물 프라이팬은 열 보존이 좋아 스테이크에 유리합니다. 지름 26-28cm가 가장 범용적이에요.",
                    "en": "Essential for stir-frying, pan-frying, and sautéing. Non-stick (Teflon) pans are forgiving for beginners; cast iron retains heat well for searing. A 26-28cm diameter is the most versatile size.",
                    "ja": "炒め物、焼き物など幅広い料理に使う必須アイテム。テフロン加工は焦げ付きにくく初心者向け。26〜28cmが汎用性が高いです。",
                    "zh": "炒菜、煎食材的必备工具。不粘锅适合新手，铸铁锅保温好适合煎牛排。26-28cm的尺寸最通用。",
                },
                "tips": {
                    "ko": ["코팅 프라이팬은 강불에 빈 채로 달구면 코팅이 망가져요. 반드시 기름을 먼저 두르거나 재료를 넣은 뒤 가열하세요.", "나무 주걱이나 실리콘 주걱을 사용해야 코팅이 긁히지 않아요.", "처음 구매 후 키친타월로 기름을 얇게 발라 약불로 달궜다가 식히면 더 오래 써요."],
                    "en": ["Never heat a non-stick pan empty over high heat — it ruins the coating. Add oil or ingredients first.", "Use wooden or silicone spatulas to avoid scratching the coating.", "Season a new pan by wiping with oil and heating gently before first use."],
                    "ja": ["テフロンパンを空のまま強火にかけるとコーティングが傷みます。必ず油か食材を入れてから加熱を。", "コーティングを傷めないよう木製またはシリコン製のへらを使いましょう。", "新品は薄く油を塗って弱火で加熱すると長持ちします。"],
                    "zh": ["不粘锅不要空锅大火加热，会损坏涂层。先放油或食材再加热。", "用木铲或硅胶铲，避免刮花涂层。", "新锅开锅时涂一层薄油小火加热，能延长使用寿命。"],
                },
            },
            {
                "id": "saucepan",
                "name": {"ko": "편수 냄비 (소스팬)", "en": "Saucepan", "ja": "片手鍋", "zh": "单柄锅"},
                "desc": {
                    "ko": "국, 찌개, 파스타 면 삶기, 소스 만들기에 사용하는 1-2인용 냄비입니다. 손잡이가 한쪽에만 달려 있어 다루기 편해요. 18-20cm 크기가 1-2인 가구에 적당합니다.",
                    "en": "A one-handled pot for soups, sauces, and boiling pasta. Great for 1-2 people. 18-20cm is the right size for a small household.",
                    "ja": "スープ、ソース、パスタの茹で上げに使う片手鍋。1〜2人なら18〜20cmが使いやすいサイズ。",
                    "zh": "用于煮汤、做酱汁、煮意面的单柄锅。1-2人用18-20cm的尺寸最合适。",
                },
                "tips": {
                    "ko": ["면을 삶을 때는 물을 넉넉히 넣어야 면이 서로 달라붙지 않아요.", "소스를 졸일 때는 약불에서 자주 저어줘야 눌어붙지 않아요."],
                    "en": ["Use plenty of water when boiling pasta — too little and the noodles stick together.", "Stir sauces frequently when reducing over low heat to prevent scorching."],
                    "ja": ["パスタを茹でる際は水を多めに入れると麺が離れやすくなります。", "ソースを煮詰める際は弱火でこまめにかき混ぜましょう。"],
                    "zh": ["煮意面时多放水，防止面条粘连。", "熬酱汁时用小火并经常搅拌，防止糊底。"],
                },
            },
            {
                "id": "stockpot",
                "name": {"ko": "양수 냄비 (스톡팟)", "en": "Stockpot", "ja": "両手鍋", "zh": "汤锅"},
                "desc": {
                    "ko": "육수 내기, 대량 조리, 칼국수 등 많은 양의 음식을 끓일 때 사용하는 양쪽에 손잡이가 달린 큰 냄비입니다. 20-24cm가 4인 가구 기준으로 적당해요.",
                    "en": "A large two-handled pot for stocks, soups, and large-batch cooking. 20-24cm is right for a family of four.",
                    "ja": "出汁取りや大量調理に使う両手鍋。4人家族なら20〜24cmが適切。",
                    "zh": "用于熬高汤、大量烹饪的双耳大锅。4人家庭用20-24cm比较合适。",
                },
                "tips": {
                    "ko": ["육수를 낼 때는 처음에 센불로 끓인 뒤 거품을 걷어내고 약불로 낮춰야 맑은 국물이 나와요.", "냄비 두께가 두꺼울수록 열 분산이 균일해 눌어붙지 않아요."],
                    "en": ["For clear broth, bring to a boil over high heat, skim foam, then reduce to a gentle simmer.", "Thicker pots distribute heat more evenly and are less prone to scorching."],
                    "ja": ["澄んだ出汁を取るには、最初に強火で沸かしてアクを取り除き、弱火に落とします。", "鍋底が厚いほど熱が均一に広がり焦げ付きにくくなります。"],
                    "zh": ["熬清汤时先大火烧开撇去浮沫，再转小火慢炖，汤色会更清澈。", "锅底越厚，导热越均匀，越不容易糊底。"],
                },
            },
            {
                "id": "wok",
                "name": {"ko": "웍 (중화팬)", "en": "Wok", "ja": "中華鍋", "zh": "炒锅"},
                "desc": {
                    "ko": "중식 볶음 요리에 사용하는 반구형 팬입니다. 높은 온도와 불의 화력을 넓게 받아 '불향(웍헤이)'을 낼 수 있어요. 볶음밥이나 짜장면 등에 필수적입니다. 가정용 가스레인지에서도 충분히 활용 가능해요.",
                    "en": "A round-bottomed pan for Chinese stir-frying. Its shape allows high heat across a wide surface, creating 'wok hei' (breath of the wok). Essential for fried rice and noodles.",
                    "ja": "中華料理の炒め物に使う半球形のフライパン。高温で広い面積に火が当たり、「鍋気（ウォッキー）」と呼ばれる独特の香りが生まれます。",
                    "zh": "炒中餐用的半球形锅。受热面积大，温度高，能产生独特的'锅气'。炒饭、炒面必备。",
                },
                "tips": {
                    "ko": ["볶음 요리는 재료를 미리 준비해 두고, 팬을 충분히 달군 뒤 빠르게 조리해야 해요.", "가정 가스레인지에서도 웍을 쓸 수 있지만, 바닥이 평평한 웍을 선택하면 더 안정적이에요."],
                    "en": ["Prep all ingredients before starting — stir-frying moves fast.", "A flat-bottom wok is more stable on a home gas stove."],
                    "ja": ["炒め物は食材を全て下準備してから素早く調理します。", "家庭のガスコンロには底が平らな中華鍋の方が安定します。"],
                    "zh": ["炒菜前要备好所有食材，因为炒的过程很快。", "家用燃气灶建议选平底炒锅，更稳定。"],
                },
            },
            {
                "id": "steamer",
                "name": {"ko": "찜기", "en": "Steamer", "ja": "蒸し器", "zh": "蒸锅"},
                "desc": {
                    "ko": "만두, 계란찜, 생선찜 등 수증기로 익히는 조리 도구입니다. 대나무 찜기와 스테인리스 찜기가 있으며, 대나무 찜기는 여분의 수분을 흡수해 음식이 덜 눅눅해집니다.",
                    "en": "Used for dumplings, steamed egg, and fish. Bamboo steamers absorb excess moisture, keeping food less soggy than metal ones.",
                    "ja": "餃子や茶碗蒸し、蒸し魚などに使います。竹製は余分な水分を吸収するため、食材がびしょびしょになりにくいです。",
                    "zh": "用于蒸饺子、蒸蛋、蒸鱼等。竹蒸笼能吸收多余水分，食物不容易变湿烂。",
                },
                "tips": {
                    "ko": ["찜기 바닥에 면포(찜포)를 깔면 음식이 달라붙지 않아요.", "물이 끓고 나서 재료를 올려야 찌는 시간이 정확해요.", "뚜껑을 열 때는 한쪽으로 비스듬히 열어 뜨거운 수증기를 피해요."],
                    "en": ["Line the steamer with cloth to prevent sticking.", "Place food only after the water is boiling for accurate timing.", "Open the lid by tilting it away from you to avoid steam burns."],
                    "ja": ["蒸し布を敷くと食材がくっつきません。", "湯が沸騰してから食材を入れると蒸し時間が正確になります。", "フタを開けるときは蒸気でやけどしないよう斜めに持ち上げましょう。"],
                    "zh": ["垫上蒸布防止食材粘锅。", "水烧开后再放食材，蒸的时间才准确。", "开盖时斜着打开，小心蒸汽烫手。"],
                },
            },
        ],
    },
    {
        "id": "utensils",
        "name": {"ko": "조리 도구", "en": "Cooking Utensils", "ja": "調理道具", "zh": "烹饪工具"},
        "color": "#2980b9",
        "tools": [
            {
                "id": "spatula",
                "name": {"ko": "뒤집개 (스패출러)", "en": "Spatula / Turner", "ja": "フライ返し", "zh": "锅铲"},
                "desc": {
                    "ko": "프라이팬에서 음식을 뒤집거나 옮길 때 사용합니다. 코팅 팬에는 실리콘 또는 나무 뒤집개를, 스테인리스 팬이나 주물팬에는 금속 뒤집개를 사용하세요.",
                    "en": "Used to flip and move food in a pan. Use silicone or wooden spatulas on non-stick pans; metal spatulas on stainless or cast iron.",
                    "ja": "フライパン内で食材をひっくり返したり移動させるときに使います。テフロンには木製かシリコン製、ステンレスや鉄製パンには金属製を使いましょう。",
                    "zh": "用于翻转和移动食材。不粘锅用木铲或硅胶铲，不锈钢或铸铁锅可用金属铲。",
                },
                "tips": {
                    "ko": ["팬케이크나 달걀 프라이를 뒤집을 때는 넓적한 뒤집개를 쓰면 부서지지 않아요.", "음식 아래로 충분히 넣은 뒤 빠르게 뒤집어야 실패하지 않아요."],
                    "en": ["Use a wide spatula for pancakes and fried eggs to keep them intact.", "Slide fully under the food before flipping quickly for best results."],
                    "ja": ["パンケーキや目玉焼きには幅広のフライ返しを使うと崩れません。", "食材の下に十分入れてから素早くひっくり返しましょう。"],
                    "zh": ["翻煎蛋或煎饼时用宽铲，不容易碎。", "铲子要充分插到食材底部，再快速翻面。"],
                },
            },
            {
                "id": "ladle",
                "name": {"ko": "국자", "en": "Ladle", "ja": "おたま", "zh": "汤勺"},
                "desc": {
                    "ko": "국, 찌개, 소스를 떠서 옮기는 도구입니다. 스테인리스 재질이 위생적이고 오래 씁니다. 용량 표시가 있는 국자는 계량할 때도 유용해요.",
                    "en": "Used to scoop and serve soups, stews, and sauces. Stainless steel is hygienic and durable. Ladles with volume markings double as measuring tools.",
                    "ja": "スープや煮汁をすくうときに使います。ステンレス製が衛生的で長持ちします。目盛り付きのものは計量にも便利。",
                    "zh": "用于盛汤、打酱汁的工具。不锈钢材质卫生耐用。带刻度的汤勺还可以用来量取液体。",
                },
                "tips": {
                    "ko": ["국물을 담을 때는 국자를 냄비 가장자리에 대고 기울여 흘리지 않게 해요.", "국자 안쪽에 기름을 살짝 바르면 꿀, 된장 등이 달라붙지 않아요."],
                    "en": ["Rest the ladle on the pot rim while filling to prevent drips.", "Lightly oil the inside of the ladle to keep sticky things like honey or miso from clinging."],
                    "ja": ["注ぐときは鍋のふちに当てると垂れません。", "内側に薄く油を塗るとみそや蜂蜜がくっつきにくくなります。"],
                    "zh": ["盛汤时让汤勺靠着锅边，不容易洒出来。", "汤勺内侧涂一点油，味噌、蜂蜜等黏稠食材就不容易粘了。"],
                },
            },
            {
                "id": "tongs",
                "name": {"ko": "집게", "en": "Tongs", "ja": "トング", "zh": "夹子"},
                "desc": {
                    "ko": "뜨거운 재료를 안전하게 집거나 뒤집을 때 사용합니다. 파스타 서빙, 고기 굽기, 샐러드 버무리기 등 다양하게 활용해요. 끝이 실리콘으로 코팅된 것은 코팅 팬에서도 사용 가능합니다.",
                    "en": "For safely gripping and turning hot food. Used for serving pasta, flipping meat, and tossing salads. Silicone-tipped tongs are safe on non-stick pans.",
                    "ja": "熱い食材を安全につかんだりひっくり返したりするのに使います。シリコン先端のものはテフロンパンでも使えます。",
                    "zh": "安全夹持和翻转热食材的工具，可用于夹意面、翻肉、拌沙拉等。硅胶头的夹子可以在不粘锅上使用。",
                },
                "tips": {
                    "ko": ["고기를 굽다가 집게로 너무 세게 누르면 육즙이 빠져요. 살살 잡으세요.", "집게 끝이 실리콘이면 가스 불꽃에 가깝게 가져가지 않도록 주의하세요."],
                    "en": ["Don't squeeze meat with tongs while cooking — it forces out the juices.", "Keep silicone-tipped tongs away from open flames."],
                    "ja": ["肉を焼くときに強く挟むと肉汁が出てしまいます。やさしく持ちましょう。", "シリコン先端のトングを直火に近づけないよう注意してください。"],
                    "zh": ["夹肉时不要用力挤压，会把肉汁挤出来。", "硅胶头的夹子注意别靠近明火。"],
                },
            },
            {
                "id": "wooden-spoon",
                "name": {"ko": "나무 주걱", "en": "Wooden Spoon", "ja": "木べら", "zh": "木铲"},
                "desc": {
                    "ko": "볶음, 저음, 반죽 섞기에 두루 사용하는 주방의 기본 도구입니다. 열 전달이 낮아 손잡이가 뜨거워지지 않고, 코팅 팬에 상처를 내지 않아요. 단, 냄새와 색이 배어들 수 있어 깨끗이 관리해야 해요.",
                    "en": "A kitchen staple for stirring, sautéing, and mixing dough. Doesn't conduct heat so the handle stays cool, and safe on non-stick pans. Clean well since it can absorb odors.",
                    "ja": "炒め物やかき混ぜ、生地の混合に使う基本道具。熱を伝えにくいので柄が熱くなりにくく、テフロンも傷めません。臭いがつくのでしっかり洗ってください。",
                    "zh": "炒菜、搅拌、和面都能用的基本工具。不导热，柄不会烫手，不划伤不粘锅。但要注意容易吸味，需要好好清洗。",
                },
                "tips": {
                    "ko": ["냄새가 배면 레몬즙이나 베이킹소다로 문질러 씻어요.", "세척 후 완전히 건조해야 곰팡이가 생기지 않아요."],
                    "en": ["If it absorbs odors, scrub with lemon juice or baking soda.", "Dry completely after washing to prevent mold."],
                    "ja": ["臭いがついたらレモン汁や重曹でこすり洗いを。", "洗った後は完全に乾かさないとカビの原因になります。"],
                    "zh": ["如果有异味，用柠檬汁或小苏打擦洗。", "洗后要完全晾干，防止发霉。"],
                },
            },
            {
                "id": "strainer",
                "name": {"ko": "체 (스트레이너)", "en": "Strainer / Sieve", "ja": "ざる・漉し器", "zh": "滤网/筛子"},
                "desc": {
                    "ko": "면이나 채소의 물기를 빼거나, 밀가루를 체 치거나, 소스를 거를 때 사용합니다. 구멍 크기가 다른 여러 종류가 있으며, 고운 체는 크림 수프나 소스를 부드럽게 만드는 데 효과적이에요.",
                    "en": "Used to drain pasta and vegetables, sift flour, and strain sauces. Fine-mesh sieves make cream soups and sauces silky smooth.",
                    "ja": "麺や野菜の水切り、粉のふるい、ソースの裏ごしに使います。目の細かいものはスープやソースをなめらかにするのに効果的です。",
                    "zh": "用于沥干意面和蔬菜的水分、过筛面粉、过滤酱汁。细孔滤网能让奶油汤和酱汁更细腻顺滑。",
                },
                "tips": {
                    "ko": ["밀가루를 체 치면 덩어리가 없어져 빵과 케이크가 더 부드러워져요.", "된장이나 고추장을 체에 풀면 국물이 더 맑아져요."],
                    "en": ["Sifting flour removes lumps and makes bread and cakes lighter.", "Dissolving miso or gochujang through a sieve gives you a cleaner broth."],
                    "ja": ["粉をふるうとダマがなくなり、パンやケーキがより滑らかになります。", "みそや唐辛子味噌を溶くときに漉すと汁が澄みます。"],
                    "zh": ["面粉过筛去掉结块，烤出来的面包和蛋糕更蓬松。", "味噌或辣椒酱通过滤网化开，汤色更清澈。"],
                },
            },
        ],
    },
    {
        "id": "measuring",
        "name": {"ko": "계량 도구", "en": "Measuring Tools", "ja": "計量器具", "zh": "量具"},
        "color": "#8e44ad",
        "tools": [
            {
                "id": "measuring-cups",
                "name": {"ko": "계량컵", "en": "Measuring Cup", "ja": "計量カップ", "zh": "量杯"},
                "desc": {
                    "ko": "액체와 가루 재료를 정확히 측정하는 도구입니다. 1컵(240ml)이 기본 단위이며, 요리 레시피에서 '1컵', '1/2컵' 등으로 표기됩니다. 투명 재질은 눈금을 읽기 쉽고, 전자레인지에도 사용 가능해요.",
                    "en": "Measures liquids and dry ingredients accurately. 1 cup equals 240ml. Transparent cups are easy to read and often microwave-safe.",
                    "ja": "液体や粉末食材を正確に計量するための道具。1カップは240mlが基本。透明なものは目盛りが見やすく電子レンジ対応のものも多いです。",
                    "zh": "精确测量液体和粉末食材的工具。1杯=240ml。透明材质便于读数，很多还可以放微波炉使用。",
                },
                "tips": {
                    "ko": ["가루 재료는 계량컵에 담고 평평한 것(칼 뒷면 등)으로 윗면을 긁어 평평하게 해야 정확해요.", "액체는 컵을 수평면에 놓고 눈높이를 낮춰 눈금을 확인하세요."],
                    "en": ["For dry ingredients, fill the cup and level the top with a flat edge for accuracy.", "Place the cup on a flat surface and read liquid measurements at eye level."],
                    "ja": ["粉類はカップに山盛りにしてからスパチュラなどで平らにならすと正確です。", "液体は水平な場所に置いて目線の高さで目盛りを読みましょう。"],
                    "zh": ["量粉类食材时，装满后用刮刀刮平顶部才准确。", "量液体时把量杯放平，眼睛与刻度平视才准。"],
                },
            },
            {
                "id": "measuring-spoons",
                "name": {"ko": "계량스푼", "en": "Measuring Spoons", "ja": "計量スプーン", "zh": "量勺"},
                "desc": {
                    "ko": "소량의 재료를 정확히 계량하는 스푼 세트입니다. 1큰술(15ml), 1작은술(5ml), 1/2작은술(2.5ml), 1/4작은술(1.25ml) 등으로 구성되어 있어요. 레시피에서 가장 많이 쓰이는 단위입니다.",
                    "en": "A spoon set for measuring small amounts. Typically includes 1 tbsp (15ml), 1 tsp (5ml), 1/2 tsp (2.5ml), and 1/4 tsp (1.25ml). The most-used measurement in recipes.",
                    "ja": "少量の食材を計量するスプーンセット。大さじ15ml、小さじ5ml、小さじ1/2（2.5ml）、小さじ1/4（1.25ml）が一般的。レシピで最もよく使う単位です。",
                    "zh": "量取少量食材的量勺套装，通常包括1大勺(15ml)、1小勺(5ml)、1/2小勺、1/4小勺。是食谱里最常用的单位。",
                },
                "tips": {
                    "ko": ["된장·고추장 같은 된 재료는 꾹 눌러 담아 평평하게 만들어야 정확해요.", "소금·후추 같은 가루는 꾹꾹 누르지 말고 자연스럽게 담아요."],
                    "en": ["Pack thick pastes like miso and gochujang firmly and level the top.", "Spoon loose dry ingredients like salt and pepper without packing."],
                    "ja": ["みそなどの粘度の高いものはしっかり詰めて平らにならします。", "塩・こしょうなどさらさらしたものは押し込まずにすくって入れます。"],
                    "zh": ["味噌、辣椒酱等粘稠食材要压实刮平。", "盐、胡椒等松散调料自然舀入即可，不用压。"],
                },
            },
            {
                "id": "kitchen-scale",
                "name": {"ko": "주방 저울", "en": "Kitchen Scale", "ja": "キッチンスケール", "zh": "厨房秤"},
                "desc": {
                    "ko": "재료를 무게(g, oz)로 정확히 재는 도구입니다. 특히 베이킹에서 필수적이에요. 디지털 저울은 1g 단위까지 측정 가능하며, 영점(tare) 기능이 있어 그릇 무게를 빼고 재료만 잴 수 있어요.",
                    "en": "Weighs ingredients in grams or ounces. Essential for baking. Digital scales measure to 1g precision; the tare function lets you zero out the bowl weight.",
                    "ja": "食材をg・ozで正確に量る道具。特にお菓子作りに欠かせません。デジタルスケールは1g単位まで計測でき、風袋引き（ゼロセット）機能が便利。",
                    "zh": "以克或盎司精确称量食材，烘焙必备。数字厨秤精度可达1g，归零(tare)功能可以扣除容器重量。",
                },
                "tips": {
                    "ko": ["베이킹은 계량컵보다 저울이 훨씬 정확해요. 밀가루 1컵도 담는 방법에 따라 무게가 달라지거든요.", "사용 전 항상 0으로 맞추고, 그릇 올리고 다시 0으로 맞춘 뒤 재료를 담으세요."],
                    "en": ["For baking, scales are far more accurate than cups — a cup of flour varies by how it's packed.", "Always zero first, place the bowl, zero again, then add your ingredient."],
                    "ja": ["お菓子作りでは計量カップより秤の方がずっと正確です。粉は詰め方で重さが変わるからです。", "使う前に必ずゼロに合わせ、器を置いてまたゼロにしてから食材を入れましょう。"],
                    "zh": ["烘焙时用秤比量杯准确得多，因为面粉装法不同重量会有很大差异。", "使用前先归零，放上容器再归零，然后再放食材。"],
                },
            },
            {
                "id": "timer",
                "name": {"ko": "타이머", "en": "Kitchen Timer", "ja": "キッチンタイマー", "zh": "定时器"},
                "desc": {
                    "ko": "조리 시간을 정확히 측정하는 도구입니다. 스마트폰 타이머로도 충분히 대체 가능하지만, 전용 타이머는 요리에 집중할 수 있게 해줘요. 파스타 삶기, 계란 삶기 등 시간이 중요한 요리에서 필수입니다.",
                    "en": "Tracks cooking time accurately. A phone timer works fine, but a dedicated kitchen timer keeps you focused on cooking. Essential for pasta, eggs, and any time-sensitive step.",
                    "ja": "調理時間を正確に管理する道具。スマホでも代用できますが、専用タイマーの方が料理に集中できます。パスタの茹で時間や卵の加熱など時間が重要な料理に欠かせません。",
                    "zh": "精确控制烹饪时间的工具。手机定时器也够用，但专用定时器让你更专注于烹饪。煮意面、煮鸡蛋等对时间敏感的步骤必不可少。",
                },
                "tips": {
                    "ko": ["계란 반숙은 끓는 물에 7분, 완숙은 12분으로 기억하세요.", "파스타는 봉지에 적힌 시간보다 1분 짧게 삶고 팬에서 마저 익히면 훨씬 맛있어요."],
                    "en": ["Soft-boiled egg = 7 minutes, hard-boiled = 12 minutes from boiling water.", "Cook pasta 1 minute less than the package says, then finish in the pan for better results."],
                    "ja": ["半熟卵は沸騰後7分、固ゆでは12分が目安です。", "パスタは袋の表示より1分短く茹でてフライパンで仕上げると美味しくなります。"],
                    "zh": ["溏心蛋水开后煮7分钟，全熟蛋12分钟。", "意面比包装说明少煮1分钟，在锅里收汁收尾，口感更好。"],
                },
            },
        ],
    },
    {
        "id": "prep",
        "name": {"ko": "손질 도구", "en": "Prep Tools", "ja": "下ごしらえ道具", "zh": "备料工具"},
        "color": "#27ae60",
        "tools": [
            {
                "id": "peeler",
                "name": {"ko": "필러 (감자칼)", "en": "Vegetable Peeler", "ja": "ピーラー", "zh": "削皮器"},
                "desc": {
                    "ko": "감자, 당근, 사과 등의 껍질을 얇고 빠르게 벗기는 도구입니다. 칼로 껍질을 벗기면 과육 손실이 많지만, 필러는 껍질만 얇게 제거해요. 앞뒤로 당기는 Y자형과 옆으로 밀어 쓰는 I자형이 있어요.",
                    "en": "Peels potatoes, carrots, and apples quickly with minimal waste. Y-shaped peelers are pulled toward you; I-shaped are pushed sideways. Both work great.",
                    "ja": "じゃがいも・にんじん・りんごなどを素早く薄く皮むきできる道具。カットロスが少ない。Y型（手前に引く）とI型（横に押す）があります。",
                    "zh": "快速削薄土豆、胡萝卜、苹果等皮的工具，损耗少。有Y形（向身体方向拉）和I形（向侧面推）两种。",
                },
                "tips": {
                    "ko": ["감자는 껍질을 벗긴 뒤 물에 담가 두면 갈변하지 않아요.", "당근 껍질은 얇아서 필러로 가볍게 한 번만 밀어도 충분해요."],
                    "en": ["Submerge peeled potatoes in water to prevent browning.", "Carrot skin is thin — one light pass with the peeler is enough."],
                    "ja": ["皮をむいたじゃがいもは水に浸けると変色しません。", "にんじんの皮は薄いので、ピーラーで軽く1回なでるだけで十分です。"],
                    "zh": ["削好皮的土豆泡在水里防止变色。", "胡萝卜皮很薄，削皮器轻轻刮一遍就够了。"],
                },
            },
            {
                "id": "grater",
                "name": {"ko": "강판 (그레이터)", "en": "Grater / Microplane", "ja": "おろし金・グレーター", "zh": "刨丝器/磨泥器"},
                "desc": {
                    "ko": "무·생강·마늘을 갈거나, 치즈·감귤 제스트를 내릴 때 사용합니다. 구멍 크기에 따라 굵게 갈기·채 썰기·곱게 갈기가 가능해요. 마이크로플레인은 치즈·제스트 전용으로 매우 고운 결이 나와요.",
                    "en": "Grates daikon, ginger, and garlic, or zests citrus and shreds cheese. Different hole sizes give coarse, medium, or fine results. A Microplane is ideal for cheese and zesting.",
                    "ja": "大根・しょうが・にんにくをすりおろしたり、チーズや柑橘の皮をおろすのに使います。穴の大きさで粗さを調整できます。マイクロプレインはチーズ・ゼストに最適。",
                    "zh": "用于磨白萝卜泥、姜末、蒜泥，或擦碎奶酪和柑橘皮屑。孔的大小决定磨出来的粗细。Microplane磨奶酪和果皮效果极佳。",
                },
                "tips": {
                    "ko": ["강판 뒷면에 손가락이 닿으면 다칠 수 있어요. 마지막에는 칼로 밀거나 포크로 긁어내세요.", "생강은 냉동 후 갈면 섬유질이 부서져 더 고운 생강즙이 나와요."],
                    "en": ["Keep fingers away from the back edge near the end — use a knife or fork to get the last bits.", "Freeze ginger before grating — the fibers break down for a finer result."],
                    "ja": ["最後に指を近づけると危ないので、フォークや包丁で押し当てましょう。", "しょうがは冷凍してからおろすと繊維が壊れてより細かくなります。"],
                    "zh": ["磨到最后注意别磨到手指，用刀或叉子推着磨。", "生姜冻硬后再磨，纤维更容易断，磨出来更细腻。"],
                },
            },
            {
                "id": "whisk",
                "name": {"ko": "거품기 (위스크)", "en": "Whisk", "ja": "泡立て器", "zh": "打蛋器"},
                "desc": {
                    "ko": "계란을 풀거나, 생크림·머랭을 휘핑하거나, 소스를 유화시킬 때 사용합니다. 손 거품기는 소량의 작업에, 전동 거품기(핸드믹서)는 생크림·머랭 등 대량 휘핑에 효율적이에요.",
                    "en": "Beats eggs, whips cream and meringue, and emulsifies sauces. A hand whisk works for small tasks; an electric hand mixer is better for large-volume whipping.",
                    "ja": "卵を解いたり、生クリームやメレンゲを泡立てたり、ソースを乳化させるときに使います。手動は少量に、電動は大量の泡立てに向いています。",
                    "zh": "用于打散鸡蛋、打发奶油和蛋白霜、乳化酱汁。手动打蛋器适合少量，电动打蛋器适合大量打发。",
                },
                "tips": {
                    "ko": ["카르보나라 소스 만들 때 계란+치즈를 거품기로 잘 섞어 두면 부드럽게 돼요.", "생크림은 차가울수록 잘 휘핑되므로 볼과 거품기를 냉장고에 넣어 식혔다가 쓰세요."],
                    "en": ["Whisk eggs and cheese together thoroughly for smooth carbonara sauce.", "Cold cream whips better — chill the bowl and whisk in the fridge before use."],
                    "ja": ["カルボナーラは卵とチーズをよく混ぜておくとなめらかな仕上がりになります。", "生クリームは冷やした方が泡立ちやすいので、ボウルと泡立て器も冷やしておきましょう。"],
                    "zh": ["做卡波纳拉时把鸡蛋和奶酪充分搅拌，酱汁会更细腻。", "奶油越冷越容易打发，使用前把碗和打蛋器一起放冰箱冷藏。"],
                },
            },
            {
                "id": "mortar",
                "name": {"ko": "절구 (모타&페스틀)", "en": "Mortar & Pestle", "ja": "すり鉢・すりこぎ", "zh": "研钵"},
                "desc": {
                    "ko": "마늘·생강·허브·향신료를 빻아 향을 극대화하는 전통 도구입니다. 믹서기와 달리 재료를 터뜨리며 갈아서 세포벽을 부수기 때문에 향이 훨씬 풍부하게 나와요. 태국 요리(쏨탐)나 이탈리아 페스토에 필수적입니다.",
                    "en": "A traditional tool that crushes garlic, herbs, and spices to maximize flavor. Unlike blenders, it bruises rather than cuts, releasing much more aroma. Essential for Thai papaya salad and Italian pesto.",
                    "ja": "にんにく・ハーブ・香辛料を砕いて香りを最大限に引き出す伝統的な道具。ミキサーと違い、食材を潰すことで細胞壁が壊れ、香りがより豊かに出ます。",
                    "zh": "研磨大蒜、香草、香料以最大程度释放香气的传统工具。与搅拌机不同，研磨是挤压破坏细胞壁，香气释放更充分。泰式木瓜沙拉和意大利青酱必备。",
                },
                "tips": {
                    "ko": ["마늘을 빻을 때 소금을 조금 넣으면 미끄러지지 않아 잘 갈려요.", "향신료는 기름 없이 팬에 살짝 볶은 뒤 빻으면 향이 배가돼요."],
                    "en": ["Add a pinch of salt when grinding garlic — it prevents slipping and helps break it down.", "Lightly toast spices in a dry pan before grinding to intensify their flavor."],
                    "ja": ["にんにくを砕くとき少し塩を加えると滑らず細かくなります。", "スパイスは油なしで軽く炒ってから砕くと香りが増します。"],
                    "zh": ["研磨大蒜时加一点盐，防止滑动，也更容易研碎。", "香料先干锅略炒再研磨，香气会加倍。"],
                },
            },
        ],
    },
    {
        "id": "appliances",
        "name": {"ko": "주방 가전", "en": "Kitchen Appliances", "ja": "キッチン家電", "zh": "厨房电器"},
        "color": "#16a085",
        "tools": [
            {
                "id": "blender",
                "name": {"ko": "믹서기 / 블렌더", "en": "Blender", "ja": "ミキサー・ブレンダー", "zh": "搅拌机/料理机"},
                "desc": {
                    "ko": "수프, 스무디, 소스를 곱게 갈아주는 가전입니다. 일반 믹서기는 통 전체를 갈고, 핸드블렌더(스틱 믹서)는 냄비 안에서 직접 갈 수 있어 뜨거운 수프를 만들 때 편리해요.",
                    "en": "Blends soups, smoothies, and sauces smooth. A standard blender uses a jug; an immersion (stick) blender goes directly into the pot — convenient for hot soups.",
                    "ja": "スープ・スムージー・ソースを滑らかに攪拌する家電。据え置き型は全体を撹拌し、ハンドブレンダーはお鍋の中で直接使えるので熱いスープに便利です。",
                    "zh": "将汤、果昔、酱汁打细腻的家电。台式料理机整体搅拌，手持料理棒可以直接在锅里使用，做热汤很方便。",
                },
                "tips": {
                    "ko": ["뜨거운 수프를 믹서기에 넣을 때는 절반만 채우고 뚜껑을 수건으로 눌러요. 수증기 압력으로 뚜껑이 폭발할 수 있어요.", "핸드블렌더는 날 부분을 재료에 완전히 담근 뒤 작동시켜야 튀지 않아요."],
                    "en": ["Only fill the blender half full with hot liquid, and hold the lid down with a towel — steam pressure can blow the lid off.", "Fully submerge the immersion blender head before turning it on to prevent splashing."],
                    "ja": ["熱い液体をミキサーに入れるときは半分までにして、ふきんでふたを押さえましょう。蒸気圧でふたが吹き飛ぶことがあります。", "ハンドブレンダーはブレード部分を完全に液体に沈めてから動かすと飛び散りません。"],
                    "zh": ["热汤放入料理机时只装一半，用毛巾压住盖子，蒸汽压力可能把盖子顶飞。", "手持料理棒要完全浸入食材后再开机，防止飞溅。"],
                },
            },
            {
                "id": "air-fryer",
                "name": {"ko": "에어프라이어", "en": "Air Fryer", "ja": "エアフライヤー", "zh": "空气炸锅"},
                "desc": {
                    "ko": "뜨거운 공기를 순환시켜 기름 없이 또는 적은 기름으로 바삭하게 조리하는 가전입니다. 냉동식품 데우기, 치킨 구이, 채소 구이, 소량 베이킹에 유용해요. 기름 사용량이 90% 이상 줄어들어요.",
                    "en": "Circulates hot air to cook food crispy with little or no oil. Great for frozen foods, chicken, roasted vegetables, and small-batch baking. Uses 90% less oil than deep-frying.",
                    "ja": "熱風を循環させて油なし（または少量の油）でカリカリに調理する家電。冷凍食品の温め直し・チキン・野菜焼き・少量のお菓子作りに便利。揚げ物に比べて油の使用量が90%以上削減できます。",
                    "zh": "通过循环热风，少油甚至无油也能做出酥脆口感的家电。适合加热冷冻食品、烤鸡、烤蔬菜和少量烘焙。用油量比油炸减少90%以上。",
                },
                "tips": {
                    "ko": ["재료를 넣기 전에 3-5분 예열하면 더 바삭해져요.", "중간에 뒤집어 주면 양면이 고르게 익어요.", "공간을 너무 많이 채우면 공기 순환이 안 돼 바삭하지 않아요. 여유 공간을 두세요."],
                    "en": ["Preheat 3-5 minutes before adding food for better crispiness.", "Flip food halfway through for even browning.", "Don't overcrowd — air needs to circulate. Leave space between pieces."],
                    "ja": ["食材を入れる前に3〜5分予熱するとよりカリカリになります。", "途中でひっくり返すと均一に焼き色がつきます。", "詰め込みすぎると空気が循環せずカリカリになりません。余裕を持って入れましょう。"],
                    "zh": ["放食材前预热3-5分钟，更脆。", "中途翻面，上色更均匀。", "不要放太满，空气要流通。食材之间留有间隙。"],
                },
            },
            {
                "id": "rice-cooker",
                "name": {"ko": "전기밥솥", "en": "Rice Cooker", "ja": "炊飯器", "zh": "电饭锅"},
                "desc": {
                    "ko": "버튼 하나로 완벽한 밥을 짓는 필수 가전입니다. 내솥의 눈금에 맞춰 쌀과 물의 비율을 맞추면 실패 없이 맛있는 밥을 지을 수 있어요. 일반 백미 외에도 잡곡밥, 죽, 찜 모드도 지원하는 제품이 많아요.",
                    "en": "Press a button and get perfect rice every time. Match the water level to the inner pot markings and it's foolproof. Many models also cook mixed grains, porridge, and steam.",
                    "ja": "ボタン一つで完璧なご飯が炊ける必須家電。内釜の目盛りに合わせて水を入れれば失敗知らず。雑穀ご飯・お粥・蒸しモード対応の機種も多いです。",
                    "zh": "按一个键就能煮出完美米饭的必备家电。按内胆刻度加水，不会失败。很多机型还支持杂粮饭、粥、蒸制等功能。",
                },
                "tips": {
                    "ko": ["쌀은 씻은 뒤 30분 이상 불리면 더 찰지고 윤기 있는 밥이 나와요.", "취사 후 뚜껑을 바로 열지 말고 10분 뜸을 들이면 더 맛있어요."],
                    "en": ["Soak washed rice for 30+ minutes before cooking for stickier, glossier results.", "Let rice steam for 10 minutes with the lid closed after the cooker finishes."],
                    "ja": ["洗った米を30分以上浸水させると、より粘りのある艶やかなご飯になります。", "炊き上がり後すぐ蓋を開けず、10分蒸らすと美味しくなります。"],
                    "zh": ["洗米后浸泡30分钟以上，煮出来的米饭更黏更有光泽。", "煮好后不要马上开盖，焖10分钟口感更好。"],
                },
            },
            {
                "id": "oven",
                "name": {"ko": "오븐", "en": "Oven", "ja": "オーブン", "zh": "烤箱"},
                "desc": {
                    "ko": "빵·케이크 굽기, 고기 로스팅, 그라탱 등 다양한 서양 요리에 사용하는 가전입니다. 온도와 시간을 정확히 지키는 것이 베이킹 성공의 핵심이에요. 컨벡션(열풍 순환) 기능이 있으면 더 고르게 익힐 수 있어요.",
                    "en": "Used for baking bread and cakes, roasting meat, and making gratins. Precise temperature and time are key to baking success. Convection mode (fan circulation) ensures more even cooking.",
                    "ja": "パン・ケーキ作り、肉のロースト、グラタンなど西洋料理に使う家電。温度と時間を正確に守ることがお菓子作りの成功の鍵です。コンベクション（熱風循環）機能があればより均一に焼けます。",
                    "zh": "用于烤面包蛋糕、烤肉、做焗烤等西式料理的家电。严格遵守温度和时间是烘焙成功的关键。有热风循环(对流)功能的烤箱加热更均匀。",
                },
                "tips": {
                    "ko": ["오븐은 항상 예열 후 사용하세요. 예열 없이 넣으면 레시피 시간이 맞지 않아요.", "베이킹 중간에 문을 열면 온도가 낮아져 케이크가 주저앉을 수 있어요.", "오븐마다 실제 온도가 다를 수 있으므로 오븐 온도계를 써보는 걸 추천해요."],
                    "en": ["Always preheat the oven — putting food in cold makes recipe times useless.", "Don't open the door mid-bake — temperature drops cause cakes to collapse.", "Every oven runs slightly different; an oven thermometer helps calibrate."],
                    "ja": ["オーブンは必ず予熱してから使いましょう。予熱なしだとレシピの時間が合わなくなります。", "焼き途中でドアを開けると温度が下がりケーキが沈む原因になります。", "オーブンによって実際の温度が異なるため、オーブン用温度計の使用をおすすめします。"],
                    "zh": ["一定要预热烤箱再放食材，不预热的话食谱时间就不准了。", "烘烤中途不要开门，温度下降会导致蛋糕塌陷。", "每台烤箱的实际温度略有不同，建议用烤箱温度计校准。"],
                },
            },
        ],
    },
]

TOOLS_UI = {
    "title": {"ko": "요리 도구 가이드", "en": "Kitchen Tools Guide", "ja": "調理道具ガイド", "zh": "厨房工具指南"},
    "subtitle": {
        "ko": "어떤 도구가 무엇인지, 어떻게 쓰는지 처음부터 알려드려요",
        "en": "What each tool is, what it does, and how to use it right",
        "ja": "道具の名前と使い方を最初から丁寧に解説",
        "zh": "从头了解每种工具是什么、怎么用",
    },
    "tips_label": {"ko": "초보자 팁", "en": "Beginner Tips", "ja": "初心者のコツ", "zh": "新手小贴士"},
}
