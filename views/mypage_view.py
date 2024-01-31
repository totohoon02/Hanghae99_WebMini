from flask import Blueprint, render_template, request, url_for, redirect
# from models import Song, db

bp = Blueprint('myPage', __name__, url_prefix="/mypage")

@bp.route("/", methods=["GET"])
def myPage():
      # wishList, friendList
      context = {
          "ff" : 232332
      }
      return render_template("myPage.html", data=context)
      
@bp.route("/deleteWish", methods=["DELETE"])
def deleteWish():
    wishID = request.json['id']
    print(wishID)
    return "200"

@bp.route("/deleteFriend", methods=["DELETE"])
def deleteFriend():
    wishID = request.json['id']
    print(wishID)
    return "200"

@bp.route("/<wishid>")
def myPageDetail(wishid):
  #소망에 해당하는 정보, 댓글 가져오기
  return render_template("myPageDetail.html")
