
from sqlalchemy import Column, ForeignKey, String, Float

from database import Base

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
    
class StandardUser(User):
    __tablename__ = 'standarduser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    report_rating = Column(Float, min=0, max=5)
    
    __mapper_args__ = {
        'polymorphic_identity': 'standard',
    }

class ResponderUser(User):
    __tablename__ = 'responderuser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    respond_rating = Column(Float, min=0, max=5)
    
    __mapper_args__ = {
        'polymorphic_identity': 'responder',
    }
    
class AdminUser(User):
    __tablename__ = 'adminuser'
    
    username = Column(ForeignKey('user.username'), primary_key=True)
    
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }
    