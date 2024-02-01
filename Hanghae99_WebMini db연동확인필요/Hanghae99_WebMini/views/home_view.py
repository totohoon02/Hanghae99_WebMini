from flask import Blueprint, render_template, request, url_for, redirect, config
from models import Song, db
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

bp = Blueprint('home', __name__, url_prefix="/home")






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