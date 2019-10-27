from Application.manager import Model, CharField, IntegerField, TextField, DateTimeField, ForeignKey




class Rate(Model):
    id = IntegerField()
    value = CharField()
    post_id = ForeignKey()
    user_id = ForeignKey()