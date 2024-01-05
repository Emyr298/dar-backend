import jwt, time

from utils.firebase import get_email_from_token
from utils.queries.user import get_user_by_email
from settings import Settings

def generate_jwt(token: str):
    email = get_email_from_token(token)
    username = get_user_by_email(email).username
    return jwt.encode({
        'username': username,
        'email': email,
        'expiration_time': time.time() + Settings.jwt.expiration_time
    }, Settings.jwt.secret_key, algorithm='HS256')
    