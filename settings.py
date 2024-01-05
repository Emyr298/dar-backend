import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials

load_dotenv()

class Settings:
    class JWTSettings:
        secret_key = os.environ.get('SECRET_KEY')
        expiration_time = 120
        
    class FirebaseSettings:
        credentials = credentials.Certificate('keys/firebase.json')
    
    jwt = JWTSettings()
    firebase = FirebaseSettings()
    