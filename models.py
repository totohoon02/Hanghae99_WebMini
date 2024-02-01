from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Song(db.Model):
  board_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  image_url = db.Column(db.String(10000), nullable=False)


class Friend(db.Model):
  index = db.Column(db.Integer, primary_key=True, nullable=False)
  user_id = db.Column(db.String, nullable=False)
  username = db.Column(db.String(100), nullable=False)
  friend_id = db.Column(db.String(100), nullable=False)   

class notice_board_list(db.Model):
  board_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String, db.ForeignKey('user.user_id'), nullable=False)
  username = db.Column(db.String, nullable=False)
  contents = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  comment_id = db.Column(db.Integer, nullable=True)
  
class User(db.Model):
  user_id = db.Column (db.String, primary_key=True)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  friendlist = db.Column(db.String, nullable=True)

class comment_list(db.Model):
  board_id = db.Column(db.String,  db.ForeignKey(
      'notice_board_list.board_id'), nullable=False)
  comment_user_id = db.Column(db.String, nullable=False)
  comment_id = db.Column(db.Integer, primary_key=True)
  comment = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)