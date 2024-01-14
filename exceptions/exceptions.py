from fastapi import HTTPException    

# 401
class ForbiddenException(HTTPException):
    status = 401
    def __init__(self, message='Forbidden'):
        self.message = message
        super().__init__(status_code=self.status, detail=self.message)

class GuestException(ForbiddenException):
    def __init__(self, message='User is not logged in'):
        self.message = message
        super().__init__(self.message)

class UnregisteredException(ForbiddenException):
    def __init__(self, message='User is not registered'):
        self.message = message
        super().__init__(self.message)

# 404
class NotFoundException(HTTPException):
    status = 404
    def __init__(self, message='Object is not found'):
        self.message = message
        super().__init__(status_code=self.status, detail=self.message)

class UserNotFoundException(NotFoundException):
    def __init__(self, message='User is not found'):
        self.message = message
        super().__init__(self.message)

# Misc
class InvalidProviderTokenException(Exception):
    def __init__(self, message='Provider token is not valid'):
        self.message = message
        super().__init__(self.message)

class InvalidTokenException(Exception):
    def __init__(self, message='Token is not valid'):
        self.message = message
        super().__init__(self.message)

class ConfigurationException(Exception):
    def __init__(self, message='A configuration is None'):
        self.message = message
        super().__init__(self.message)