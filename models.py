from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Song(db.Model):
  board_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  image_url = db.Column(db.String(10000), nullable=False)

class Wish(db.Model):
  board_id = db.Column(db.String(100), primary_key=True, nullable=False) 
  username = db.Column(db.String(100), nullable=False) 
  board_title = db.Column(db.String(100), nullable=False) 
  contents = db.Column(db.String(100), nullable=False) 
  create_at = db.Column(db.String(100), nullable=False)

class Friend(db.Model):
  index = db.Column(db.Integer, primary_key=True, nullable=False)
  username = db.Column(db.String(100), nullable=False)
  friend = db.Column(db.String(100), nullable=False)

    

class notice_board_list(db.Model):
  board_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
  username = db.Column(db.String, nullable=False)
  contents = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  comment_id = db.Column(db.Integer, nullable=True)
  
class User(db.Model):
  user_id = db.Column (db.String, primary_key=True)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  friendlist = db.Column(db.String, nullable=True)