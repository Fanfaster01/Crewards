from flask import request, render_template, Blueprint, redirect, url_for, session, flash
from static.config.supabase_config import supabase

user_bp = Blueprint('/static/src/user', __name__)


#Ruta para Registrar Usuarios
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Registro en Supabase
        user, error = supabase.auth.sign_up({
          "email": email,
          "password": password,
        })
        if error:
            flash(str(error), 'danger')
        else:
            flash('Registro exitoso. Por favor, inicia sesión.', 'success')
            return redirect(url_for('login'))
        
    return render_template('/user/Register.html')



@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Iniciar sesión en Supabase
        user, error = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if error:
            flash(str(error), 'danger')
        else:
            session['user'] = user
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
    return render_template('/user/login.html')




@user_bp.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Por favor, inicia sesión para ver esta página', 'danger')
        return redirect(url_for('login'))
    return render_template('/user/Dashboard.html')




@user_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))