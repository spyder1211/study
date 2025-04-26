#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify

# Flaskアプリケーションの初期化
app = Flask(__name__)

@app.route('/')
def index():
    """
    TODOアプリのメインページを返す関数
    """
    return render_template('todo.html')

@app.route('/time')
def time():
    """
    現在時刻を表示するページを返す関数
    """
    return render_template('time.html')

@app.route('/todo2')
def todo2():
    """
    時間指定可能なTODOアプリのページを返す関数
    """
    return render_template('todo2.html')

if __name__ == '__main__':
    # デバッグモードでアプリケーションを実行
    app.run(debug=True)
