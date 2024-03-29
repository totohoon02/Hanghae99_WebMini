import os
from flask import Flask
from models import db
# , User

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] =\
      'sqlite:///' + os.path.join(basedir, 'database.db')

  db.init_app(app)
  db.app = app
  
  
  with app.app_context():
    db.create_all()

  from views import mypage_view, home_view, join_view
  
  app.register_blueprint(mypage_view.bp)
  app.register_blueprint(home_view.bp)
  app.register_blueprint(join_view.bp)
  return app

