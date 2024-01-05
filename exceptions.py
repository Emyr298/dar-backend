class InvalidProviderTokenException(Exception):
    def __init__(self, message='Provider token is not valid'):
        self.message = message
        super().__init__(self.message)

class InvalidTokenException(Exception):
    def __init__(self, message='Token is not valid'):
        self.message = message
        super().__init__(self.message)
        
class UserNotFoundException(Exception):
    def __init__(self, message='User is not found'):
        self.message = message
        super().__init__(self.message)
        
class UnregisteredException(Exception):
    def __init__(self, message='User is not registered'):
        self.message = message
        super().__init__(self.message)
        