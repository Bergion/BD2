from Application.Manager.fields import IntegerField, CharField, DateTimeField, ForeignKey
from Application.Manager.manager import  Model

class Blog(Model):
    id = IntegerField()
    name = CharField('name')
    created = DateTimeField()
    user_id = ForeignKey()