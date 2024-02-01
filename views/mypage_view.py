from flask import Blueprint, render_template, request, url_for, redirect
from models import notice_board_list, Friend, comment_list, db

bp = Blueprint('myPage', __name__, url_prefix="/mypage")

@bp.route("/", methods=["GET"])
def myPage():
    userID = request.cookies.get("user_id")
    boards = notice_board_list.query.filter(notice_board_list.user_id.in_([userID])).all()
    friends = Friend.query.filter(Friend.user_id.in_([userID])).all()

    return render_template("myPage.html", data= {
        "boards" : boards,
        "friends" : friends 
    })
    
@bp.route("/deleteWish", methods=["DELETE"])
def deleteWish():
    wishID = request.json['id']
    deleteBoard = notice_board_list.query.filter_by(board_id = wishID).first()
    db.session.delete(deleteBoard)
    db.session.commit()
    return "200"

@bp.route("/deleteFriend", methods=["DELETE"])
def deleteFriend():
    friendID = request.json['id']
    print(friendID)
    try:
        Friend.query.filter(Friend.friend_id == friendID).delete()
        db.session.commit()
        return {"status" : "200"}
    except:
        raise Exception("친구 삭제 실패")

@bp.route("/<wishid>")
def myPageDetail(wishid):
  board = notice_board_list.query.filter(notice_board_list.board_id == wishid).one()
  comments = comment_list.query.filter(comment_list.board_id == wishid).all()
  return render_template("myPageDetail.html", data={
      "board" : board,
      "comments" : comments
  })
