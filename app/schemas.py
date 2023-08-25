from pydantic import BaseModel, validator


class UserRequestModel(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    dni: int
    phone: int

    @validator('username')
    def username_validator(cls, username):
        if len(username) <3 or len(username)>50:
            raise ValueError('La longitud del Username debe ser mayor a 3 caracteres y menor a 50')
        return username
    
class UserResponseModel(BaseModel):
    id:int
    username:str