
from sqlalchemy import Column, Integer, ForeignKey, String, Float, Text

from database import Base

class EmergencyCategory(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    
class Emergency(Base):
    __tablename__ = 'emergency'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(ForeignKey('user.username'), nullable=False, index=True)
    category = Column(ForeignKey('category.id'), nullable=False)
    title = Column(String(64), nullable=True)
    description = Column(Text, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class EmergencyRespond(Base):
    __tablename__ = 'emergencyrespond'
    
    emergency = Column(ForeignKey('emergency.id'), primary_key=True)
    responder = Column(ForeignKey('responderuser.username'), primary_key=True)
    