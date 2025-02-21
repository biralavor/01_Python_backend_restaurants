import os

###################################################
#             GLOBAL VARIABLES                    #
#  (I'll remove them as soon as I learn how to)   #
###################################################
restaurants = []
call_menu_flag = True

###################################################
#                MENU FUCNTIONS                   #
###################################################
def title() :
  print('┳┳┓          •    ┳┓  ┓•        ')
  print('┃┃┃┏┓┏┳┓┏┓┏┳┓┓┏┓  ┃┃┏┓┃┓┓┏┏┓┏┓┓┏')
  print('┛ ┗┗┻┛┗┗┗┻┛┗┗┗┗┻  ┻┛┗ ┗┗┗┛┗ ┛ ┗┫')
  print('                               ┛')

def show_menu() :
  print('1. List All Restaurants')
  print('2. Add new Restaurant')
  print('3. Remove a Restaurant')
  print('4. Activate a Restaurant')
  print('5. Quit\n')

def callback_menu() :
  input('\nPress Enter to go back to Menu...')
  os.system('clear')
  main()

def illegal_choice() :
  print('\nError. Only numbers are accepted')
  print('Try again!')

###################################################
#             LIST ALL RESTAURANTS                #
###################################################
def list_all_restaurants(call_menu_flag) :
  index = 1
  if len(restaurants) == 0:
    print('\n<<<<<< No restaurants added yet! >>>>>>')
  else:
    print('Here is the actual Restaurants\'s List:')  
    for restaurant in restaurants:
      print(f'{index}. {restaurant}')
      index += 1
  if call_menu_flag == True :
    callback_menu()

###################################################
#             ADD RESTAURANTS                     #
###################################################
def add_new_restaurant() :
  print('\n|||| Let\'s add a new Restaurant ||||')
  new_rest = input('\nRestaurant name: ')
  restaurants.append(new_rest)
  print(f'Restaurant called {new_rest} added successfully!')
  another = input('\nDo you want to add another one? (y/n) ')
  if another == 'y' :
    add_new_restaurant()
  else :
    callback_menu()

###################################################
#             REMOVE RESTAURANTS                  #
###################################################
def remove_restaurant() :
  list_all_restaurants(False)
  if len(restaurants) == 0:
    print('You need to add a restaurant first!')
    callback_menu()
  else :
    chosen_res = input('\nWhich of them do you want to remove? ')
    try :
      chosen_res = int(chosen_res)
      if 1<= chosen_res <= len(restaurants) :
        print('Now removing: ')
        print(f'{restaurants[chosen_res - 1]}')
        restaurants.pop(chosen_res - 1)
      else :
        print('Invalid option')
      print('\n')
      list_all_restaurants(True)
    except ValueError :
      illegal_choice()

###################################################
#             ACTIVATE RESTAURANTS                #
###################################################
def activate_restaurant() :
  print('Let\'s activate a Restaurant:')

###################################################
#             READ USER INPUT                     #
###################################################
def read_first_user_input() :
  userinput = input('Choose an option: ')
  try :
    userinput = int(userinput)
    match userinput :
      case 1 :
        list_all_restaurants(True)
      case 2 :
        add_new_restaurant()
      case 3 :
        remove_restaurant()
      case 4 :
        activate_restaurant()
      case 5 :
        clear_all_and_quit()
      case _ :
        raise ValueError('Invalid option')
  except ValueError :
    illegal_choice()

###################################################
#             CLEAR FUNCTION                      #
###################################################
def clear_all_and_quit():
  os.system('clear')
  print('Goodbye!')
  exit()

###################################################
#                   MAIN                          #
###################################################
def main() :
  os.system('clear')
  title()
  show_menu()
  read_first_user_input()

if __name__ == '__main__' :
  main()