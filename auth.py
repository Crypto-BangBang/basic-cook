from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User, Favorite, CookingLog, RecipeNote, CourseProgress

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        lang = request.args.get('lang', 'ko')
        return redirect(url_for('index', lang=lang))

    lang = request.args.get('lang', 'ko')
    error = None

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=True)
            next_page = request.args.get('next', '')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('index', lang=lang)
            return redirect(next_page)
        error = {
            'ko': '이메일 또는 비밀번호가 올바르지 않아요.',
            'en': 'Incorrect email or password.',
            'ja': 'メールアドレスまたはパスワードが正しくありません。',
            'zh': '邮箱或密码不正确。',
        }.get(lang, '이메일 또는 비밀번호가 올바르지 않아요.')

    return render_template('login.html', lang=lang, error=error)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        lang = request.args.get('lang', 'ko')
        return redirect(url_for('index', lang=lang))

    lang = request.args.get('lang', 'ko')
    error = None

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        password2 = request.form.get('password2', '')

        if not email or not username or not password:
            error = {'ko': '모든 항목을 입력해주세요.', 'en': 'Please fill in all fields.',
                     'ja': 'すべての項目を入力してください。', 'zh': '请填写所有字段。'}.get(lang)
        elif password != password2:
            error = {'ko': '비밀번호가 일치하지 않아요.', 'en': 'Passwords do not match.',
                     'ja': 'パスワードが一致しません。', 'zh': '两次密码不一致。'}.get(lang)
        elif len(password) < 6:
            error = {'ko': '비밀번호는 6자 이상이어야 해요.', 'en': 'Password must be at least 6 characters.',
                     'ja': 'パスワードは6文字以上にしてください。', 'zh': '密码至少需要6个字符。'}.get(lang)
        elif User.query.filter_by(email=email).first():
            error = {'ko': '이미 사용 중인 이메일이에요.', 'en': 'Email already in use.',
                     'ja': 'このメールアドレスはすでに使われています。', 'zh': '该邮箱已被使用。'}.get(lang)
        else:
            user = User(email=email, username=username)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('index', lang=lang))

    return render_template('register.html', lang=lang, error=error)


@auth_bp.route('/logout')
@login_required
def logout():
    lang = request.args.get('lang', 'ko')
    logout_user()
    return redirect(url_for('index', lang=lang))


@auth_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    lang = request.args.get('lang', 'ko')
    current_pw = request.form.get('current_password', '')
    new_pw = request.form.get('new_password', '')
    new_pw2 = request.form.get('new_password2', '')

    if not current_user.check_password(current_pw):
        flash({'ko': '현재 비밀번호가 올바르지 않아요.', 'en': 'Current password is incorrect.',
               'ja': '現在のパスワードが正しくありません。', 'zh': '当前密码不正确。'}.get(lang))
    elif new_pw != new_pw2:
        flash({'ko': '새 비밀번호가 일치하지 않아요.', 'en': 'New passwords do not match.',
               'ja': '新しいパスワードが一致しません。', 'zh': '新密码不一致。'}.get(lang))
    elif len(new_pw) < 6:
        flash({'ko': '비밀번호는 6자 이상이어야 해요.', 'en': 'Password must be at least 6 characters.',
               'ja': 'パスワードは6文字以上にしてください。', 'zh': '密码至少需要6个字符。'}.get(lang))
    else:
        current_user.set_password(new_pw)
        db.session.commit()
        flash({'ko': '비밀번호가 변경됐어요.', 'en': 'Password updated.',
               'ja': 'パスワードを変更しました。', 'zh': '密码已更改。'}.get(lang))

    return redirect(url_for('profile', lang=lang))


@auth_bp.route('/delete-account', methods=['POST'])
@login_required
def delete_account():
    lang = request.args.get('lang', 'ko')
    password = request.form.get('password', '')

    if not current_user.check_password(password):
        flash({'ko': '비밀번호가 올바르지 않아요.', 'en': 'Incorrect password.',
               'ja': 'パスワードが正しくありません。', 'zh': '密码不正确。'}.get(lang))
        return redirect(url_for('profile', lang=lang))

    user = User.query.filter_by(id=current_user.id).first()
    user_id = user.id
    logout_user()
    Favorite.query.filter_by(user_id=user_id).delete()
    CookingLog.query.filter_by(user_id=user_id).delete()
    RecipeNote.query.filter_by(user_id=user_id).delete()
    CourseProgress.query.filter_by(user_id=user_id).delete()
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('index', lang=lang))
