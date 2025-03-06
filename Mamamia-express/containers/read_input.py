from containers.errors import AppErrors

class ReadInput:
###################################################
#             READ USER INPUT                     #
###################################################
  def read_user_input() :
    while True:
      userinput = input('Choose an option: ')
      try :
        userinput = int(userinput)
        return userinput
      except ValueError :
        AppErrors.illegal_choice()
