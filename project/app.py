#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from datetime import datetime

# Flaskアプリケーションの初期化
app = Flask(__name__)

@app.route('/')
def index():
    """
    ルートURLにアクセスした際に現在時刻を表示するページを返す関数
    """
    # 現在時刻を取得
    current_time = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
    
    # テンプレートに現在時刻を渡してレンダリング
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    # デバッグモードでアプリケーションを実行
    app.run(debug=True)
