from flask import Flask, render_template, request, redirect, url_for, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, notice_board_list, User

bp = Blueprint('home', __name__, url_prefix="/")

@bp.route("/",methods=["GET"])
def home():
    input_keyword = request.args.get('query')

    if input_keyword:
        notice_list = notice_board_list.query.filter(
            (notice_board_list.contents.like(f"%{input_keyword}%")) |
            (notice_board_list.username.like(f"%{input_keyword}%"))
        ).all()
    else:
        notice_list = notice_board_list.query.all()

    print("아래와 같음")
    print(notice_list)
    
    return render_template('home.html', data=notice_list)

@bp.route("/board", methods=['POST'])
def submitwish():
    jsonData = request.get_json()
    userId = jsonData.get('user_id')
    contents = jsonData.get('contents')
    
    user = User.query.filter_by(user_id=userId).first()
    if user:
        newBoard = notice_board_list(user_id=userId, username=user.username, contents=contents)
        db.session.add(newBoard)
        db.session.commit()
    else:
        print("사용자 정보를 찾을 수 없습니다.")
    return render_template('home.html')

    
    
