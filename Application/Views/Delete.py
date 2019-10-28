from Application.Controllers.CRUDController import CRUDController
from Application.Models.Blog import Blog
from Application.Models.Post import Post
from Application.Models.Customuser import Customuser
from Application.Models.Rate import Rate
from datetime import datetime
import os



class Delete():

    @staticmethod
    def delete_menu():
        clear = lambda: os.system('cls')
        while(True):
            print(' You want to: ')
            print(' 1 - Delete all data ')            
            print(' 2 - Delete data from specific table ')            
            print(' 3 - Delete item (specified by id) ')            
            print(' 0 - Back to main menu ')

            input_result = input("Your input here: ")
            if input_result == '0':
                clear()
                return
            if input_result == '1':
                clear()
                print(' Removing...\n\n\n')
                status = CRUDController.clear_database()    
                print(status)
            if input_result == '2':
                clear()
                table = input("Input table name:")
                status = CRUDController.clear_table(table)
                print(status)