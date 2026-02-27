# 各 AI 的提示詞模板
# 根據各 AI 的接受風格做不同格式化

LEVELS = {
    "初學者（剛開始學習）": "初學者",
    "入門（寫過一些小專案）": "入門開發者",
    "中級（有完整專案經驗）": "中級工程師",
    "進階（熟悉架構設計）": "進階工程師",
    "資深（有帶團隊或大型系統經驗）": "資深工程師"
}

CATEGORIES = ["除錯", "功能開發", "程式碼優化", "技術選型", "學習路線", "系統設計", "Code Review", "SAP 開發"]

LANGUAGES = [
    "Python", "JavaScript", "TypeScript", "Go", "Rust",
    "Java", "C#", "C++", "Swift", "Kotlin", "PHP", "Ruby",
    "ABAP", "其他"
]


def build_claude_prompt(level, language, category, task):
    """
    Claude 喜歡有結構、有脈絡的提示詞
    對 XML 標籤分區反應好
    """
    templates = {
        "除錯": f"""<context>
你是一位擅長 {language} 的資深工程師，正在協助一位{level}解決問題。
請根據對方的程度調整說明深度，不要假設太多先備知識。
</context>

<task>
{task}
</task>

<instructions>
1. 先分析最可能的錯誤原因（列出 2~3 個）
2. 針對每個原因提供對應的解法
3. 提供可直接執行的修正後程式碼
4. 說明如何避免這個問題再次發生
</instructions>

<format>
請用繁體中文回答，程式碼部分用英文，說明要清楚易懂。
</format>""",

        "功能開發": f"""<context>
你是一位 {language} 專家，正在指導一位{level}實作新功能。
</context>

<task>
{task}
</task>

<instructions>
1. 先說明整體實作思路
2. 拆分成清楚的步驟
3. 每個步驟提供範例程式碼
4. 說明每段程式碼的用意
5. 提醒常見的錯誤或注意事項
</instructions>

<format>
請用繁體中文說明，程式碼加上適當的註解。
</format>""",

        "程式碼優化": f"""<context>
你是一位注重程式品質的資深 {language} 工程師。
對象是一位{level}，請在優化的同時說明理由。
</context>

<task>
請幫我優化以下程式碼：
{task}
</task>

<instructions>
1. 列出原本程式碼的問題點
2. 提供優化後的完整程式碼
3. 逐一說明每個改動的原因
4. 如果有效能提升，說明提升了多少
</instructions>

<format>
用繁體中文說明，優化前後對比清楚呈現。
</format>""",

        "技術選型": f"""<context>
你是一位有豐富專案經驗的技術顧問，對象是一位{level}。
</context>

<task>
{task}
</task>

<instructions>
1. 列出主要的技術選項（至少 3 個）
2. 針對各選項分析優缺點
3. 根據對象的程度給出具體建議
4. 說明什麼情境下該選哪個
</instructions>

<format>
用表格或條列清楚比較，最後給出明確建議。
</format>""",

        "學習路線": f"""<context>
你是擅長教學的資深工程師，正在幫一位{level}規劃 {language} 的學習路線。
</context>

<task>
{task}
</task>

<instructions>
1. 根據目前程度設計合適的學習階段
2. 每個階段列出具體要學的主題
3. 推薦學習資源（書、課程、文件）
4. 建議練習方式和小專案
5. 給出大概的時間估計
</instructions>

<format>
用階段性的方式呈現，讓人清楚知道現在該做什麼。
</format>""",

        "系統設計": f"""<context>
你是一位有大型系統經驗的架構師，正在協助一位{level}進行系統設計。
</context>

<task>
{task}
</task>

<instructions>
1. 釐清需求和限制條件
2. 說明整體架構設計
3. 解釋各元件的職責和互動方式
4. 討論可能的瓶頸和解決方案
5. 根據對象程度說明可以省略的複雜度
</instructions>

<format>
用繁體中文說明，可以用文字描述架構圖。
</format>""",

        "Code Review": f"""<context>
你是一位嚴謹但友善的資深 {language} 工程師，正在幫一位{level}做 Code Review。
</context>

<task>
請 Review 以下程式碼：
{task}
</task>

<instructions>
1. 先給整體評價（優點和問題）
2. 按嚴重程度分類問題（必改 / 建議改 / 小建議）
3. 每個問題說明原因和修改方式
4. 給出鼓勵和學習方向
</instructions>

<format>
友善但誠實的語氣，讓對方知道如何進步。
</format>""",

        "SAP 開發": f"""<context>
你是一位熟悉 SAP 生態（ABAP、模組、報表、增強、Fiori 等）的資深顧問，正在協助一位{level}進行 SAP 相關開發。
請根據對方程度調整說明深度，必要時說明 SAP 術語與最佳實務。
</context>

<task>
{task}
</task>

<instructions>
1. 釐清需求對應的 SAP 模組或技術（如 MM、SD、FI、ABAP、S/4HANA 等）
2. 說明實作思路與建議的開發方式（報表、增強、自訂程式、ODATA 等）
3. 提供可參考的程式碼或步驟（若為 ABAP 請符合新語法與最佳實務）
4. 提醒權限、傳輸、測試與上線注意事項
</instructions>

<format>
請用繁體中文回答，程式碼與物件名稱用英文，說明清楚易懂。
</format>"""
    }
    return templates.get(category, templates["功能開發"])


