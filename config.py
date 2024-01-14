import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials

load_dotenv()

class Config:
    class JWTConfig:
        secret_key = os.environ.get('SECRET_KEY')
        expiration_time = 120
        
    class FirebaseConfig:
        credentials = credentials.Certificate('keys/firebase.json')
    
    class DatabaseConfig:
        url = os.environ.get('DATABASE_URL')
    
    jwt = JWTConfig()
    firebase = FirebaseConfig()
    database = DatabaseConfig()
    