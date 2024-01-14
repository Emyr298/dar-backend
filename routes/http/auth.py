from fastapi import APIRouter

from validators.auth import Login
from utils.authentication import generate_jwt

router = APIRouter()

@router.post('/login')
async def login(data: Login):
    return {
        'token': generate_jwt(data.provider_token),
    }
