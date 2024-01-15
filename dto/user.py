from pydantic import BaseModel

from models.user import UserRole

# User
class UserBaseDTO(BaseModel):
    username: str
    role: UserRole

class UserDTO(UserBaseDTO):
    email: str
    
    class Config:
        from_attributes = True

class UserCreateDTO(UserBaseDTO):
    password: str

# Standard User
class StandardUserBaseDTO(UserBaseDTO):
    pass

class StandardUserDTO(UserDTO, StandardUserBaseDTO):
    report_rating: float

class StandardUserCreateDTO(UserCreateDTO, StandardUserBaseDTO):
    pass

# Responder User
class ResponderUserBaseDTO(UserBaseDTO):
    pass

class ResponderUserDTO(UserDTO, ResponderUserBaseDTO):
    respond_rating: float

class ResponderUserCreateDTO(UserCreateDTO, ResponderUserBaseDTO):
    pass

# Admin User
class AdminUserBaseDTO(UserBaseDTO):
    pass

class AdminUserDTO(UserDTO, AdminUserBaseDTO):
    pass

class AdminUserCreateDTO(UserCreateDTO, AdminUserBaseDTO):
    pass
