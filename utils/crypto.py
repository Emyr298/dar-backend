from config import Config

def hash_password(password: str) -> str:
    return Config.password_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return Config.password_context.verify(plain_password, hashed_password)
