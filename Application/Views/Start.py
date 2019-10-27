from Application.Controllers.StartController import StartController
from Application.Views.Read import Read
from Application.Views.Update import Update
from Application.Views.Create import Create
from Application.Views.Delete import Delete
from datetime import datetime
import os

class Start():

    @staticmethod
    def main_menu():
        clear = lambda: os.system('cls')
        while(True):
            print(' You want to: ')
            print(' 1 - List all avaliable tables ')
            print(' 2 - Read data ')
            print(' 3 - Update data ')
            print(' 4 - Create data ')
            print(' 5 - Delete data ')
            print(' 6 - Seed data ')
            print(' 0 - exit')

            input_result = input("Your input here: ")
            if input_result == '0':
                break
            if input_result == '1':
                clear()
                Start.avaliable_tables()
            if input_result == '2':
                clear()
                Read.read_menu()
            if input_result == '3':
                clear()
                Update.update_menu()
            if input_result == '4':
                clear()
                Create.create_menu()
            
            if input_result == '5':
                clear()
                Delete.delete_menu()
            
            if input_result == '6':
                clear()
                print(' Seeding data pls w8...\n\n\n')
                StartController.seed_data()

    @staticmethod
    def avaliable_tables():
        print('\n\n')
        print('table_name\n_____________________________________________\n')
        for row in StartController.get_tables_list():
            print(row, '\n')