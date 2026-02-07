from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Post
from app import db
from .forms import PostForm

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/create", methods=["GET","POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect("/")
    return render_template("create_post.html", form=form)

@posts_bp.route("/post/<int:id>")
def post_detail(id):
    post = Post.query.get_or_404(id)
    return render_template("post_detail.html", post=post)
