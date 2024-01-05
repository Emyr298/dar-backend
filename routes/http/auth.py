from fastapi import APIRouter

from validators.auth import Login
from utils.authenticator import generate_jwt

router = APIRouter('/api/v1/auth')

@router.post('/login')
async def login(data: Login):
    return {
        'token': generate_jwt(data.provider_token),
    }

# @router.post()
