import os
from containers.menu import Menu
from containers.read_input import ReadInput

class CallBacks:
###################################################
#                 CALLBACK MENU                   #
###################################################
  @staticmethod
  def callback_menu(restaurants, next_operation) :
    input('\nPress Enter to go back to Menu...')
    os.system('clear')
    Menu.title()
    Menu.show_menu()
    userinput = ReadInput.read_user_input()
    next_operation(userinput, restaurants)