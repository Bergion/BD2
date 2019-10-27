from Application.Controllers.CRUDController import CRUDController
from datetime import datetime
import os

class Update():

    @staticmethod
    def update_menu():
        clear = lambda: os.system('cls')
        while(True):
            print(' You want to: ')
            print(' 1 - Update all data in specific table ')            
            print(' 2 - Update item specified by id ')
            print(' 0 - Back to main menu ')
            input_result = input("Your input here: ")
            if input_result == '0':
                clear()
                return
            if input_result == '1':
                clear()
                table = input("Input table name: ")
                print('\n')
                fields = input("Input fields you want to update: ")
                values = input("Input values: ")
                to_update = {key: value for (key, value) in zip(fields.split(','), values.split(','))}
                df = CRUDController.update(table, **to_update)
                print(df, '\n\n\n')

            if input_result == '2':
                clear()
                table = input("Input table name: ")
                print('\n')
                ID = input("Input id: ")
                fields = input("Input fields you want to update: ")
                values = input("Input values: ")
                if values and fields and ID:
                    to_update = {key: value for (key, value) in zip(fields.split(','), values.split(','))}
                    to_update['id'] = ID
                    df = CRUDController.update(table, **to_update)
                    print(df, '\n\n\n')
                else:
                    print("Wrong Input :( \n")


                
