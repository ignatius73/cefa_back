from datetime import datetime
import hashlib
from peewee import *
from .database import db

class User(Model):
    id=AutoField()
    username= CharField(max_length=80,unique=True)
    password= CharField(max_length=100)
    name= CharField(max_length=180)
    surname= CharField(max_length=180)
    dni= IntegerField()
    phone= IntegerField()
    photoUrl=TextField()
    created_at= DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'users'

    @classmethod
    def create_password(cls,password):
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        return hash.hexdigest()
