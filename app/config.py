import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGODB_SETTINGS = {
        'db': 'barbas',
        'host': os.getenv('MONGODB_URI')
    }
    SECRET_KEY = os.getenv('SECRET_KEY')
