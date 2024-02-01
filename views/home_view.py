from flask import Flask, render_template, request, redirect, url_for, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, notice_board_list, User, Friend

bp = Blueprint('home', __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def home():
    input_keyword = request.args.get('query')
    user_cookie_id = request.cookies.get('user_id')

    if input_keyword:
        notice_list = notice_board_list.query.filter(
            (notice_board_list.contents.like(f"%{input_keyword}%")) |
            (notice_board_list.username.like(f"%{input_keyword}%"))
        ).all()
    else:
        notice_list = notice_board_list.query.all()
    
    if user_cookie_id:
        friend_list = Friend.query.filter_by(user_id=user_cookie_id).all()   
    
    print(friend_list)
    
    return render_template('home.html', data=notice_list, friendList=friend_list)

    print("아래와 같음")
    print(notice_list)

    if 'user_id' in request.cookies:
        # 쿠키가 있을 때 다른 페이지로 랜더링
        return render_template('home2.html', data=notice_list)
    else:
        # 쿠키가 없을 때 현재 페이지 랜더링
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

@bp.route("/friend", methods=['POST'])
def addfriend():
    jsonData = request.get_json()
    friend_id_req = jsonData.get("user_id")
    user_cookie_id = request.cookies.get('user_id')
    user_name = User.query.filter_by(user_id=user_cookie_id).first().username
    exist_friend = Friend.query.filter_by(user_id=user_cookie_id, friend_id = friend_id_req).first()
    
    exist_friend = Friend.query.filter_by(user_id=user_cookie_id, friend_id=friend_id_req).first()

    if user_cookie_id and not exist_friend:
        new_friend_row = Friend(user_id=user_cookie_id, username=user_name, friend_id=friend_id_req)
        print(new_friend_row)
        db.session.add(new_friend_row)
        db.session.commit()

    friend_list = Friend.query.filter_by(user_id=user_cookie_id).all()

    return render_template('home.html', friendList=friend_list)
    
    
