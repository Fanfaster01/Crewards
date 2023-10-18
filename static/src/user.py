from flask import Blueprint, request, redirect, url_for, flash, jsonify
from static.config.supabase_config import supabase
from gotrue.errors import AuthApiError
import gotrue


user_bp = Blueprint('user', __name__, url_prefix='/user')

# Ruta para registrar usuarios 
@user_bp.route('/register')
def register():

    try:
        data = request.json
    
        email = data.get('email')
        password = data.get('password')
    
        # Supabase manejará la comprobación de duplicados por nosotros
        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        if response.user.identities==[]:
            return jsonify({"message":"El Email suministrado ya está en uso, porfavor intente con otro."})
        else:
            return jsonify({"message":"Usuario creado con éxito!, porfavor confirme su email."})
        
    except AuthApiError as error:
    # Manejar el error de la API de autenticación
        return f"Error de autenticación: {error.message}"

  
