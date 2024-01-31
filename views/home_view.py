from flask import Blueprint, render_template, request, url_for, redirect
from models import Song, db

bp = Blueprint('home', __name__, url_prefix="/home")

@bp.route("/")
def music():
    song_list = Song.query.all()
    return render_template('home.html')
