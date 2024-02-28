import os
from dotenv import load_dotenv
from firebase_admin import credentials
from enum import Enum, auto
from passlib.context import CryptContext

load_dotenv()

class Environment(Enum):
    PRODUCTION = 'production'
    DEBUG = 'debug'

class Config:
    class JWTConfig:
        secret_key = os.environ.get('SECRET_KEY')
        expiration_time = 120
        
    class FirebaseConfig:
        credentials = credentials.Certificate('keys/firebase.json')
    
    class DatabaseConfig:
        url = os.environ.get('DATABASE_URL')
    
    environment = Environment.PRODUCTION if os.getenv('ENVIRONMENT') == 'production' else Environment.DEBUG
    jwt = JWTConfig()
    firebase = FirebaseConfig()
    database = DatabaseConfig()
    password_context = CryptContext(
        schemes=['bcrypt'],
        deprecated='auto'
    )
    