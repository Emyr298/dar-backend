
from sqlalchemy import Column, ForeignKey, String, Float, CheckConstraint

from database import Base, get_session

class User(Base):
    __tablename__ = 'user'
    
    username = Column(String(64), primary_key=True)
    email = Column(String(64), unique=True)
    password = Column(String(64))
    role = Column(String(64))
    
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': 'role'
    }
    
    def get_by_email(email: str | None):
        db = get_session()
        if not email:
            return None
        return db.query(User).filter_by(email=email).first()
    
    def get_by_username(username: str):
        db = get_session()
        return db.query(User).filter_by(username=username).first()
    
class StandardUser(User):
    __tablename__ = 'standarduser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    report_rating = Column(Float, CheckConstraint('report_rating >= 0 AND report_rating <= 5'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'standard',
    }

class ResponderUser(User):
    __tablename__ = 'responderuser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    respond_rating = Column(Float, CheckConstraint('respond_rating >= 0 AND respond_rating <= 5'))
    
    __mapper_args__ = {
        'polymorphic_identity': 'responder',
    }
    
class AdminUser(User):
    __tablename__ = 'adminuser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }
    