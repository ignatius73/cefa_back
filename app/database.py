from decouple import config
from peewee import *
from playhouse.postgres_ext import *

db = PostgresqlExtDatabase(
    'cefa-db', 
    user=config('PSQLUSER'), 
    password=config('PSQLPASS'),
    host=config('PSQLHOST'),
    port=config('PSQLPORT'))

print(config('PSQLUSER'))


class BaseModel(Model):
    class Meta:
        database = db

