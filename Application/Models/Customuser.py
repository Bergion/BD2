from Application.Manager.fields import  CharField, IntegerField, BoolField
from Application.Manager.manager import  Model

class Customuser(Model):
    id = IntegerField()
    password = CharField('password')
    is_superuser = BoolField()
    username = CharField('username')
    first_name = CharField('first_name')
    last_name = CharField('last_name')
    email = CharField('email')
