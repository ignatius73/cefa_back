
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models import User
from app.schemas import UserRequestModel, UserRequestPutModel, UserResponseModel, UsersResponseModel
from sql_alchemy.models import Item


router = APIRouter()

@router.get('/usuarios', response_model=List[UsersResponseModel])
async def get_all_users():
    users = User.select()
    #return [user for user in users]
    return users

@router.get('/usuarios/{user_id}', response_model=UsersResponseModel)
async def usuariosById(user_id:int):
    user = User.select().where(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='El usuario no existe')
    return  user

@router.post('/usuarios', response_model=UserResponseModel)
async def create_user(user:UserRequestModel):

    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username ya se encuentra en uso')
    hashed_password = User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hashed_password,
        name=user.name,
        surname=user.surname,
        dni=user.dni,
        phone=user.phone,
        photoUrl=user.photoUrl
    )
    return UserResponseModel(
        id= user.id,
        username=user.username
    )


@router.put('/usuarios/{user_id}', response_model=UsersResponseModel)
async def update_user(user_id:int, item:UserRequestPutModel):
    user_to_update = User.select().where(user_id==User.id).first()
    if user_to_update is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_to_update.phone = item.phone
    user_to_update.photoUrl = item.photoUrl

    user_to_update.save()

    return user_to_update

@router.delete('/user/{user_id}', response_model=UsersResponseModel)
def delete_user(user_id:int):
    user_to_delete = User.select().where(user_id==User.id).first()

    if user_to_delete is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
    user_to_delete.delete_instance()

    return user_to_delete

