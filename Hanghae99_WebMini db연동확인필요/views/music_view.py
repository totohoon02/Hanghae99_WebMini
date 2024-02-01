from flask import Blueprint, render_template, request, url_for, redirect
from models import Song, db

bp = Blueprint('music', __name__, url_prefix="/music")

@bp.route("/")
def music():
    song_list = Song.query.all()
    return render_template('music.html', data=song_list)

@bp.route("/music/create/")
def music_create():
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    artist_receive = request.args.get("artist")
    image_receive = request.args.get("image_url")

    song = Song(username = username_receive, title=title_receive, artist=artist_receive, image_url=image_receive)
    db.session.add(song)
    db.session.commit()
    return redirect(url_for("music.music"))

@bp.route("/music/delete/")
def music_delete():
    title = request.args.get("title")
    delItem = db.session.query(Song).filter(Song.title == title).first()
    db.session.delete(delItem)
    db.session.commit()
    return redirect(url_for("music.music"))

