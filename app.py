import streamlit as st
from templates import LEVELS, CATEGORIES, LANGUAGES, generate_all_prompts

# ── 頁面設定 ──────────────────────────────────────────────
st.set_page_config(
    page_title="工程師 AI 提示詞產生器",
    page_icon="🧑‍💻",
    layout="wide"
)

# ── CSS 樣式 ──────────────────────────────────────────────
st.markdown("""
<style>
    .main-title {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #888;
        margin-bottom: 2rem;
    }
    .ai-label {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .tip-box {
        background-color: #1e1e2e;
        border-left: 4px solid #7c7cff;
        padding: 0.8rem 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
        font-size: 0.85rem;
        color: #ccc;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ── 標題 ──────────────────────────────────────────────────
st.markdown('<div class="main-title">🧑‍💻 工程師 AI 提示詞產生器</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">根據你的程度和需求，自動產生適合各個 AI 的提示詞</div>', unsafe_allow_html=True)

# ── 輸入區塊 ──────────────────────────────────────────────
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        level = st.selectbox(
            "🎯 你的開發程度",
            list(LEVELS.keys()),
            index=2,
            help="程式會根據程度調整提示詞的說明深度"
        )

    with col2:
        language = st.selectbox(
            "💻 主要語言 / 技術",
            LANGUAGES,
            index=0,
            help="選擇你主要使用的程式語言"
        )

    with col3:
        category = st.selectbox(
            "📂 問題類型",
            CATEGORIES,
            index=0,
            help="選擇你的需求屬於哪個類型"
        )

st.markdown("---")

task = st.text_area(
    "📝 描述你的需求或問題",
    placeholder="例如：我在用 Python 寫一個 FastAPI 的登入功能，但一直收到 422 錯誤，我的 request body 格式看起來是對的...",
    height=140
)

# ── 產生按鈕 ──────────────────────────────────────────────
generate = st.button("🚀 產生提示詞", use_container_width=True, type="primary")

# ── 輸出區塊 ──────────────────────────────────────────────
if generate:
    if not task.strip():
        st.warning("⚠️ 請先描述你的需求或問題！")
    else:
        prompts = generate_all_prompts(level, language, category, task)

        st.markdown("---")
        st.markdown("### ✅ 你的提示詞已產生，點選對應的 AI 分頁複製使用")

        # AI 風格說明
        AI_TIPS = {
            "Claude": "喜歡有結構的 XML 標籤格式，給越多背景資訊效果越好",
            "ChatGPT": "對角色設定和 step-by-step 指令反應強",
            "Gemini": "喜歡簡潔直接，重點一目了然",
            "Grok": "對話感強，直接有觀點的提示詞效果最好",
        }

        tabs = st.tabs(list(prompts.keys()))

        for tab, (ai_name, prompt_text) in zip(tabs, prompts.items()):
            with tab:
                st.markdown(
                    f'<div class="tip-box">💡 <strong>{ai_name} 小提示：</strong>{AI_TIPS[ai_name]}</div>',
                    unsafe_allow_html=True
                )
                st.code(prompt_text, language=None)

# ── 使用說明（底部） ─────────────────────────────────────
with st.expander("❓ 怎麼使用這個工具？"):
    st.markdown("""
1. **選擇你的程度**：誠實選擇，程度影響提示詞的說明深度
2. **選擇語言和類型**：盡量選對應的類型，產出效果會更好
3. **描述需求**：越具體越好，把你遇到的情況、錯誤訊息都寫進去
4. **點選產生**：程式會自動產出四個 AI 版本的提示詞
5. **複製貼上**：點右上角的複製按鈕，直接貼到對應的 AI 就能用

**為什麼不同 AI 有不同版本？**
每個 AI 對提示詞的「口味」稍微不同，針對性地格式化可以讓回答品質更好。
""")
