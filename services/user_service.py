from sqlalchemy.orm import Session

from models.user import User, StandardUser, ResponderUser, AdminUser
from dto.user import UserCreateDTO, ResponderUserCreateDTO, AdminUserCreateDTO
from utils.crypto import hash_password

def get_user_by_email(session: Session, email: str | None):
    if not email:
        return None
    return session.query(User).filter_by(email=email).first()
    
def get_user_by_username(session: Session, username: str):
    return session.query(User).filter_by(username=username).first()

def create_user(session: Session, data: UserCreateDTO, email: str):
    data.password = hash_password(data.password)
    if isinstance(data, AdminUserCreateDTO):
        user = AdminUser(**data.model_dump(), email=email)
    elif isinstance(data, ResponderUserCreateDTO):
        user = ResponderUser(**data.model_dump(), email=email)
    else:
        user = StandardUser(**data.model_dump(), email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user: User):
    session.delete(user)
    session.commit()
