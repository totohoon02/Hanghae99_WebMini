from flask import Flask, render_template, request, redirect, url_for, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dp import 

bp = Blueprint('home', __name__, url_prefix="/")



app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'database.db')


db = SQLAlchemy(app)

@bp.route("/")
def music():
    return render_template('home.html')

@bp.route("/login", methods=['POST'])
def whenlogin():
    if request.method == 'POST':
        username = request.form.get('username')  # 폼에서 'username' 필드를 가져옴
        password = request.form.get('password')  # 폼에서 'password' 필드를 가져옴
        user = User.query.filter_by(username=username, password=password).first()

        userInfo = User.query.all()
        if user:
            return redirect(url_for('home.music'))
        else:
            return render_template('homelogin.html', error="아이디가 틀리거나 비밀번호가 틀림")

    return render_template('homelogin.html')


@bp.route("/board", methods=['POST'])
def submitwish():
    jsonData = request.get_json()
    userId = jsonData.get('user_id')
    contents = jsonData.get('contents')
    
    newBoard = notice_board_list(user_id = userId, contents = contents)
    db.session.add(newBoard)
    db.session.commit()
    
    print(userId)
    print(contents)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)