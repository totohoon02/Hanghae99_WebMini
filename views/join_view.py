from flask import Flask, render_template, request, abort, jsonify, make_response, url_for, redirect, request
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import User, db

bp = Blueprint('join', __name__, url_prefix="/join")







@bp.route('/sign')
def join():
    return render_template("join.html")


@bp.route('/check', methods=['POST'])
def check():
    id = request.form.get("id")
    user_in_db = User.query.filter_by(user_id=id).first()
    if user_in_db:
        abort(404)
    else:
        return {"msg": "중복없음"}


@bp.route('/home')
def ss():
	return render_template("home.html")


@bp.route("/signup", methods=['POST'])
def music():
    id = request.form.get("id")
    pw = request.form.get("password")
    name = request.form.get("name")
    user = User(user_id=id, password=pw, username=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "가입완료!"})


@bp.route("/login", methods=['POST'])
def login():
    ids = request.form.get("ids")
    pws = request.form.get("passwords")
    check = User.query.filter_by(user_id=ids, password=pws).first()
    if check:
        resp = make_response("Cookie Setting Complete")
        resp.set_cookie('user_id', ids)
        return resp
    return abort(404)


@bp.route("/home")
def hh():
    return redirect(url_for("/"))


