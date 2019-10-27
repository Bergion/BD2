from Application.manager import Model, IntegerField, CharField, DateTimeField, ForeignKey


class Blog(Model):
    id = IntegerField()
    name = CharField()
    created = DateTimeField()
    user_id = ForeignKey()