def build_chatgpt_prompt(level, language, category, task):
    """
    ChatGPT 對角色扮演設定反應強
    喜歡明確的 step-by-step 指令
    """
    templates = {
        "除錯": f"""你是一位擅長 {language} 的資深工程師，現在要幫助一位{level}除錯。

請按照以下步驟回答：
Step 1：分析問題，列出最可能的 2~3 個原因
Step 2：針對每個原因給出具體解法
Step 3：提供修正後的完整程式碼
Step 4：說明怎麼避免這個問題再次發生

問題描述：
{task}

請用繁體中文回答，說明要清楚，適合{level}的理解程度。""",

        "功能開發": f"""你是一位 {language} 專家，你的任務是指導一位{level}實作新功能。

請按照以下步驟回答：
Step 1：說明整體思路和架構
Step 2：把實作拆分成清楚的小步驟
Step 3：每個步驟提供範例程式碼
Step 4：解釋每段程式碼在做什麼
Step 5：列出常見錯誤和注意事項

需求：
{task}

請用繁體中文說明，程式碼加上中文註解。""",

        "程式碼優化": f"""你是一位注重程式品質的資深 {language} 工程師。

請幫我優化以下程式碼，並按照步驟說明：
Step 1：指出原始碼的問題（可讀性、效能、安全性等）
Step 2：提供優化後的完整程式碼
Step 3：逐一說明每個修改的原因
Step 4：如果有效能提升，量化說明

程式碼：
{task}

對象是{level}，說明請適合他的程度。""",

        "技術選型": f"""你是一位經驗豐富的技術顧問，請幫一位{level}做技術選型分析。

請按照以下格式回答：
1. 列出主要選項（至少 3 個）
2. 用表格比較各選項的優缺點
3. 根據不同情境給出建議
4. 給出你最終的具體推薦和理由

問題：
{task}

請用繁體中文，結論要明確不要模糊帶過。""",

        "學習路線": f"""你是一位擅長教學的資深工程師，請幫一位{level}規劃 {language} 學習路線。

請提供：
1. 學習階段規劃（分成 3~4 個階段）
2. 每個階段的具體學習目標和主題
3. 推薦的學習資源（書籍、課程、官方文件）
4. 適合練手的小專案建議
5. 每個階段的預估時間

需求：
{task}

用繁體中文回答，路線要清楚實際，不要太理論。""",

        "系統設計": f"""你是一位資深系統架構師，請幫一位{level}進行系統設計。

請按照以下架構回答：
1. 需求分析（功能需求 vs 非功能需求）
2. 整體架構設計
3. 各元件說明和職責
4. 資料流和元件互動方式
5. 可能的瓶頸和解決方案

設計需求：
{task}

請用繁體中文，根據{level}的程度調整細節深度。""",

        "Code Review": f"""你是一位資深 {language} 工程師，請幫一位{level}做 Code Review。

請按照以下格式回覆：
【整體評價】給個簡短的整體評價

【必須修改】嚴重問題，影響功能或安全性
【建議修改】中等問題，影響可維護性或效能
【小建議】風格或習慣性建議

【修改後的程式碼】提供改善後的版本

程式碼：
{task}

語氣請友善，幫助對方學習而不是批評。""",

        "SAP 開發": f"""你是一位熟悉 SAP（ABAP、各模組、報表、增強、Fiori）的資深顧問，請幫一位{level}完成 SAP 相關開發。

請按照以下步驟回答：
Step 1：確認需求對應的 SAP 模組或技術（MM、SD、FI、ABAP、S/4HANA 等）
Step 2：說明建議的實作方式（報表、增強、自訂程式、ODATA 等）與整體步驟
Step 3：提供可用的程式碼或操作步驟（ABAP 請符合新語法與最佳實務）
Step 4：列出權限、傳輸、測試與上線的注意事項

需求描述：
{task}

請用繁體中文說明，程式碼與物件名稱用英文，適合{level}的理解程度。"""
    }
    return templates.get(category, templates["功能開發"])


