import jwt, time
from utils.firebase import get_email_from_token
from models.user import User
from exceptions.exceptions import InvalidProviderTokenException, InvalidTokenException, UnregisteredException, UserNotFoundException
from config import Config

def generate_jwt(provider_token: str):
    email = get_email_from_token(provider_token)
    if not email:
        raise InvalidProviderTokenException()
    
    user = User.get_by_email(email)
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
    
def get_user_from_token(token: str):
    try:
        decoded_token = jwt.decode(token, Config.jwt.secret_key, algorithms=['HS256'])
        
        if time.time() > decoded_token['expiration_time']:
            raise InvalidTokenException()
        
        user = User.get_by_email(decoded_token['email'])
        if not user:
            raise UserNotFoundException()
        return user
    
    except UserNotFoundException:
        raise UnregisteredException()
    except Exception:
        raise InvalidTokenException()
    