from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dto.auth import Login
from services.auth_service import generate_jwt
from database import get_session

router = APIRouter()

@router.post('/login')
def login(data: Login, session: Session = Depends(get_session)):
    return {
        'token': generate_jwt(session, data.provider_token),
    }
