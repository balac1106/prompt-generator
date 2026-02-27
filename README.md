# 🧑‍💻 工程師 AI 提示詞產生器

根據你的程度和需求，自動產生適合 Claude、ChatGPT、Gemini、Grok 的提示詞。

## 功能

- 根據工程師程度（初學者～資深）調整提示詞深度
- 支援多種程式語言
- 支援 8 種問題類型：除錯、功能開發、程式碼優化、技術選型、學習路線、系統設計、Code Review、SAP 開發
- 針對各 AI 的接受風格輸出不同格式版本
- 不需要 API，直接複製貼上使用

## 快速開始

### 本地端執行

```bash
# 安裝依賴
pip install -r requirements.txt

# 啟動
streamlit run app.py
```

打開瀏覽器進入 `http://localhost:8501` 即可使用。

## 部署到 Streamlit Cloud（免費）

1. Fork 這個 repo 到你的 GitHub
2. 前往 [streamlit.io/cloud](https://streamlit.io/cloud) 登入
3. 點選 "New app"，選擇你的 repo
4. Main file path 填入 `app.py`
5. 點 Deploy，完成！

## 各 AI 提示詞風格說明

| AI | 風格特色 |
|---|---|
| Claude | XML 標籤結構，適合複雜任務，給越多背景越好 |
| ChatGPT | 角色設定 + step-by-step，指令明確 |
| Gemini | 簡潔直接，重點條列 |
| Grok | 對話感，直接有觀點 |

## 問題類型

- **除錯**：找出並修正 bug
- **功能開發**：實作新功能
- **程式碼優化**：改善現有程式碼品質
- **技術選型**：比較技術方案
- **學習路線**：規劃學習計畫
- **系統設計**：架構設計討論
- **Code Review**：程式碼審查
- **SAP 開發**：SAP/ABAP 報表、增強、模組、Fiori 等相關開發

語言選項包含 **ABAP**，可搭配「SAP 開發」類型產生 SAP 專用提示詞。

## License

MIT
