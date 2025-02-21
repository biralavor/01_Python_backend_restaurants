import os

restaurants = []
call_menu_flag = True

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

def remove_restaurant() :
  list_all_restaurants(False)
  chosen_res = input('\nWhich of them do you want to remove? ')
  try :
    chosen_res = int(chosen_res)
    print('Now removing: ')
    match chosen_res :
      case 1 :
        print(f'{restaurants[0]}')
        restaurants.pop(0)
      case 2 :
        print(f'{restaurants[1]}')
        restaurants.pop(1)
      case 3 :
        print(f'{restaurants[2]}')
        restaurants.pop(2)
      case 4 :
        print(f'{restaurants[3]}')
        restaurants.pop(3)
      case _ :
        print('Invalid option')
    print('\n')
    list_all_restaurants(True)
  except ValueError :
    illegal_choice()

def activate_restaurant() :
  print('Let\'s activate a Restaurant:')

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

def clear_all_and_quit():
  os.system('clear')
  print('Goodbye!')
  exit()

def main() :
  os.system('clear')
  title()
  show_menu()
  read_first_user_input()

if __name__ == '__main__' :
  main()