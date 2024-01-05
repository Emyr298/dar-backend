from firebase_admin import auth

def get_email_from_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token['email']
    except Exception:
        return None
    