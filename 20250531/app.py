from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-for-middle-school-students'

# データファイルのパス
DATA_DIR = 'data'
DATA_FILE = os.path.join(DATA_DIR, 'messages.json')

def init_data_file():
    """データファイルとディレクトリを初期化"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    if not os.path.exists(DATA_FILE):
        initial_data = {
            "messages": [],
            "total_count": 0
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)

def load_messages():
    """JSONファイルからメッセージを読み込み"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        init_data_file()
        return {"messages": [], "total_count": 0}

def save_message(name, message):
    """新しいメッセージをJSONファイルに保存"""
    try:
        data = load_messages()
        
        new_message = {
            "id": data["total_count"] + 1,
            "name": name,
            "message": message,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "method": "POST"
        }
        
        data["messages"].append(new_message)
        data["total_count"] += 1
        
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

@app.route('/')
def index():
    """ホームページ - メッセージ一覧と投稿フォーム（GET）"""
    data = load_messages()
    return render_template('index.html', 
                         messages=data["messages"], 
                         total_count=data["total_count"])

@app.route('/post_message', methods=['POST'])
def post_message():
    """メッセージ投稿処理（POST）"""
    name = request.form.get('name', '').strip()
    message = request.form.get('message', '').strip()
    
    if not name or not message:
        flash('名前とメッセージの両方を入力してください！', 'error')
        return redirect(url_for('index'))
    
    if save_message(name, message):
        flash(f'メッセージが正常に保存されました！（POSTメソッドで送信）', 'success')
    else:
        flash('メッセージの保存に失敗しました。', 'error')
    
    return redirect(url_for('index'))

@app.route('/explanation')
def explanation():
    """GETとPOSTの説明ページ（GET）"""
    return render_template('explanation.html')

@app.route('/data_view')
def data_view():
    """JSONファイルの中身を表示（GET）"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            json_content = f.read()
        
        data = load_messages()
        return render_template('data_view.html', 
                             json_content=json_content,
                             total_count=data["total_count"])
    except FileNotFoundError:
        init_data_file()
        return redirect(url_for('data_view'))

@app.route('/search')
def search():
    """検索機能の例（GETパラメータ）"""
    query = request.args.get('q', '')
    data = load_messages()
    
    if query:
        filtered_messages = [
            msg for msg in data["messages"] 
            if query.lower() in msg["message"].lower() or query.lower() in msg["name"].lower()
        ]
    else:
        filtered_messages = data["messages"]
    
    return render_template('index.html', 
                         messages=filtered_messages, 
                         total_count=len(filtered_messages),
                         search_query=query)

if __name__ == '__main__':
    init_data_file()
    app.run(debug=True, host='0.0.0.0', port=5001) 