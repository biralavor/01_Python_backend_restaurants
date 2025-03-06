from containers.restaurants_db import RestaurantsDB
from containers.clear import ClearAll
from containers.callbacks import CallBacks

###################################################
#             GLOBAL VARIABLES                    #
###################################################
call_menu_flag = True

class Operations:
###################################################
#             CHOSEN OPERATION                    #
###################################################
  @staticmethod
  def chosen_operation(userinput, restaurants, next_operation) :
    if userinput is None:
        return
    match userinput :
      case 1 :
        RestaurantsDB.list_all_restaurants(restaurants, call_menu_flag,next_operation)
      case 2 :
        RestaurantsDB.add_new_restaurant(restaurants, next_operation)
      case 3 :
        RestaurantsDB.remove_restaurant(restaurants, next_operation)
      case 4 :
        RestaurantsDB.activate_restaurant(restaurants,next_operation)
      case 5 :
        ClearAll.clear_all_and_quit()
      case _ :
        raise ValueError('Invalid option')
    return restaurants