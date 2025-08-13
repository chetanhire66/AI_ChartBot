from flask import Flask, render_template, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Chatbot import gimini
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SQL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    ans = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    data = SQL.query.all()
    return render_template('home.html', data=data)

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    ans = gimini(question)
    new_data = SQL(question=question, ans=ans)
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"question": question, "answer": ans})

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

