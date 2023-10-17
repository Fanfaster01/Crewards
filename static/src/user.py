from flask import Blueprint, request, redirect, url_for, flash, jsonify
from static.config.supabase_config import supabase


user_bp = Blueprint('user', __name__, url_prefix='/user')

# Ruta para registrar usuarios 
@user_bp.route('/register')
def register():

    data = request.json

    email = data.get('email')
    password = data.get('password')

    # Supabase manejará la comprobación de duplicados por nosotros
    response = supabase.auth.sign_up({
        "email": email,
        "password": password
    })

    return jsonify(response.user)
