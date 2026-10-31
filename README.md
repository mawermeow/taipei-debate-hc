# 台北辯論觀測室

以 ETtoday 台北市長候選人辯論逐字稿及兩套 Minerva HC 社群資料庫，探索沈伯洋與蔣萬安的論證行為。

純 HTML、CSS、JavaScript，沒有 npm 套件、後端、API 金鑰或 Sites 託管依賴。網站入口位於專案根目錄，能部署於 GitHub Pages 的 `https://<帳號>.github.io/<儲存庫>/` 子路徑，也支援自訂網域。

## 推上 GitHub 並展示

1. 在 GitHub 建立空的儲存庫。使用 GitHub Free 時請選擇 Public。
2. 在本專案根目錄提交並推送；將下方 URL 換成你的儲存庫網址：

   ```sh
   git add .
   git commit -m "Prepare debate observatory for GitHub Pages"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   git push -u origin main
   ```

3. 開啟儲存庫 **Settings → Pages → Build and deployment → Source**，選擇 **GitHub Actions**。
4. 到 **Actions → Deploy GitHub Pages → Run workflow** 手動執行一次；之後每次推送到 `main` 都會自動更新網站。
5. 部署完成後，從 **Settings → Pages** 或 Actions 的 **github-pages** environment 取得展示網址。

若已設定 `origin`，省略 `git remote add origin`。若你重新下載專案且沒有 `.git`，先執行 `git init -b main`。此流程不需要建立 `gh-pages` 分支，也不用設定任何自訂 secret。

GitHub 官方說明：[Pages 發布來源](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)、[自訂部署流程](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)。

### 也可以直接從根目錄發布

不使用 Actions 時，可在 **Settings → Pages** 選擇 **Deploy from a branch → main → / (root)**。根目錄已有 `index.html` 與 `.nojekyll`，不需要 Jekyll。這兩種部署方式擇一即可。

## 本機預覽

在專案根目錄執行：

```sh
python3 -m http.server 4173
```

瀏覽 <http://localhost:4173/>。請經 HTTP 載入，直接雙擊 `index.html` 的 `file://` 路徑可能無法讀取 JSON。

要預覽與 Actions 完全相同的發布內容：

```sh
python3 scripts/build_pages.py
python3 -m http.server 4173 --directory _site
```

網站資源與 JSON 使用相對路徑，因此不需設定儲存庫名稱或 base URL。字型使用 Google Fonts，連線無法取得時會使用系統備用字型。

## 專案結構

```text
.
├── index.html                 # 一頁式網站、判準與來源
├── app.js                     # 比較、權重、趨勢、篩選與下載
├── style.css                  # 響應式版面
├── data.json                  # 40 次發言編碼；20 次回答具有品質分數
├── provenance.json            # 來源、擷取日期與原始 HTML 雜湊
├── .nojekyll                  # 直接發布靜態檔案
├── .github/workflows/pages.yml # GitHub Pages 自動部署
└── scripts/build_pages.py     # 產生僅含公開網站檔案的 _site/
```

`_site/` 是產生的部署目錄，不提交。舊的 `sites/` 是保留在本機的 Sites 工作副本，已由 `.gitignore` 排除。之後請編輯根目錄檔案；GitHub Pages 流程不會讀取舊副本，也不會更新原有的 Sites 網址。

## 分析範圍與限制

單次 AI 質性判讀，並非 Minerva 官方評鑑，未經獨立多位編碼者檢驗。所有彙整數字由逐筆資料計算；互動分類來自品質中的切題分，不是獨立測量。攻擊類別允許重疊。候選人提出的數字與指控尚未完成外部事實查核。

原文全文未重刊。資料保留來源頁 `ARCHIVE_ROWS` 的零起算列號、候選人、角色與議題；T01–T40 為本站實質發言順序編號。完整來源與判準可在網站底部展開檢視。

- [ETtoday 逐字稿](https://features.ettoday.net/taipei-debate-2026/)
- [tingtmu/minerva-hc-skills](https://github.com/tingtmu/minerva-hc-skills)
- [charlesjr0719dev/mnv-thinking-skill](https://github.com/charlesjr0719dev/mnv-thinking-skill)
