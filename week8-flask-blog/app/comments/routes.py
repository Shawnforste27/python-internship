from flask import Blueprint, request, redirect
from app.models import Comment
from app import db

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/comment/<int:post_id>", methods=["POST"])
def add_comment(post_id):
    comment = Comment(content=request.form["content"], post_id=post_id)
    db.session.add(comment)
    db.session.commit()
    return redirect(f"/post/{post_id}")
