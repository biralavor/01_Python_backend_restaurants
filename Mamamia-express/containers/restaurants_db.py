from containers.errors import AppErrors
from containers.callbacks import CallBacks

class RestaurantsDB :
###################################################
#             LIST ALL RESTAURANTS                #
###################################################
  @staticmethod
  def list_all_restaurants(restaurants, call_menu_flag, next_operation) :
    index = 1
    if not restaurants :
      print('\n<<<<<< No restaurants added yet! >>>>>>')
    else:
      print('Here is the actual Restaurants\'s List:')
      for restaurant in restaurants:
        print(f'{index}. {restaurant}')
        index += 1
    if call_menu_flag == True :
      CallBacks.callback_menu(restaurants, next_operation)

###################################################
#             ADD RESTAURANTS                     #
###################################################
  @staticmethod
  def add_new_restaurant(restaurants, next_operation) :
    print('\n|||| Let\'s add a new Restaurant ||||')
    new_rest = input('\nRestaurant name: ')
    restaurants.append(new_rest)
    print(f'Restaurant called {new_rest} added successfully!')
    another = input('\nDo you want to add another one? (y/n) ')
    if another == 'y' :
      RestaurantsDB.add_new_restaurant(restaurants, next_operation)
    else :
      CallBacks.callback_menu(restaurants, next_operation)
    return restaurants

###################################################
#             REMOVE RESTAURANTS                  #
###################################################
  @staticmethod
  def remove_restaurant(restaurants, next_operation) :
    RestaurantsDB.list_all_restaurants(restaurants, False, next_operation)
    if not restaurants :
      print('You need to add a restaurant first!')
      return restaurants
    else :
      while True :
        chosen_res = input('\nWhich of them do you want to remove? ')
        try :
          chosen_res = int(chosen_res)
          if 1 <= chosen_res <= len(restaurants) :
            print('Now removing: ')
            print(f'{restaurants[chosen_res - 1]}')
            restaurants.pop(chosen_res - 1)
          else :
            print('Invalid option')
          print('\n')
          RestaurantsDB.list_all_restaurants(restaurants, True, next_operation)
          return restaurants
        except ValueError :
          AppErrors.illegal_choice()
          return restaurants

###################################################
#             ACTIVATE RESTAURANTS                #
###################################################
  @staticmethod
  def activate_restaurant(restaurants, next_operation) :
    print('Let\'s activate a Restaurant:')
    CallBacks.callback_menu(restaurants, next_operation)
    return restaurants
