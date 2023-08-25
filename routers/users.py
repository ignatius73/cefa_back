from fastapi import APIRouter, Depends, HTTPException
from app.models import User
from app.schemas import UserRequestModel, UserResponseModel


router = APIRouter()

users = [ 
        { "idusuario": 123456,
          "name":"Gabriel",
          "surname":"Garcia",
          "dni": 12345678,
          "phone": 12345645468,
          "age": 20
        },
        { "idusuario": 123457,
          "name":"Hernán",
          "surname":"Garcia",
          "dni": 12345680,
          "phone": 12345645480,
          "age": 60
        },
        { "idusuario": 123458,
          "name":"Gabriela",
          "surname":"Garcia",
          "dni": 12345679,
          "phone": 12345645469,
          "age": 40
        },
        { "idusuario": 123456,
          "name":"Gabriel",
          "surname":"Garcia",
          "dni": 12345678,
          "phone": 12345645468,
          "age": 30
        },
    ]

@router.get('/usuarios')
async def get_all_users():
    return { "users": users}

@router.get('/usuarios/{user_id}')
async def usuariosById(user_id):
    return { "param" : user_id}

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
        phone=user.phone
    )
    return UserResponseModel(
        id= user.id,
        username=user.username
    )