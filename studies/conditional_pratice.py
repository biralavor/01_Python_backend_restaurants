import os

############################################
#               Program Title              #
############################################
def title() :
  print(' >> Conditional Practice << ')

############################################
#          First Example functions         #
############################################
def first_example_ask_user_age() :
  age = input('How old are you? ')
  return age

def first_example_age_checker(age) :
  try :
      age = int(age)
      if (0 <= age <= 12) :
        print('You are a child')
      elif (13 <= age <= 18) :
        print('You are a teenager')
      elif (19 <= age <= 110) :
        print('You are an adult')
      else :
        print('You are an E.T. Sorry. We only accept humans')
  except ValueError :
      print('Only numbers are accepted')

def first_example() :
  print('\n::::::: Staring the first example :::::::::::')
  age = first_example_ask_user_age()
  first_example_age_checker(age)

############################################
#         Second Example functions         #
############################################
def second_example_ask_user_name() :
  name = input('What is your name? ')
  print('Welcome ' + name)
  return name

def second_example_ask_password() :
  password = input('What is your password? ')
  return password

def second_example_password_checker(name, password) :
  if (name == 'alura' and password == 'CaelumUpgraded') :
    print('\n>>>>>>>>>>>>>>>> Access granted')
    print('\\o/')
  else :
    print('\nXXXXXXXXXXXXXXXX Access denied')
    print('T.T')

def second_example() :
  print('\n::::::: Staring the second example :::::::::::')
  name = second_example_ask_user_name()
  password = second_example_ask_password()
  second_example_password_checker(name, password)

############################################
#          Third Example functions         #
############################################
def third_example_ask_for_x() :
  x = int(input('Enter the X coordinate: '))
  return x

def third_example_ask_for_y() :
  y = int(input('Enter the Y coordinate: '))
  return y

def thrid_example_cartesian_quadrant(x, y) :
  if (x > 0 and y > 0) :
    print('The point in Cartesian plane is in the 1st Quadrant')
  elif (x < 0 and y > 0) :
    print('The point in Cartesian plane is in the 2nd Quadrant')
  elif (x < 0 and y < 0) :
    print('The point in Cartesian plane is in the 3rd Quadrant')
  elif (x > 0 and y < 0) :
    print('The point in Cartesian plane is in the 4th Quadrant')
  else :
    print('The point in Cartesian plane is in the origin or in axis')

def third_example() :
  print('\n::::::: Staring the third example :::::::::::')
  x = third_example_ask_for_x()
  y = third_example_ask_for_y()
  thrid_example_cartesian_quadrant(x, y)


############################################
#              MAIN program                #
############################################
if __name__ == '__main__' :
  title()
  first_example()
  second_example()
  third_example()
  print('\n/////////// THIS IS THE END ///////////')
  print('The Conditional Practice program has finished')
  exit()