def build_gemini_prompt(level, language, category, task):
    """
    Gemini 喜歡簡潔直接的指令
    太長反而容易跑偏
    """
    templates = {
        "除錯": f"""角色：{language} 資深工程師
對象：{level}
任務：除錯並修正

問題：{task}

請提供：
- 原因分析（2~3 點）
- 修正後的程式碼
- 預防建議

語言：繁體中文""",

        "功能開發": f"""角色：{language} 開發專家
對象：{level}
任務：實作功能

需求：{task}

請提供：
- 實作步驟
- 範例程式碼（附中文說明）
- 注意事項

語言：繁體中文""",

        "程式碼優化": f"""角色：{language} 資深工程師
對象：{level}
任務：優化程式碼

原始碼：{task}

請提供：
- 問題列表
- 優化後程式碼
- 改動說明

語言：繁體中文""",

        "技術選型": f"""角色：技術顧問
對象：{level}
任務：技術選型建議

問題：{task}

請提供：
- 選項比較表
- 各情境建議
- 最終推薦

語言：繁體中文，結論要明確""",

        "學習路線": f"""角色：資深工程師教練
對象：{level}
技術：{language}

需求：{task}

請提供：
- 分階段學習計畫
- 推薦資源
- 練習專案建議

語言：繁體中文，要實際可執行""",

        "系統設計": f"""角色：系統架構師
對象：{level}
任務：系統設計

需求：{task}

請提供：
- 架構概覽
- 元件說明
- 技術選擇理由

語言：繁體中文，簡潔清楚""",

        "Code Review": f"""角色：{language} 資深工程師
對象：{level}
任務：Code Review

程式碼：{task}

請提供：
- 問題分類（嚴重 / 建議 / 小建議）
- 修改後的程式碼
- 學習建議

語言：繁體中文，語氣友善""",

        "SAP 開發": f"""角色：SAP 資深顧問（ABAP、模組、報表、增強、Fiori）
對象：{level}
任務：SAP 相關開發

需求：{task}

請提供：
- 對應模組/技術與實作方式
- 步驟或範例程式碼（ABAP 符合新語法）
- 權限與傳輸注意事項

語言：繁體中文，程式與物件名稱用英文"""
    }
    return templates.get(category, templates["功能開發"])


def build_grok_prompt(level, language, category, task):
    """
    Grok 喜歡直接、有觀點、對話感強的提示詞
    """
    templates = {
        "除錯": f"""我是一位 {language} 的{level}，碰到一個 bug 需要你幫我搞定。

{task}

直接告訴我：
1. 這個 bug 最可能是什麼原因造成的？
2. 怎麼修？給我可以直接貼上去跑的程式碼
3. 我以後怎麼避免踩同樣的坑？

用繁體中文回答，不要廢話，直接給解法。""",

        "功能開發": f"""我是 {language} 的{level}，想做一個功能需要你幫我。

{task}

給我：
- 怎麼做的思路（簡單說就好）
- 可以跑的範例程式碼
- 有什麼要注意的地方

直接講重點，繁體中文，程式碼加上簡單說明。""",

        "程式碼優化": f"""我是 {language} 的{level}，這段程式碼想讓你幫我變更好。

{task}

告訴我：
- 這段程式碼有什麼問題？
- 優化後長什麼樣？
- 你改了什麼、為什麼這樣比較好？

直接給優化後的版本，繁體中文說明。""",

        "技術選型": f"""我是{level}，在做技術選型需要你給個明確的意見。

{task}

不要給我「各有優缺點，看情況」這種廢話，直接告訴我：
- 主要選項有哪些？
- 各自的優缺點是什麼？
- 你覺得我應該選哪個、為什麼？

繁體中文，要有明確立場。""",

        "學習路線": f"""我是 {language} 的{level}，想要一個實際可以執行的學習計畫。

{task}

給我：
- 分階段的學習計畫（不要太理論）
- 具體要學什麼、用什麼資源
- 可以練手的專案建議

繁體中文，實際一點，不要給我一堆我看完還是不知道從哪裡開始的建議。""",

        "系統設計": f"""我是{level}，需要你幫我想系統設計。

{task}

給我：
- 整體架構怎麼搭
- 各個元件負責什麼
- 有什麼潛在問題要注意

繁體中文，根據我的程度說就好，不需要過度複雜。""",

        "Code Review": f"""我是 {language} 的{level}，想請你幫我 review 這段程式碼。

{task}

直接告訴我：
- 這段程式碼有什麼問題？（分嚴重度）
- 怎麼改？給我改好的版本
- 我需要注意哪些編程習慣？

繁體中文，說實話，我需要真正有幫助的回饋。""",

        "SAP 開發": f"""我是做 SAP 的{level}，需要你幫我搞定一個開發需求。

{task}

直接給我：
- 這需求大概對應哪個模組/技術，用什麼方式做比較好（報表、增強、自訂程式等）
- 可以參考的步驟或 ABAP 程式碼（新語法、最佳實務）
- 權限、傳輸、測試要注意什麼

繁體中文，程式碼和物件名稱用英文，講重點、可執行。"""
    }
    return templates.get(category, templates["功能開發"])


def generate_all_prompts(level, language, category, task):
    level_label = LEVELS.get(level, level)
    return {
        "Claude": build_claude_prompt(level_label, language, category, task),
        "ChatGPT": build_chatgpt_prompt(level_label, language, category, task),
        "Gemini": build_gemini_prompt(level_label, language, category, task),
        "Grok": build_grok_prompt(level_label, language, category, task),
    }
