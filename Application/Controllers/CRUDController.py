import psycopg2
from Application.settings import CONNECTION_STRING
from Application.Models.Blog import Blog
from Application.Models.Post import Post
from Application.Models.Customuser import Customuser
from Application.Models.Rate import Rate
import pandas as pd
import types


class CRUDController():

    @staticmethod
    def get_table_or_false(table):
        if 'blog' in table.lower():
            blog_table = Blog()
            return blog_table

        if 'user' in table.lower():
            user_table = Customuser()
            return user_table

        if 'post' in table.lower():
            post_table = Post()
            return post_table

        if 'rate' in table.lower():
            rate_table = Rate()
            return rate_table

        return False

    @staticmethod
    def create_item(table, **kwargs):
        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'    
        return table.create_single(**kwargs)

    @staticmethod
    def get_all_from_table(table):

        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'    
        return table.get_all()
    
    @staticmethod
    def get_all():
        return {'customuser': CRUDController.get_all_from_table('user'),
                'blog': CRUDController.get_all_from_table('blog'),
                'post': CRUDController.get_all_from_table('post'),
                'rate': CRUDController.get_all_from_table('rate')}

    @staticmethod
    def task3(bool_value, string_list):
        cmd = """SELECT * FROM social_network_customuser 
                        INNER JOIN social_network_blog ON social_network_customuser.id = social_network_blog.user_id
                        WHERE is_superuser=%s AND (""" + ("name ILIKE %s OR " * len(string_list))
        cmd = cmd[:-3] + ')'
        string_list = ['%{}%'.format(string) for string in string_list]
        string_list.insert(0, bool_value)
        with psycopg2.connect(CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(cmd, (string_list))
                except psycopg2.Error as e:
                    return e.pgerror
                columns = [key for key, value in Customuser.__dict__.items() if not '__' in key]
                columns.extend([key for key, value in Blog.__dict__.items() if not '__' in key])
                data = cursor.fetchall()
                df = pd.DataFrame(data=data, columns=columns)
                return df

    @staticmethod
    def full_text_search(table, attribute, text):
        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'  
        df = type(table).__dict__[attribute].fulltext_search_word(text)
        return df

    @staticmethod
    def full_text_search_exclude(table, attribute, text):
        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'  
        df = type(table).__dict__[attribute].exclude_word(text)
        return df

    @staticmethod
    def update(table, **kwargs):

        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'    
        return table.update(**kwargs)

    
    @staticmethod
    def clear_database():
        user_table = Customuser()
        return user_table.delete_all()

    @staticmethod
    def clear_table(table):

        table = CRUDController.get_table_or_false(table)
        if isinstance(table, bool):
            return 'Table does not exist'    
        return table.delete_all()