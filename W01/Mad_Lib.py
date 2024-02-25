# Author: Eric Arndt
# Class: CSE 110 W01 Prove Assignment (Mad Lib)
# Request word inputs, insert user words into an Ad Lib story
# Display that story to the user

NL               = '\n'
ESC              = '\x1b'
WHITE_FG         = ESC + '[37m'
CYAN_FG          = ESC + '[36m'
RED_BG           = ESC + '[41m'
RED_FG           = ESC + '[31m'
YELLOW_BG        = ESC + '[43m'
YELLOW_FG        = ESC + '[33m'
GREEN_BG         = ESC + '[42m'
GREEN_FG         = ESC + '[32m'
BLUE_BG          = ESC + '[44m'
BLUE_FG          = ESC + '[34m'
PURPLE_BG        = ESC + '[45m'
PURPLE_FG        = ESC + "[35m"
NORMAL           = ESC + '[0m'
WELCOME_BANNER   = 'WELCOME TO MAD-LIB STORIES'
STORY_BANNER     = "HERE'S YOUR STORY... "
END              = '       THE END.      '

print(RED_BG + WELCOME_BANNER.center(50,' ') + NORMAL + NL)

print(NORMAL + 'Please enter the following: ' + NL)
adj1 = input('Adjective: ')
animal1 = input('Animal: ')
verb1 = input('Verb: ')
exclam1 = input('Exclamation: ')
verb2 = input('Verb: ')
verb3 = input('Verb: ')
print(NL)


S1_1             = f'The other day, I was really in trouble.'
S1_2             = f'It all started when I saw a very {adj1.lower()} {animal1.lower()} {verb1.lower()} down the hallway.'
S1_3             = f'{exclam1.capitalize()}! I yelled. '
S1_4             = f'But all I could think to do was to {verb2.lower()} over and over.'
S1_5             = f'Miraculously, that caused it to stop, '
S1_6             = f'but not before it tried to {verb3.lower()} right in front of my family.'
STORY            = S1_1 + S1_2 + S1_3 + S1_4 + S1_5 + S1_6


print(RED_BG + STORY_BANNER.center(50,' ') + NORMAL + NL)
print(STORY)
print(RED_BG + END.center(50,' ') + NORMAL + NL)