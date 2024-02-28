from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from database import get_session
from exceptions.exceptions import UserNotFoundException

from services.user_service import get_user_by_username, create_user, delete_user

from models.user import UserRole
from dto.user import StandardUserDTO, ResponderUserDTO, AdminUserDTO, StandardUserCreateDTO, ResponderUserCreateDTO, AdminUserCreateDTO

router = APIRouter()

router.get('/{username}')
def get_user(username: str, session: Session = Depends(get_session)):
    user = get_user_by_username(session, username)
    if not user:
        raise UserNotFoundException()
    
    if user.role == UserRole.ADMIN:
        return AdminUserDTO.model_validate(user)
    elif user.role == UserRole.RESPONDER:
        return ResponderUserDTO.model_validate(user)
    return StandardUserDTO.model_validate(user)

@router.post('/standard', response_model=StandardUserDTO)
def register_standard_user(request: Request, data: StandardUserCreateDTO, session: Session = Depends(get_session)):
    email = str(request.state.email)
    return create_user(session, data, email)
    
@router.post('/responder', response_model=StandardUserDTO)
def register_responder_user(request: Request, data: ResponderUserCreateDTO, session: Session = Depends(get_session)):
    email = str(request.state.email)
    return create_user(session, data, email)

@router.post('/admin', response_model=StandardUserDTO)
def register_admin_user(request: Request, data: AdminUserCreateDTO, session: Session = Depends(get_session)):
    email = str(request.state.email)
    return create_user(session, data, email)

@router.delete('/')
def delete_current_user(request: Request, session: Session = Depends(get_session)):
    if request.state.user is not None:
        delete_user(session, request.state.user)
    return {'detail': 'success'}
