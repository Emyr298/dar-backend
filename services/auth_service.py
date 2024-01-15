import jwt, time
from sqlalchemy.orm import Session

from exceptions.exceptions import InvalidProviderTokenException, InvalidTokenException, UnregisteredException, UserNotFoundException
from config import Config

from utils.firebase import get_email_from_token
from services.user_service import get_user_by_email

def generate_jwt(session: Session, provider_token: str):
    email = get_email_from_token(provider_token)
    if not email:
        raise InvalidProviderTokenException()
    
    user = get_user_by_email(session, email)
    if not user:
        return jwt.encode({
            'is_registered': False,
            'email': email,
            'expiration_time': time.time() + Config.jwt.expiration_time,
        }, Config.jwt.secret_key, algorithm='HS256')
    
    username = user.username
    return jwt.encode({
        'is_registered': True,
        'username': username,
        'email': email,
        'expiration_time': time.time() + Config.jwt.expiration_time,
    }, Config.jwt.secret_key, algorithm='HS256')

def get_email_from_token(token: str):
    try:
        decoded_token = jwt.decode(token, Config.jwt.secret_key, algorithms=['HS256'])
        
        if time.time() > decoded_token['expiration_time']:
            raise InvalidTokenException()
        
        return str(decoded_token['email'])
    except Exception:
        raise InvalidTokenException()

def get_user_from_token(session: Session, token: str):
    try:
        email = get_email_from_token(session, token)
        user = get_user_by_email(session, email)
        if not user:
            raise UserNotFoundException()
        return user
    
    except UserNotFoundException:
        raise UnregisteredException()
    except Exception:
        raise InvalidTokenException()
