from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone


def _now():
    return datetime.now(timezone.utc)

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=_now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_path = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=_now)
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_path', name='uq_fav'),)


class CookingLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_path = db.Column(db.String(200), nullable=False)
    count = db.Column(db.Integer, default=1)
    last_cooked = db.Column(db.DateTime, default=_now)
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_path', name='uq_log'),)


class RecipeNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_path = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, default='')
    updated_at = db.Column(db.DateTime, default=_now)
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_path', name='uq_note'),)


class CourseProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_path = db.Column(db.String(200), nullable=False)
    completed_at = db.Column(db.DateTime, default=_now)
    __table_args__ = (db.UniqueConstraint('user_id', 'recipe_path', name='uq_prog'),)
