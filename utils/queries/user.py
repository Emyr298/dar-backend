from models.user import User
from sqlalchemy.orm import session as db

def get_user_by_email(email: str) -> User | None:
    return db.query(User).filter_by(email=email).first()
