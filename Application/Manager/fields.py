import psycopg2
from Application.settings import CONNECTION_STRING
import pandas as pd

class Field():

    def __init__(self, column=None):
        self.column = column
        self.table = None

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def fulltext_search_word(self, string):
        command = """SELECT id, ts_headline({0}, q)
                    FROM (SELECT * FROM {1}, to_tsquery(%s) q
                    WHERE to_tsvector({0}) @@ q) AS foo""".format(self.column, self.table)
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command, (string, ))
                except psycopg2.Error as e:
                    return e.pgerror
                data = cursor.fetchall()
                df = pd.DataFrame(data=data, columns=['id', 'ts_headline'])
                df.set_index(['id'], inplace=True)
                return df
    
    def exclude_word(self, string):
        command = """SELECT id, ts_headline({0}, q)
                    FROM (SELECT * FROM {1}, to_tsquery(%s) q
                    WHERE NOT to_tsvector({0}) @@ q) AS foo""".format(self.column, self.table)
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command, (string, ))
                except psycopg2.Error as e:
                    return e.pgerror
                data = cursor.fetchall()
                df = pd.DataFrame(data=data, columns=['id', 'ts_headline'])
                df.set_index(['id'], inplace=True)
                return df

class ForeignKey(Field):
    pass

class CharField(Field):
    pass

class DateTimeField(Field):
    pass

class TextField(Field):
    pass

class IntegerField(Field):
    pass

class BoolField(Field):
    pass

