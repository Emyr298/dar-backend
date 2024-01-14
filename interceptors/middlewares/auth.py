from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from enums.auth import AuthStatus
from utils.authentication import get_user_from_token
from exceptions.exceptions import UnregisteredException

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        token = request.headers.get('Authorization', '')[len('Bearer '):]
        try:
            request.state.user = get_user_from_token(token)
            request.state.auth_status = AuthStatus.REGISTERED
        except UnregisteredException:
            request.state.auth_status = AuthStatus.UNREGISTERED
        except:
            request.state.user = None
            request.state.auth_status = AuthStatus.GUEST
        return await call_next(request)
