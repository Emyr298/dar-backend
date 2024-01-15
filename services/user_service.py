from sqlalchemy.orm import Session

from models.user import User, StandardUser, ResponderUser, AdminUser
from dto.user import StandardUserCreateDTO, ResponderUserCreateDTO, AdminUserCreateDTO

def get_user_by_email(session: Session, email: str | None):
    if not email:
        return None
    return session.query(User).filter_by(email=email).first()
    
def get_user_by_username(session: Session, username: str):
    return session.query(User).filter_by(username=username).first()

def create_standard_user(session: Session, data: StandardUserCreateDTO, email: str):
    user = StandardUser(**data.model_dump(), email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_responder_user(session: Session, data: ResponderUserCreateDTO, email: str):
    user = ResponderUser(**data.model_dump(), email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def create_admin_user(session: Session, data: AdminUserCreateDTO, email: str):
    user = AdminUser(**data.model_dump(), email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user: User):
    session.delete(user)
    session.commit()
