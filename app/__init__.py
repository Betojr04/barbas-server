from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
import os

db = MongoEngine()

def create_app(): 
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "https://barbas.vercel.app"]}})
    
    # Register blueprints
    from app.routes.contact import contact_bp
    app.register_blueprint(contact_bp, url_prefix='/api/contact')
    
    return app
