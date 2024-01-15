from pydantic import BaseModel

class Login(BaseModel):
    provider_token: str
    