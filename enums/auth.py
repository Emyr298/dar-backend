from enum import Enum, auto

class AuthStatus(Enum):
    GUEST = auto()
    UNREGISTERED = auto()
    REGISTERED = auto()
