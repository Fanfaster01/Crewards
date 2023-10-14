from flask import Flask, render_template
from flask_cors import CORS
from static.src.user import user_bp
from static.src.user import init_app

app = Flask(__name__)
app.secret_key = 'K*i*r3a4'
CORS(app)

# Registrar blueprint User
app.register_blueprint(user_bp, url_prefix='/user')
init_app(app)


@app.route("/")
def index():
	return render_template("/index.html")

if __name__ == '__main__':
	app.run(debug=True)