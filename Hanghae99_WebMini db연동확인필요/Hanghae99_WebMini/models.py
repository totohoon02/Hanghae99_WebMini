from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), nullable=False)
  artist = db.Column(db.String(100), nullable=False)
  title = db.Column(db.String(100), nullable=False)
  image_url = db.Column(db.String(10000), nullable=False)

  def __repr__(self):
      return f'{self.username} {self.title} 추천 by {self.username}'
  