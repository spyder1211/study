from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def top():
    # 日本時間を取得
    japan_tz = pytz.timezone('Asia/Tokyo')
    current_time = datetime.now(japan_tz).strftime('%Y年%m月%d日 %H時%M分%S秒')
    return render_template('top.html', current_time=current_time)

@app.route('/memo')
def memo():
    # サンプルメモを作成
    sample_memos = [
        {"title": "買い物リスト", "content": "牛乳、卵、パン、野菜"},
        {"title": "会議の予定", "content": "5月20日 14:00から営業会議"},
        {"title": "ToDo", "content": "レポート提出、プレゼン資料作成、同僚に連絡"}
    ]
    return render_template('memo.html', memos=sample_memos)

@app.route('/profile')
def profile():
    # サンプルプロフィール情報
    profile_info = {
        "name": "山田太郎",
        "age": 30,
        "occupation": "ウェブデベロッパー",
        "skills": ["Python", "JavaScript", "HTML/CSS", "Flask", "Django"],
        "hobbies": ["読書", "旅行", "写真撮影"]
    }
    return render_template('profile.html', profile=profile_info)

if __name__ == '__main__':
    app.run(debug=True) 