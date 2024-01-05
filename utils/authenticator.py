import jwt, time
from utils.firebase import get_email_from_token
from utils.queries.user import get_user_by_email
from exceptions import InvalidProviderTokenException, InvalidTokenException, UnregisteredException, UserNotFoundException
from settings import Settings

def generate_jwt(token: str):
    email = get_email_from_token(token)
    if not email:
        raise InvalidProviderTokenException()
    
    user = get_user_by_email(email)
    if not user:
        return jwt.encode({
            'is_registered': False,
            'email': email,
            'expiration_time': time.time() + Settings.jwt.expiration_time,
        }, Settings.jwt.secret_key, algorithm='HS256')
    
    username = get_user_by_email(email).username
    return jwt.encode({
        'is_registered': True,
        'username': username,
        'email': email,
        'expiration_time': time.time() + Settings.jwt.expiration_time,
    }, Settings.jwt.secret_key, algorithm='HS256')
    
def get_user_from_token(token: str):
    try:
        decoded_token = jwt.decode(token, Settings.jwt.secret_key, algorithms=['HS256'])
        
        if time.time() > decoded_token['expiration_time']:
            raise InvalidTokenException()
        
        user = get_user_by_email(decoded_token['email'])
        if not user:
            raise UserNotFoundException()
        return user
    
    except UserNotFoundException:
        raise UnregisteredException()
    except Exception:
        raise InvalidTokenException()
    