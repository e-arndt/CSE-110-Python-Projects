# CREATIVITY: The story was extended along with additional user word inputs.
# Red Welcome, Story and End "banners" were added to dress-up the output.

# Author: Eric Arndt
# Class: CSE 110 W01 Prove Assignment (Mad Lib)
# Request word inputs, insert user words into an Ad Lib story
# Display that story to the user


# Set static variables
NEW_LINE         = '\n'
ESC              = '\x1b'
RED_BG           = ESC + '[41m'
NORMAL_TEXT      = ESC + '[0m'
WELCOME_BANNER   = 'WELCOME TO CLEVER STORIES'
STORY_BANNER     = "HERE'S YOUR STORY... "
END_BANNER       = '       THE END.      '


# Welcome "banner": Set background color to Red, Print welcome message in center, 
# return colors to normal, add a New Line for spacing.
print(RED_BG + WELCOME_BANNER.center(50,' ') + NORMAL_TEXT + NEW_LINE)


# Display prompt asking user to enter responses to the following input requests.
# Make sure text is set to Normal, display message, add a New Line.
print(NORMAL_TEXT + 'Please enter the following: ' + NEW_LINE)


# Variables set for input from user.
# Variable name, input prompt, description of type of input requested.
adj1    = input('Adjective: ')
animal1 = input('Animal: ')
verb1   = input('Verb: ')
exclam1 = input('Exclamation: ')
verb2   = input('Verb: ')
verb3   = input('Verb: ')
exclam2 = input('Exclamation: ')
sound1  = input('A Sound: ')
verb4   = input('Verb: ')
verb5   = input('Verb: ')


# Story sentences assigned to variables
# Variable name, (f)function allowing user input variables to be added to text of story.
STORY1_1  = 'The other day, I was really in trouble.'
STORY1_2  = f'It all started when I saw a very {adj1.lower()} {animal1.lower()} {verb1.lower()} down the hallway.'
STORY1_3  = f'{exclam1.capitalize()}! I yelled. '
STORY1_4  = f'But all I could think to do was to {verb2.lower()} over and over.'
STORY1_5  = 'Miraculously, that caused it to stop, '
STORY1_6  = f'but not before it tried to {verb3.lower()} right in front of my family.'
STORY1_7  = f'My family yelled "{exclam2.capitalize()}!" at the {adj1.lower()} {animal1.lower()}.'
STORY1_8  = f'The {animal1.lower()} just ignored them as it let out a loud {sound1.lower()}.'
STORY1_9  = f'My family and I watched in complete {verb4.lower()} as the {adj1.lower()} {animal1.lower()}'
STORY_10  = f'calmly {verb5.lower()} out the door.'


# Story "banner" displayed at begining of Story.
print(NEW_LINE + RED_BG + STORY_BANNER.center(50,' ') + NORMAL_TEXT + NEW_LINE)


# First story sentence displayed, New Line, second sentence displayed... until enitre story is displayed to user.
print(STORY1_1 + NEW_LINE + STORY1_2 + NEW_LINE + STORY1_3 + STORY1_4 + NEW_LINE + STORY1_5 + STORY1_6)
print(STORY1_7 + NEW_LINE + STORY1_8 + NEW_LINE + STORY1_9 + NEW_LINE + STORY_10 + NEW_LINE)


# Ending "banner" dispalyed at end of story.
print(RED_BG + END_BANNER.center(50,' ') + NORMAL_TEXT + NEW_LINE)
