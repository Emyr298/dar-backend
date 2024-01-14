from fastapi import Request

from enums.auth import AuthStatus
from exceptions.exceptions import GuestException, UnregisteredException

def register_required(request: Request):
    if request.state.auth_status != AuthStatus.REGISTERED:
        raise UnregisteredException()
    
def login_required(request: Request):
    if request.state.auth_status == AuthStatus.GUEST:
        raise GuestException()
    