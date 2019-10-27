from Application.manager import Model, CharField, IntegerField, BoolField


class Customuser(Model):
    id = IntegerField()
    password = CharField()
    is_superuser = BoolField()
    username = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
