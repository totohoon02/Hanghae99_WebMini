from flask import Blueprint, render_template, request, url_for, redirect
from models import Wish, Friend, db

bp = Blueprint('myPage', __name__, url_prefix="/mypage")

@bp.route("/", methods=["GET"])
def myPage():
    # 사용자 ID를 가져와서 검색!
    boards = Wish.query.filter(Wish.username.in_(['totohoon01'])).all()
    friends = Friend.query.filter(Friend.username.in_(['totohoon01'])).all()

    return render_template("myPage.html", data= {
        "boards" : boards,
        "friends" : friends 
    })
    
@bp.route("/deleteWish", methods=["DELETE"])
def deleteWish():
    wishID = request.json['id']
    Wish.query.filter(Wish.board_id == wishID).delete()
    db.session.commit()
    return "200"

@bp.route("/deleteFriend", methods=["DELETE"])
def deleteFriend():
    wishID = request.json['id']
    return "200"

@bp.route("/<wishid>")
def myPageDetail(wishid):
  # 글 내용, 댓글리스트 가져오기
  board = Wish.query.filter(Wish.board_id == wishid).one()
  return render_template("myPageDetail.html", data={
      "board" : board,
  })
