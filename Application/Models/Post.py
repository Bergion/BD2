from Application.Manager.fields import  CharField, IntegerField, TextField, DateTimeField, ForeignKey
from Application.Manager.manager import  Model

class Post(Model):
    id = IntegerField()
    title = CharField('title')
    content = TextField('content')
    pub_date = DateTimeField()
    blog_id = ForeignKey()