from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chjnp1qq%2s#%bixja1hc3t_ej*r5!qdr$f1^hvqvgs+hhvj!q'
    return app