from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager
from static.config.supabase_config import supabase


user_bp = Blueprint('user', __name__, url_prefix='/user')

login_manager = LoginManager()

def init_app(app):
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

class User():
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    user = supabase.auth.get_user(user_id)
    if user:
        return User(user.user.id, user.user.email, user.user)

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = supabase.auth.sign_in_with_password({
            "email": email, 
            "password": password
        })
        if not result.user:
            flash('Email o contraseña incorrectos', 'error')
            return redirect(url_for('user.login'))
        else:
            user = User(result.user.id, email, password)
            login_user(user)
            return redirect(url_for('user.dashboard'))
    else:
        return render_template('/user/Login.html')

@user_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        print(result)
        if result.user.identities[]:

        return render_template('/user/Dashboard.html')
    return render_template('/user/Register.html')

"""         if result.user:
            flash('Usuario registrado exitosamente', 'success')
            return redirect(url_for('user.login'))
            flash('El email ya está registrado', 'error')
            return redirect(url_for('user.Register'))
        else:
            if result.get('error'):
                flash('Error al registrar usuario', 'error')
                return redirect(url_for('user.signup'))
            else:
    else: """

@user_bp.route('/dashboard')
@login_required
def dashboard():
    user = supabase.auth.get_user(current_user.id).get('user')
    if user:
        return render_template('dashboard.html', user=user)
    else:
        flash('Error al cargar el usuario', 'error')
        return redirect(url_for('user.login'))

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@user_bp.route('/delete_user')
@login_required
def delete_user():
    user_id = current_user.id
    result = supabase.auth.delete_user(user_id)
    if result.get('error'):
        flash('Error al eliminar usuario', 'error')
    else:
        flash('Usuario eliminado exitosamente', 'success')
        logout_user()
    return redirect(url_for('user.login'))