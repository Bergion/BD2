from Application.Manager.fields import  CharField, IntegerField, TextField, DateTimeField, ForeignKey
from Application.Manager.manager import  Model



class Rate(Model):
    id = IntegerField()
    value = CharField('value')
    post_id = ForeignKey()
    user_id = ForeignKey()