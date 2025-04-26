#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from datetime import datetime
import pytz

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

@app.route('/us')
def us():
    """
    アクセスした際にアメリカの時刻を表示するページを返す関数
    """
    # アメリカの現在時刻を取得
    us_time = datetime.now(pytz.timezone('US/Central'))
    us_time_str = us_time.strftime('%Y年%m月%d日 %H:%M:%S')
    
    # テンプレートにアメリカの時刻を渡してレンダリング
    return render_template('index.html', current_time=us_time_str)

@app.route('/ch')
def ch():
    """
    アクセスした際に中国の時刻を表示するページを返す関数
    """
    # 中国の現在時刻を取得
    ch_time = datetime.now(pytz.timezone('Asia/Shanghai'))
    ch_time_str = ch_time.strftime('%Y年%m月%d日 %H:%M:%S')
    
    # テンプレートに中国の時刻を渡してレンダリング
    return render_template('index.html', current_time=ch_time_str)

@app.route('/diff')
def diff():
    """
    アクセスした際に日本とアメリカの時刻を両方表示するページを返す関数
    """
    # 日本の現在時刻を取得
    jp_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    jp_time_str = jp_time.strftime('%Y年%m月%d日 %H:%M:%S')
    
    # アメリカの現在時刻を取得
    us_time = datetime.now(pytz.timezone('US/Central'))
    us_time_str = us_time.strftime('%Y年%m月%d日 %H:%M:%S')
    
    # テンプレートに日本とアメリカの時刻を渡してレンダリング
    return render_template('diff.html', current_time=jp_time_str, us_time=us_time_str)

if __name__ == '__main__':
    # デバッグモードでアプリケーションを実行
    app.run(debug=True)
