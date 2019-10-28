from Application.Controllers.CRUDController import CRUDController
from datetime import datetime
import os

class Read():

    @staticmethod
    def read_menu():
        clear = lambda: os.system('cls')
        while(True):
            print(' You want to: ')
            print(' 1 - Read all data from all tables ')            
            print(' 2 - Read all data from specific table ')
            print(' 3 - Task 3')
            print(' 4 - Full text search ')
            print(' 0 - Back to main menu ')
            input_result = input("Your input here: ")
            if input_result == '0':
                clear()
                return
            if input_result == '1':
                clear()
                tables = CRUDController.get_all()
                for key, value in tables.items():
                    if len(value) == 0:
                        print(' {0} table is empty '.format(key)) 
                    else:
                        print('social_network_' + key + " table\n__________________________________________________________________________________________\n")
                        print(value, '\n\n\n')

            if input_result == '2':
                clear()
                table = input("Input table name: ")
                print('\n')
                df = CRUDController.get_all_from_table(table)
                if len(df) == 0:
                   print(' Table is empty ') 
                else:
                    print(df, '\n\n\n')

            if input_result == '3':
                clear()
                bool_value = input("Input bool value: ")
                string_list = input("Input words : ").split(',')
                df = CRUDController.task3(bool_value, string_list)
                if len(df) == 0:
                   print(' No such rows ') 
                else:
                    print(df, '\n\n\n')

            if input_result == '4':
                clear()
                print(' 1 - Search by word: ')
                print(' 2 - Exclude word: ')
                input_result = input("Your input here: ")

                if input_result == '1':
                    table = input("Input table name: ")
                    attribute = input("Input attribute name: ")
                    text = input('Input word: ')
                    df = CRUDController.full_text_search(table, attribute, text)
                    if len(df) == 0:
                        print(' No such rows ') 
                    else:
                        print(df, '\n\n\n')
                
                if input_result == '2':
                    table = input("Input table name: ")
                    attribute = input("Input attribute name: ")
                    text = input('Input word: ')
                    df = CRUDController.full_text_search_exclude(table, attribute, text)
                    if len(df) == 0:
                        print(' No such rows ') 
                    else:
                        print(df, '\n\n\n')

                
