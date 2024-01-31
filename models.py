from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Song(db.Model):
  board_id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  image_url = db.Column(db.String(10000), nullable=False)

  def __repr__(self):
      return f'{self.username} {self.title} 추천 by {self.username}'

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
