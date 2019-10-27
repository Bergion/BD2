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
            print(' 0 - Back to main menu ')
            input_result = input("Your input here: ")
            if input_result == '0':
                clear()
                return
            if input_result == '2':
                table = input("Input table name: ")
                print('\n')
                df = CRUDController.get_all_from_table(table)
                if len(df) == 0:
                   print(' Table is empty ') 
                else:
                    print(df, '\n\n\n')


                
