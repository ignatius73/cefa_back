from typing import Any
from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from peewee import ModelSelect

#----------------User Validators ----------------------------
class UserValidators():

    @validator('username')
    def username_validator(cls, username):
        if len(username) <3 or len(username)>50:
            raise ValueError('La longitud del Username debe ser mayor a 3 caracteres y menor a 50')
        return username


class PeeweeGetterDict(GetterDict):
    def get(self,key:Any, default:Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res,ModelSelect):
            return list(res)
        return res

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict    

class UserRequestPutModel(BaseModel):
    phone:int
    photoUrl:str

class UserRequestModel(BaseModel, UserValidators):
    username: str
    password: str
    name: str
    surname: str
    dni: int
    phone: int
    photoUrl:str



class UserResponseModel(ResponseModel):
    id:int
    username:str

class UsersResponseModel(ResponseModel):
    username: str
    password: str
    name: str
    surname: str
    dni: int
    phone: int
    photoUrl:str

