# Hello fellow programer, for my Python Final at Sophia, I decided to code a Password Generator,
# I decided to code this project after I had my password stolen online, so this concept hits close to home
# I really hope you enjoy the program and you can also get some potential uses from it. Enjoy!

# these import functions below are built into replt that allows us to access features on while running replit
import string
import random

# This is the beginning of where the user would get asked
# what would you like your random password length to be

length = int(input('How many characters would you like your password to be: '))

# this is where the user is asked what type of special characters they would like in their password, they can choose one or all of them for the final password
print(
  '''Below you can decide what special characters will be generated in your password, you can use more than 1 feature in your password :
         1. Letters of Alphabet
         2. Numbers
         3. Special characters
         4. Exit''')

# this is used to combine the random characters that are generated from the character lists
characterList = " "
# This is the part of the program that would use the input from the choices above to determine
# which character is going to be used for each spot in the password
while (True):
  choice = int(input('Pick a number: '))

  # if the user picks the number 1 this if statement will generate upper and lower case letters to use
  if (choice == 1):
    characterList += string.ascii_letters

# if the user picks the number 2 this if statement will generate digits to to use
  elif (choice == 2):
    characterList += string.digits

# if the user picks the number 3 this if statement will generate special characters to use
  elif (choice == 3):
    characterList += string.punctuation

# if the user picks the number 4 this will stop running the program
  elif (choice == 4):
    break

# if the user pick any other number than 4 then they receive the error message to pick an int 1-4
  else:
    print(' Please pick a valid number between 1-4! ')

# this is used to show the generated password after the user makes their choices
password = []

# this part is to help determine the length range or legth of the password that is generated
for i in range(length):

  # this is where a random character is imported from replits random choice function
  randomchar = random.choice(characterList)

  # this is where we start tp append our random characters together
  password.append(randomchar)

# this is where the final password that is generated and combined as a string this is also the farewell to the end of the code and where the user is asked if they like it or not with the option to regenerate a password
print(' Your random generated password is: ' + "".join(password))

print(
  'I hope you like your new random generated password. If you do not, please generate another one! '
)
