# シンプルTODOアプリ

ブラウザのLocalStorageを利用したシンプルなTODOアプリケーションです。
Python（Flask）でサーバーを構築し、フロントエンドはJavaScriptで実装しています。

## 機能

- TODOタスクの追加
- タスクの完了/未完了の切り替え
- タスクの削除
- ブラウザのLocalStorageによるデータ保存

## 実行方法

1. 必要なパッケージのインストール
   ```
   pip install flask
   ```

2. アプリケーションの起動
   ```
   cd 20250426
   python app.py
   ```

3. ブラウザでアクセス
   ```
   http://127.0.0.1:5000/
   ```

## 学習ポイント

- Flask（Pythonフレームワーク）の基本的な使い方
- ブラウザのLocalStorageの活用方法
- JavaScriptによるDOM操作
- イベント処理（イベント委任パターン） 