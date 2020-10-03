# This is the Users class, to make players, currently it is set to always let the player go first
class Users:
    character: None
    first: True

# Created a new user object using the Users class
user = Users()

# This allows the user to select which character they wish to play
char = prompt('Choose a character, either X or O')

# Now, what if it is no an X or an O?  This function will check to see if the user selected either or,
# and if it is wrong, it will give an error and reprompt the user

if char != 'X' and char != 'O':
    