# Author: Eric Arndt
# Class: CSE 110 W01 Prove Assignment (Mad Lib)
# Request word inputs, insert user words into an Ad Lib story
# Display that story to the user

NL               = '\n'
ESC              = '\x1b'
RED_BG           = ESC + '[41m'
NORMAL           = ESC + '[0m'
WELCOME_BANNER   = 'WELCOME TO MAD-LIB STORIES'
STORY_BANNER     = "HERE'S YOUR STORY... "
NO_STORY         = 'NO STORY SELECTED... BYE'
END              = '        THE END.        '

print(RED_BG + WELCOME_BANNER.center(50,' ') + NORMAL + NL)



choose = input('Do you want story A or story B [A/B]? ')

if (choose == "A" or choose == "a"):

    print(NL + NORMAL + 'Please enter the following: ' + choose + NL)

    adj_A1 = input('Adjective: ')
    animal_A1 = input('Animal: ')
    verb_A1    = input('Verb: ')
    exclam_A1  = input('Exclamation: ')
    verb_A2 = input('Verb: ')
    verb_A3    = input('Verb: ')
    print(NL)


    StoryA1_1  = f'The other day, I was really in trouble.'
    StoryA1_2  = f'It all started when I saw a very {adj_A1.lower()} {animal_A1.lower()} {verb_A1.lower()} down the hallway.'
    StoryA1_3  = f'{exclam_A1.capitalize()}! I yelled. '
    StoryA1_4  = f'But all I could think to do was to {verb_A2.lower()} over and over.'
    StoryA1_5  = f'Miraculously, that caused it to stop, '
    StoryA1_6  = f'but not before it tried to {verb_A3.lower()} right in front of my family.'



    print(RED_BG + STORY_BANNER.center(50,' ') + NORMAL + NL)

    print(StoryA1_1 + NL + StoryA1_2 + NL + StoryA1_3 + StoryA1_4 + NL + StoryA1_5 + NL + StoryA1_6 + NL)

    print(RED_BG + END.center(50,' ') + NORMAL + NL)



elif (choose == "B" or choose == "b"):

    print(NL + NORMAL + 'Please enter the following: ' + choose + NL)

    name_B1    = input('Last Name: ')
    silly_B1   = input('Silly word: ')
    num_B1     = input('Number: ')
    adj_B1     = input('Adjective: ')
    noun_B1    = input('Noun: ')
    adj_B2     = input('Adjective: ')
    rel_B1     = input('A Relative: ')
    adj_B3     = input('Adjective: ')
    verb_B1    = input('Verb: ')
    adj_B4     = input('Adjective: ')
    adj_B5     = input('Adjective: ')
    print(NL)


    StoryB2_1  = f'Hello, my name is astronaut {name_B1.capitalize()}.'
    StoryB2_2  = f'I am on my way to planet {silly_B1.capitalize()}.'
    StoryB2_3  = f'I will be gone for {num_B1} days.'
    StoryB2_4  = f'I am very {adj_B1.lower()} about the trip, but I will miss my {noun_B1}.'
    StoryB2_5  = f'I have heard that the atmosphere there is {adj_B2.lower()}.'
    StoryB2_6  = f'Luckily my {rel_B1.lower()} packed me a jacket to keep me {adj_B3.lower()}.'
    StoryB2_7  = f'When I land on the planet, I will {verb_B1.lower()} for joy.'
    StoryB2_8  = f'I am {adj_B4.lower()} to walk on another planet.'
    StoryB2_9  = f'I could not be more {adj_B5.lower()} for this trip.'



    print(RED_BG + STORY_BANNER.center(50,' ') + NORMAL + NL)

    print(StoryB2_1 + NL + StoryB2_2 + NL + StoryB2_3 + NL + StoryB2_4 + NL + StoryB2_5 + NL + StoryB2_6 + NL 
              + StoryB2_7 + NL + StoryB2_8 + NL + StoryB2_9 + NL)

    print(RED_BG + END.center(50,' ') + NORMAL + NL)


else:
    print(NL + RED_BG + NO_STORY.center(50,' ') + NORMAL + NL)