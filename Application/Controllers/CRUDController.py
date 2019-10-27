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