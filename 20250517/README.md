# Flaskページ遷移サンプルアプリケーション

シンプルなFlaskアプリケーションで、複数ページ間の遷移を実装したサンプルプロジェクトです。

## 機能

- **TOPページ (`/`)**: 現在の日本時間を表示
- **メモページ (`/memo`)**: サンプルメモの一覧を表示
- **プロフィールページ (`/profile`)**: サンプルのプロフィール情報を表示

## インストール方法

1. リポジトリをクローンまたはダウンロード
2. 必要なパッケージをインストール
```
pip install -r requirements.txt
```

## 実行方法

```
python app.py
```

ブラウザで `http://127.0.0.1:5000/` にアクセスして利用できます。

## 技術スタック

- Python 3
- Flask
- HTML/CSS
- Jinja2テンプレートエンジン 