#!/usr/bin/python3

import os
from containers.menu import Menu
from containers.read_input import ReadInput
from containers.chosen_operation import Operations

def operation_init(userinput, restaurants):
    Operations.chosen_operation(userinput, restaurants, operation_init)

if __name__ == "__main__" :
  restaurants = []
  os.system('clear')
  Menu.title()
  Menu.show_menu()
  userinput = ReadInput.read_user_input()
  operation_init(userinput, restaurants)