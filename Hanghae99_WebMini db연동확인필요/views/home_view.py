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
    
    user = User.query.filter_by(user_id=1).first()
    if user:
        newBoard = notice_board_list(user_id=1, username='박찬섭', contents=contents)
        db.session.add(newBoard)
        db.session.commit()
    else:
        print("사용자 정보를 찾을 수 없습니다.")
    return render_template('home.html')

@bp.route('/list/')
def _list():
    somang_list = notice_board_list.query.order_by(notice_board_list.board_id.desc())
    sortboard = request.args.get('sortboard', type=str, default='recent')

    if sortboard == 'maxcomment':
        somang_list = notice_board_list.comment_id.count()
    elif sortboard == 'old':
        somang_list = notice_board_list.query.order_by(notice_board_list.created_at.asc())
    else:
        somang_list = notice_board_list.query.order_by(notice_board_list.created_at.desc())

    return render_template('board.html', somang_list=somang_list, sortboard=sortboard)
    
    
