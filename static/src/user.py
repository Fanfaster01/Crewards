from flask import request, render_template, Blueprint
from static.config.supabase_config import supabase

user_bp = Blueprint('/static/src/user', __name__)


#Ruta para Registrar Usuarios
@user_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')

    # Insertar el usuario en la base de datos
    supabase.insert_user(email, password, name, surname, phone)