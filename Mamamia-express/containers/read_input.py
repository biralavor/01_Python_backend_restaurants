from containers.errors import AppErrors

class ReadInput:
###################################################
#             READ USER INPUT                     #
###################################################
  def read_user_input() :
    userinput = input('Choose an option: ')
    try :
      userinput = int(userinput)
    except ValueError :
      AppErrors.illegal_choice()
    return userinput
