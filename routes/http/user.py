from fastapi import APIRouter, Request

router = APIRouter()

@router.get('/status')
async def login(request: Request):
    return request.state.auth_status.name
