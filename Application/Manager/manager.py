import psycopg2
from Application.settings import CONNECTION_STRING
import pandas as pd


class Model():
    
    def __init__(self):
        attrs = [key for key, value in type(self).__dict__.items() if not '__' in key]
        for attr in attrs:
            setattr(type(self).__dict__[attr], 'table', 'social_network_{0}'.format(type(self).__name__.lower()))

    def create_single(self, **kwargs):
        command = "INSERT INTO social_network_{0}({1}) VALUES (".format(type(self).__name__.lower(), ','.join(kwargs.keys()))
        command += '%s,' * len(kwargs.values())
        command = command[:-1] + ')'
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command, list(kwargs.values()))
                except psycopg2.Error as e:
                    return e.pgerror
                return 'Created'
    
    def get_all(self):
        command = "SELECT * FROM social_network_{0}".format(type(self).__name__.lower())
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command)
                except psycopg2.Error as e:
                    return e.pgerror
                columns = [key for key, value in type(self).__dict__.items() if not '__' in key]
                data = cursor.fetchall()
                df = pd.DataFrame(data=data, columns=columns)
                df.set_index(['id'], inplace=True)
                return df

    def update(self, **kwargs):
        command = "UPDATE social_network_{0} SET ".format(type(self).__name__.lower())
        try:
            ID = kwargs.pop('id') 
        except KeyError:
            ID = None
        for key, value in kwargs.items():
            command += "{0}=%s,".format(key)
        var = list(kwargs.values())
        command = command[:-1]
        if ID is not None:
            command += " WHERE id=%s"
            var.append(ID)

        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command, var)
                except psycopg2.Error as e:
                    return e.pgerror
                return 'Updated'
    
    def delete_all(self):
        command = "DELETE FROM social_network_{0}".format(type(self).__name__.lower())
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                connection.autocommit = True
                try:
                    cursor.execute(command)
                except psycopg2.Error as e:
                    return e.pgerror
                return 'Deleted'
                

        
