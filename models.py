from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  image_url = db.Column(db.String(10000), nullable=False)

  def __repr__(self):
      return f'{self.username} {self.title} 추천 by {self.username}'
    

class notice_board_list(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  contents = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  comment_id = db.Column(db.Integer, nullable=True)
  
class User(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
  frinedlist = db.Column(db.String, nullable=True)