
from sqlalchemy import Column, ForeignKey, String, Float, CheckConstraint
from sqlalchemy.orm import Session
from enum import Enum

from database import Base, get_session

class UserRole(str, Enum):
    BASE_USER = 'user'
    STANDARD = 'standard'
    RESPONDER = 'responder'
    ADMIN = 'admin'

class User(Base):
    __tablename__ = 'user'
    
    username = Column(String(64), primary_key=True)
    email = Column(String(64), unique=True)
    password = Column(String(64))
    role = Column(String(64))
    
    __mapper_args__ = {
        'polymorphic_identity': UserRole.BASE_USER,
        'polymorphic_on': 'role'
    }
    
class StandardUser(User):
    __tablename__ = 'standard_user'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    report_rating = Column(Float, CheckConstraint('report_rating >= 0 AND report_rating <= 5'), default=0)
    
    __mapper_args__ = {
        'polymorphic_identity': UserRole.STANDARD,
    }

class ResponderUser(User):
    __tablename__ = 'responder_user'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    respond_rating = Column(Float, CheckConstraint('respond_rating >= 0 AND respond_rating <= 5'), default=0)
    
    __mapper_args__ = {
        'polymorphic_identity': UserRole.RESPONDER,
    }
    
class AdminUser(User):
    __tablename__ = 'admin_user'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': UserRole.ADMIN,
    }
    