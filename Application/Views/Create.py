from Application.Controllers.CRUDController import CRUDController
from Application.Models.Blog import Blog
from Application.Models.Post import Post
from Application.Models.Customuser import Customuser
from Application.Models.Rate import Rate
from datetime import datetime
import os

class Create():

    @staticmethod
    def create_menu():
        clear = lambda: os.system('cls')
        while(True):
            print(' You want to: ')
            print(' 1 - Insert data into a table ')            
            print(' 0 - Back to main menu ')
            input_result = input("Your input here: ")
            if input_result == '0':
                clear()
                return
            if input_result == '1':
                table = input("Input table name: ").lower()
                print('\n')
                data = None
                if 'blog' in table:
                    fields = [key for key, value in Blog.__dict__.items() if not '__' in key]
                    values = []
                    for field in fields:
                        values.append(input('{0}='.format(field)))
                    data = {key: value for (key, value) in zip(fields, values)}

                if 'user' in table:
                    fields = [key for key, value in Customuser.__dict__.items() if not '__' in key]
                    values = []
                    for field in fields:
                        values.append(input('{0}='.format(field)))
                    data = {key: value for (key, value) in zip(fields, values)}

                if 'post' in table:
                    fields = [key for key, value in Post.__dict__.items() if not '__' in key]
                    values = []
                    for field in fields:
                        values.append(input('{0}='.format(field)))
                    data = {key: value for (key, value) in zip(fields, values)}

                if 'rate' in table:
                    fields = [key for key, value in Rate.__dict__.items() if not '__' in key]
                    values = []
                    for field in fields:
                        values.append(input('{0}='.format(field)))
                    data = {key: value for (key, value) in zip(fields, values)}
                
                if data is None:
                    print('Table does not exist')
                else:
                    df = CRUDController.create_item(table, **data)
                    print(df)
