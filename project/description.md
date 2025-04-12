---
marp: true
theme: default
paginate: true
---

# 時刻表示ウェブアプリケーション
## Flaskで構築したシンプルな現在時刻表示アプリ

---

# プロジェクト概要

- **目的**: 現在時刻をウェブブラウザで表示する
- **技術**: Python/Flask、Jinja2、HTML/CSS
- **特徴**: シンプルな実装、レスポンシブデザイン

---

# 技術スタック

- **バックエンド**: Python 3 + Flask フレームワーク
- **テンプレートエンジン**: Jinja2
- **フロントエンド**: HTML5 + CSS3
- **コンテンツ**: サーバー側で取得した現在時刻

---

# プロジェクト構成

```text
project/
├── app.py                # メインアプリケーション
├── static/
│   └── css/
│       └── style.css     # スタイルシート
└── templates/
    └── index.html        # HTMLテンプレート
```

---

# ファイル詳細: app.py

```python
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
```

- Flaskアプリの初期化
- 現在時刻の取得と書式設定
- テンプレートへのデータ受け渡し

---

# ファイル詳細: index.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>現在時刻表示アプリ</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>現在の時刻</h1>
        <div class="time-display">{{ current_time }}</div>
        <p class="description">このアプリはPython+Flaskで構築されています</p>
    </div>
</body>
</html>
```

- Jinja2テンプレート構文の使用
- 現在時刻の表示
- CSSファイルのリンク

---

# ファイル詳細: style.css

```css
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #f5f7fa;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.time-display {
    font-size: 2.2rem;
    font-weight: bold;
    color: #2c3e50;
    background-color: #ecf0f1;
    border-radius: 8px;
}
```

- レスポンシブデザイン
- モダンで見やすいUI
- 時刻表示の強調スタイリング

---

# 処理フロー

1. ユーザーがブラウザでアプリにアクセス
2. Flaskアプリがリクエストを受信
3. `app.py`内の`index()`関数が実行される
4. Pythonが現在時刻を取得
5. 取得した時刻データをテンプレートに渡す
6. テンプレートエンジンがHTMLをレンダリング
7. スタイルシートが適用される
8. レスポンスがブラウザに返される
9. ユーザーに時刻が表示される

---

# アプリ実行方法

```bash
# 必要なライブラリのインストール
pip install flask

# アプリケーションの起動
python app.py

# ブラウザでアクセス
# http://127.0.0.1:5000/
```

---

# まとめ

- **シンプルながら機能的**: 必要最小限のコードで時刻表示機能を実現
- **MVCパターン**: Model(データ処理)、View(テンプレート)、Controller(ルーティング)の分離
- **拡張性**: 追加機能の実装が容易（日付形式変更、複数タイムゾーン対応など）
- **学習教材**: Webアプリケーション開発の基礎を学ぶのに最適なサンプル

---

# ご清聴ありがとうございました
## 質問・フィードバックをお待ちしています