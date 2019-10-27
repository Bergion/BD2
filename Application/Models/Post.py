from Application.manager import Model, CharField, IntegerField, TextField, DateTimeField, ForeignKey


class Post(Model):
    id = IntegerField()
    title = CharField()
    content = TextField()
    pub_date = DateTimeField()
    blog_id = ForeignKey()