
###################################################
#                MENU FUCNTIONS                   #
###################################################
class Menu:
  @staticmethod
  def title() :
    print('┳┳┓          •    ┳┓  ┓•        ')
    print('┃┃┃┏┓┏┳┓┏┓┏┳┓┓┏┓  ┃┃┏┓┃┓┓┏┏┓┏┓┓┏')
    print('┛ ┗┗┻┛┗┗┗┻┛┗┗┗┗┻  ┻┛┗ ┗┗┗┛┗ ┛ ┗┫')
    print('                               ┛')

  @staticmethod
  def show_menu() :
    print('1. List All Restaurants')
    print('2. Add new Restaurant')
    print('3. Remove a Restaurant')
    print('4. Activate a Restaurant')
    print('5. Quit\n')
