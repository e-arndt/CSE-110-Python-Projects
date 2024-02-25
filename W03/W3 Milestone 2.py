# Welcome Message
print('Welcome to the Haunted Mansion!')
print('You are a nosy kid, who is bored and wants take a walk around your new neighborhood.  You come upon this old delapidated house.')
print('Because you are nosy, you enter the house.  Shame on you!')

#Prompt user for an item choice
adventure_game = input('You are tiptoeing around a dark old house and find three items: a SOCK, a HAT and a CRAYON.  Which one do you want to pick up?')
#adventure_game_1 = 'SOCK'
#adventure_game_2 = 'HAT'
#adventure_game_3 = 'CRAYON'

if adventure_game.lower () == 'sock':
    print('You bring the sock close to your face and smell a foul odor of a person who has worn this sock for too many days in a row. Ewww!  You continue towards the BACK DOOR of the house or you chose to run back out through the FRONT DOOR.  Which one do you pick?')
 
elif adventure_game.lower () == 'hat':
    print('You notice the hat is soft to the touch, contains a brown sweat stain beneath the lid and is dusty with soft brownish dirt.  It has obviously been put to good use.  You blow the DUST OFF the hat or you place the cap on your HEAD.  Which one you pick?')

elif adventure_game.lower () == 'crayon':
    print('You pick up the crayon and begin to place it in your pocket, when you happen upon a gruesome childs drawing of an alien from outerspace!  You continue up the STAIRS or you chose to enter the LIVING ROOM.  Which one do you pick?')

    