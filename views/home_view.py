from flask import Flask, render_template, request, redirect, url_for, Blueprint
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, notice_board_list, User, Friend, comment_list

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

    friend_list = Friend.query.filter_by(user_id=user_cookie_id).all()
    
    
    return render_template('home.html', data=notice_list, friendList=friend_list)

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
    exist_friend = Friend.query.filter_by(user_id=user_cookie_id, friend_id=friend_id_req).first()

    if user_cookie_id and not exist_friend:
        new_friend_row = Friend(user_id=user_cookie_id, username=user_name, friend_id=friend_id_req)
        db.session.add(new_friend_row)
        db.session.commit()

    # user_cookie_id가 None이 아닌 경우에만 friend_list 초기화
    friend_list = Friend.query.filter_by(user_id=user_cookie_id).all() if user_cookie_id else []

    return render_template('home.html', friendList=friend_list)

@bp.route('/sort')
def _list():
    sortboard = request.args.get('sortboard', type=str, default='recent')

    if sortboard == 'maxcomment':
        somang_list = notice_board_list.query.order_by(notice_board_list.comment_id.desc()).all()
    elif sortboard == 'old':
        somang_list = notice_board_list.query.order_by(notice_board_list.created_at.asc()).all()
    else:
        somang_list = notice_board_list.query.order_by(notice_board_list.created_at.desc()).all()

    return render_template('home.html', data=somang_list, sortboard=sortboard)


@bp.route("/get_comments")
def update():
    board_id = request.args.get('boardId')
    comments = comment_list.query.filter(
        comment_list.board_id == board_id).all()
    return {'data': comments}


@bp.route("/wish/<wishid>")
def godetail(wishid):
  # 글 내용, 댓글리스트 가져오기
  board = notice_board_list.query.filter(
      notice_board_list.board_id == wishid).one()
  test = True
  comments = comment_list.query.filter(comment_list.board_id == wishid).all()
  usernames = [comment.comment_user_id for comment in comments]
  first_comment_username = usernames[0] if usernames else ""
# User 테이블에서 작성자 정보 가져오기 (예시로 첫 번째 댓글의 작성자 정보 사용)
  user = User.query.filter(User.username == first_comment_username).first()

# User 테이블에서 가져온 사용자 정보에서 username 추출
  username = user.username if user else ""
  return render_template("myPageDetail.html", data={
      "board": board, "test": test, "comments": comments, "username": username
  })


@bp.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    board_id = data.get('board_id')
    comment_id = data.get('comment_id')
    comment_content = data.get('comment_content')
    new_comment = comment_list(
        board_id=board_id, comment_user_id=comment_id, comment=comment_content)
    db.session.add(new_comment)
    db.session.commit()
    return ({'message': '댓글이 성공적으로 추가되었습니다.'})
