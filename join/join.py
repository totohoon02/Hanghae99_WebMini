"""
회원 가입 기능
1. 입력창에 아이디 입력하고 아이디 중복확인 버튼 누르면 여기로 넘어와서 맞으면 아이디 중복확인 옆에 사용가능한 아이디 입니다
2. 아니면 중복된 아이디 입니다 
3. 비밀번호 확인 맞으면 맞ㅅ급니다 이나면 틀리빈다 
이거 다 맞으면 버튼 이 넘어가고  디비에 저장 post로

"""
from flask import Flask, render_template, request, abort, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')


db = SQLAlchemy(app)

current_utc_time = datetime.utcnow()


@app.route('/')
def home():
	return render_template("join.html")


@app.route('/check', methods=['POST'])
def check():
    id = request.form.get("id")
    user_in_db = User.query.filter_by(username=id).first()
    if user_in_db:
        abort(404)
    else:
        return {"msg":"중복없음"}
    
@app.route('/home')
def ss():
	return render_template("home.html")

@app.route("/signup", methods=['POST'])
def music():
    id = request.form.get("id")
    pw = request.form.get("password")
    user= User(username = id, password = pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "가입완료!"})

  
       

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    frinedlist = db.Column(db.String, nullable=True)
   

    




with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True, port=8000)