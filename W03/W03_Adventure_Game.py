# Author: Eric Arndt
# Class: CSE 110 W03 Adventure Game
# 
# 

import os
import time


new_line            = '\n'
esc                 = '\x1b'
red_bd              = esc + '[41m'
normal              = esc + '[0m'
welcome_banner      = 'WELCOME TO TEXT ADVENTURES'
end_banner          = 'THE END '
die_banner          = 'YOU DIED... THE END'
inv                 = 0
pocket              = ''
room                = 'R1'
living_room_banner  = 'LIVING ROOM'
instruction_banner  = 'INSTRUCTIONS'
kitchen_banner      = 'KITCHEN'
backyard_banner     = 'BACKYARD'
bathroom_banner     = 'BATHROOM'
bedroom_banner      = 'BEDROOM'
die_banner          = "YOU'RE DEAD!"
tree_banner         = 'TREE'
branch_banner       = 'WEAK BRANCH'
road_banner         = 'DIRT ROAD'
shed_banner         = 'TOOL SHED'
closet_banner       = 'CLOTHES CLOSET'
road2_banner        = 'LONG DIRT ROAD'
grove_banner        = 'LARGE GROVE OF TREES'
grassy_banner       = 'LARGE GRASSY FIELD'
ship_banner         = 'METALIC SAUCER SPACESHIP'
ship_entry_banner   = 'DARK SHIP CORRIDOR'
the_end_banner      = 'THE END OF YOUR ADVENTURE'
com_center_banner   = "SHIP'S COMMAND CENTER"
eng_room_banner     = 'ENGINEERING ROOM'

def instruct():
    os.system('cls')
    print(red_bd + instruction_banner.center(50,' ') + normal + new_line)
    print('Use the words in all CAPS to perform actions.')
    print('Also can use the first letter of any all CAPS word.')
    print('Exapmle r for RUN or d for DOOR.')
    print('Both Upper or Lower case will work.')
    print(new_line)
    input('Press Enter key when ready to continue: ')
    living_room()
    
def the_end():
    global inv
    global pocket
    os.system('cls')
    print(red_bd + the_end_banner.center(50,' ') + normal + new_line)
    time.sleep(2)
    print('Congratulations! You made it to The End.')
    run = (input('Play again? [Y/N]: '))
    if (run == "Y" or run == "y"):
         inv = 0
         pocket = ''
         living_room()
    else:
         print('Thank you for playing, bye.')
         print(new_line)


def die():
    global inv
    global pocket
    os.system('cls')
    print(red_bd + die_banner.center(50,' ') + normal + new_line)
    time.sleep(2)
    print('Better luck next time.')
    run = (input('Play again? [Y/N]: '))
    if (run == "Y" or run == "y"):
         inv = 0
         pocket = ''
         living_room()
    else:
         print('Thank you for playing, bye.')
         print(new_line)


def huh():
    print(new_line + "Sorry, I didn't understand that.")
    time.sleep(2)


def shed():
    global inv
    global pocket
    os.system('cls')
    print(red_bd + shed_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a lawmmower, a rake, a shovel, the DOOR of the shed and a FLASHLIGHT.')
    action    = input('Enter your choice: ')
    if (action == "DOOR" or action == "door" or action == "D" or action == "d"):
        print(new_line + 'You walk out of the shed.')
        time.sleep(2)
        backyard()
    elif (action == "FLASHLIGHT" or action == "flashlight" or action == "F" or action == "f"):
            t_action    = input('Take the Flashlight [Y/N]? ')
            if (t_action == 'Y' or t_action == 'y'):
                print(new_line + 'You take the Flashlight and leave the shed.')
                inv = (inv + 1)
                if inv > 0:
                    pocket = 'FL'
                    time.sleep(2)
                    backyard()
                elif inv <= 0:
                    pocket = ''
                    time.sleep(2)
                    backyard()
            
            
            elif (t_action == 'N' or t_action == 'n'):
                print(new_line + 'You leave the Flashlight and leave the shed.')
                if inv > 0:
                    pocket = 'FL'
                    time.sleep(2)
                    backyard()
                else:
                    pocket = ''
                    time.sleep(2)
                    backyard()

            else:
                huh()
                shed()
    else:
            huh()
            shed()


def tree():
    os.system('cls')
    print(red_bd + tree_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a BRANCH, the GROUND, a bird nest and a shiny metal object in the distance.')
    time.sleep(2)
    print('You hear a strange humming sound coming from outside the yard.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "BRANCH" or action == "branch" or action == "B" or action == "b"):
        print(new_line + 'You climb out onto the Branch.')
        time.sleep(2)
        print('You hear a loud crack.')
        time.sleep(2)
        print('You fall to the ground, OUCH!')
        time.sleep(2)
        die()
    elif (action == "GROUND" or action == "ground" or action == "G" or action == "g"):
        print(new_line + 'You climb back down to the ground.')
        time.sleep(2)
        backyard()
    else:
        huh()
        tree()

def panel_button():
    print(new_line + 'The ship starts to swing wildly from side to side.')
    time.sleep(5)
    print("You realize you have disengaged the Autopilot.")
    time.sleep(5)
    print("The ship makes a steep dive into Earth's atmosphere.")
    time.sleep(5)
    print("You are gaining speed as you hurl towards Earth.")
    time.sleep(5)
    print("The ship shakes violently as it starts to break apart, what will you do?.")
    time.sleep(5)
    print("No need to fear! The ship slams into the ground just before it completely breaks apart.")
    time.sleep(6)
    die()

def eng_door():
    os.system('cls')
    print(red_bd + eng_room_banner.center(50,' ') + pocket + normal + new_line)
    print("You see racks of equipment, a ship's CREW member and the DOOR back to the Command Center.")
    time.sleep(2)
    action    = input('Enter your choice: ')
    if (action == "DOOR" or action == "door" or action == "D" or action == "d"):
        print(new_line + 'You walk back into the Command Center.')
        time.sleep(2)
        com_center()

    elif (action == "CREW" or action == "crew" or action == "C" or action == "c"):
        print(new_line + 'You see the crew member is hopelessly tangled in sparking wires.')
        time.sleep(2)
        action2    = input('Help crew member [Y/N]? ')
        if (action2 == 'Y' or action2 == 'y'):
                print(new_line + 'You carefully assist the crew member out of the tangle of wires.')
                time.sleep(5)
                print("Despite being shocked yourself, you bravely rescue the crew member.")
                time.sleep(5)
                print("The entire ship's crew is thankful.")
                time.sleep(4)
                print("They take you to their planet and celebrate you as a Hero.")
                time.sleep(5)
                print("You live the rest of your life in comfort and luxury.")
                time.sleep(5)
                the_end()

        elif (action2 == 'N' or action2 == 'n'):
                print(new_line + 'You walk back into the Command Center.')
                time.sleep(2)
                com_center()
        else:
            huh()
            eng_door()

    else:
        huh()
        eng_door()

def grove():
    os.system('cls')
    print(red_bd + grove_banner.center(50,' ') + pocket + normal + new_line)
    print('You see trees, birds chirping, a DIRT road.')
    time.sleep(2)
    action    = input('Enter your choice: ')
    if (action == "DIRT" or action == "dirt" or action == "D" or action == "d"):
        print(new_line + 'You walk to the Dirt Road.')
        time.sleep(2)
        road()
    elif (action == "GROVE" or action == "grove" or action == "G" or action == "g"):
        print(new_line + 'You walk into the Wooded Grove.')
        time.sleep(2)
        grove()
    else:
        huh()
        road()

def com_center():
    os.system('cls')
    print(red_bd + com_center_banner.center(50,' ') + pocket + normal + new_line)
    print('You see control BUTTONS, display monitors and a DOOR labeled Engineering.')
    time.sleep(2)
    action    = input('Enter your choice: ')
    if (action == "BUTTONS" or action == "buttons" or action == "B" or action == "b"):
        print(new_line + 'You walk over to a control panel and carefully press a button.')
        time.sleep(4)
        panel_button()
    elif (action == "DOOR" or action == "Door" or action == "D" or action == "d"):
        print(new_line + 'You walk over to the Engineering door and it slowly slides open.')
        time.sleep(4)
        eng_door()
    else:
        huh()
        com_center()


def use_light():
    global inv
    global pocket
    print(new_line + 'You turn on your Flashlight and look around.')
    time.sleep(5)
    print("You see three doors and a low overhead beam.")
    time.sleep(5)
    print("The first door is the one you came through, no visable button near it.")
    time.sleep(5)
    print("The second door has a button near it that is labeled, AirLock.")
    time.sleep(6)
    print("The third door has a button near it that is labled, Command Center.")
    time.sleep(7)
    os.system('cls')
    print(red_bd + ship_entry_banner.center(50,' ') + pocket + normal + new_line)
    print('You can use the AIRLOCK button or the COMMAND Center button.')
    time.sleep(3)
    action    = input('Enter your choice: ')
    if (action == "AIRLOCK" or action == "airlock" or action == "A" or action == "a"):
            air_lock()

    elif (action == "COMMAND" or action == "command" or action == "C" or action == "c"):
            com_center()

    else:
        huh()
        use_light()

def yell_help():
    print(new_line + 'You yell for help hoping someone will come to your aid.')
    time.sleep(10)
    print("Eventually, one of the ship's crew sees you and calls for others to come.")
    time.sleep(5)
    print("They watch and listen as you yell for help.")
    time.sleep(5)
    print("They decide to take you back to their planet where you are put on into a singing group.")
    time.sleep(5)
    print("They call the group: The Three Cacophony Tenors.")
    time.sleep(5)
    print("You live the rest of your life in meager comfort as a curiousty act.")
    time.sleep(7)
    the_end()

def dim_wit():
    print(new_line + 'You walk down the corridor.')
    time.sleep(3)
    print("In the dark, you hit your head on a beam and fall unconscious to the floor.")
    time.sleep(5)
    print("The ship's crew find you and put you into a glass chamber.")
    time.sleep(5)
    print("They take you back to their planet where you are put on display.")
    time.sleep(5)
    print("The sign on your chamber reads: Dim Witted Human.")
    time.sleep(5)
    print("You spend the rest of your life begging and doing simple tricks for snacks.")
    time.sleep(7)
    the_end()

def air_lock():
    print(new_line + 'You search in the dark for a button.')
    time.sleep(8)
    print("You finally find a button and eagerly press it.")
    time.sleep(5)
    print("You see a bright red light and the sound of an alarm.")
    time.sleep(5)
    print("You hear mechanical clanks and bangs followed by a whoosh of air.")
    time.sleep(5)
    print("Under the red light, you can see a large door open wide.")
    time.sleep(5)
    print("You are instantly sucked out into space along with various bits of debris.")
    time.sleep(7)
    die()

def ship_entry():
    global inv
    global pocket
    os.system('cls')
    print(red_bd + ship_entry_banner.center(50,' ') + pocket + normal + new_line)
    print('All is dark except for the faint glow of indicator lights.')
    time.sleep(4)
    if (pocket == 'FL'):
        print(new_line + 'You can WALK forward, SEARCH for a button or use your FLASHLIGHT.')
        time.sleep(1)
        action    = input('Enter your choice: ')
        if (action == "WALK" or action == "walk" or action == "W" or action == "w"):
            dim_wit()

        elif (action == "SEARCH" or action == "search" or action == "S" or action == "s"):
            air_lock()

        elif (action == "FLASHLIGHT" or action == "flashlight" or action == "F" or action == "f"):
            use_light()

        else:
            huh()
            ship_entry()

    elif (pocket != 'FL'):
        print(new_line + 'You can WALK forward, SEARCH for a button or YELL for help.')
        time.sleep(1)
        action    = input('Enter your choice: ')
        if (action == "WALK" or action == "walk" or action == "W" or action == "w"):
            dim_wit()

        elif (action == "SEARCH" or action == "search" or action == "S" or action == "s"):
            air_lock()

        elif (action == "YELL" or action == "yell" or action == "Y" or action == "y"):
            yell_help()

        else:
            huh()
            ship_entry()

    else:
            huh()
            ship_entry()


def ship():
    os.system('cls')
    print(red_bd + ship_banner.center(50,' ') + pocket + normal + new_line)
    print('You see grass, a FIELD, a shiny metalic ship and a metal door with a BUTTON.')
    time.sleep(2)
    print('You hear a strange humming sound coming from the Ship.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "FIELD" or action == "field" or action == "F" or action == "f"):
        print(new_line + 'You walk to the grassy Field.')
        time.sleep(2)
        field()
    elif (action == "BUTTON" or action == "button" or action == "B" or action == "b"):
        print(new_line + 'You press the button, a metal ramp appears and the door opens.')
        time.sleep(4)
        action2    = input('Enter the Ship [Y/N]? ')
        if (action2 == 'Y' or action2 == 'y'):
                print(new_line + 'You carefully walk into the Ship, the door slides shut.')
                time.sleep(5)
                print("The frequency of the humming sound intensifies, the ship begins to rumble.")
                time.sleep(5)
                print("You're sure the ship is now flying.")
                time.sleep(3)
        ship_entry()

    elif (action2 == 'N' or action2 == 'n'):
                print(new_line + 'You walk back to the Grassy Field.')
                time.sleep(2)
                field()
    else:
        huh()
        ship()


def closet():
    global inv
    global pocket
    os.system('cls')
    print(red_bd + closet_banner.center(50,' ') + pocket + normal + new_line)
    print('You see clothes, shoes, a FLASHLIGHT and the closet DOOR.')
    action    = input('Enter your choice: ')
    if (action == "FLASHLIGHT" or action == "flashlight" or action == "F" or action == "f"):
            t_action    = input('Take the Flashlight [Y/N]? ')
            if (t_action == 'Y' or t_action == 'y'):
                print(new_line + 'You take the Flashlight and leave the closet.')
                inv = (inv + 1)
                if inv > 0:
                    pocket = 'FL'
                    time.sleep(2)
                    bed_room()
                elif inv <= 0:
                    pocket = ''
                    time.sleep(2)
                    bed_room()
            
            elif (t_action == 'N' or t_action == 'n'):
                print(new_line + 'You leave the Flashlight and leave the closet.')
                if inv > 0:
                    pocket = 'FL'
                    time.sleep(2)
                    bed_room()
                else:
                    pocket = ''
                    time.sleep(2)
                    bed_room()

    elif (action == "DOOR" or action == "door" or action == "D" or action == "d"):
        print(new_line + 'You walk out of the Closet.')
        time.sleep(2)
        bed_room()

    else:
        huh()
        closet()


def field():
    os.system('cls')
    print(red_bd + grassy_banner.center(50,' ') + pocket + normal + new_line)
    print('You see grass, a DIRT road and a large metalic saucer shaped SHIP.')
    time.sleep(2)
    print('You hear a strange humming sound coming from the Ship.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "DIRT" or action == "dirt" or action == "D" or action == "d"):
        print(new_line + 'You walk to the long Dirt Road.')
        time.sleep(2)
        road2()
    elif (action == "SHIP" or action == "ship" or action == "S" or action == "s"):
        print(new_line + 'You walk across the Grassy Field to the Ship.')
        time.sleep(3)
        ship()
    else:
        huh()
        road()



def road2():
    os.system('cls')
    print(red_bd + road2_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a DIRT road, a wooded GROVE and a grassy FIELD.')
    time.sleep(2)
    print('You hear a strange humming sound coming from nearby.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "DIRT" or action == "dirt" or action == "D" or action == "d"):
        print(new_line + 'You walk down the long Dirt Road.')
        time.sleep(2)
        road()
    elif (action == "GROVE" or action == "grove" or action == "G" or action == "g"):
        print(new_line + 'You walk into the Wooded Grove.')
        time.sleep(2)
        grove()
    elif (action == "FIELD" or action == "field" or action == "F" or action == "f"):
        print(new_line + 'You walk into the Grassy Field.')
        time.sleep(2)
        field()
    else:
        huh()
        road()


def road():
    os.system('cls')
    print(red_bd + road_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a DIRT road and a wooded GROVE.')
    time.sleep(2)
    print('You hear a strange humming sound coming from down the road.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "DIRT" or action == "dirt" or action == "D" or action == "d"):
        print(new_line + 'You walk down the long Dirt Road.')
        time.sleep(2)
        road2()
    elif (action == "GROVE" or action == "grove" or action == "G" or action == "g"):
        print(new_line + 'You walk into the Wooded Grove.')
        time.sleep(2)
        grove()
    else:
        huh()
        road()

def backyard():
    os.system('cls')
    print(red_bd + backyard_banner.center(50,' ') + pocket + normal + new_line)
    print('You see grass, a TREE, a SHED, door to the KITCHEN, a fence with a GATE.')
    time.sleep(2)
    print('You hear a strange humming sound coming from outside the fence.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "TREE" or action == "tree" or action == "T" or action == "t"):
        print(new_line + 'You climb the tree.')
        time.sleep(2)
        tree()
    elif (action == "KITCHEN" or action == "kitchen" or action == "K" or action == "k"):
        print(new_line + 'You open the door and walk into the Kitchen')
        time.sleep(2)
        kitchen()
    elif (action == "GATE" or action == "gate" or action == "G" or action == "g"):
        print(new_line + 'You open the gate and walk out of the Backyard.')
        time.sleep(2)
        road()
    elif (action == "SHED" or action == "shed" or action == "S" or action == "s"):
        print(new_line + 'You walk into the tool shed.')
        time.sleep(2)
        shed()
    else:
        huh()
        backyard()

def bed_room():
    os.system('cls')
    global inv
    global pocket
    print(red_bd + bedroom_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a CLOSET, a BED, a DOOR to the bathroom.')
    action    = input('Enter your choice: ')
    if (action == "CLOSET" or action == "closet" or action == "C" or action == "c"):
        print(new_line + 'You walk into the closet.')
        time.sleep(2)
        closet()
            
    elif (action == "BED" or action == "bed" or action == "B" or action == "b"):
        print(new_line + 'You climb into bed and take a nap, ZZZZzzzz....')
        time.sleep(10)
        bed_room()
    elif (action == "DOOR" or action == "door" or action == "D" or action == "d"):
        print(new_line + 'You walk into the BATHROOM.')
        time.sleep(2)
        bathroom()
    else:
        huh()
        bed_room()


def kitchen():
    os.system('cls')
    print(red_bd + kitchen_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a SINK, stove, REFRIGERATOR, doorway to the LIVING room and a door to the BACKYARD.')
    time.sleep(2)
    print('You hear a strange humming sound coming from outside.')
    time.sleep(1)
    action    = input('Enter your choice: ')
    if (action == "SINK" or action == "sink" or action == "S" or action == "s"):
        print(new_line + 'You get a glass a water and drink it.')
        time.sleep(3)
        kitchen()
    elif (action == "REFRIGERATOR" or action == "refrigerator" or action == "R" or action == "r"):
        print(new_line + 'You make yourself a sandwich and eat it, Mmmm...')
        time.sleep(3)
        kitchen()
    elif (action == "LIVING" or action == "living" or action == "L" or action == "l"):
        print(new_line + 'You walk into the Living Room.')
        time.sleep(2)
        living_room()
    elif (action == "BACKYARD" or action == "backyard" or action == "B" or action == "b"):
        print(new_line + 'You walk into the Backyard.')
        time.sleep(3)
        backyard()
    else:
        huh()
        kitchen()

def bathroom():
    os.system('cls')
    print(red_bd + bathroom_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a SINK, a TOILET, a door to a BEDROOM and the door to the LIVING Room.')
    action    = input('Enter your choice: ')
    if (action == "SINK" or action == "sink" or action == "S" or action == "s"):
        print(new_line + 'You wash your hands.')
        time.sleep(2)
        bathroom()
    elif (action == "TOILET" or action == "toilet" or action == "T" or action == "t"):
        print(new_line + 'You use the toilet, better wash your hands.')
        time.sleep(2)
        bathroom()
    elif (action == "LIVING" or action == "living" or action == "L" or action == "l"):
        print(new_line + 'You walk back into the Living Room.')
        time.sleep(2)
        living_room()
    elif (action == "BEDROOM" or action == "bedroom" or action == "B" or action == "b"):
        print(new_line + 'You walk into the Bedroom.')
        time.sleep(2)
        bed_room()
    else:
        huh()
        bathroom()

def living_room():
    os.system('cls')
    print(red_bd + living_room_banner.center(50,' ') + pocket + normal + new_line)
    print('You see a COUCH, TV, doorway to KITCHEN and a BATHROOM door.')
    action    = input('Enter your choice: ')
    if (action == "COUCH" or action == "couch" or action == "C" or action == "c"):
        print(new_line + 'You sit on the couch and watch TV.')
        time.sleep(5)
        living_room()
    elif (action == "TV" or action == "tv" or action == "T" or action == "t"):
        print(new_line + 'You notice that the TV is on.')
        time.sleep(2)
        living_room()
    elif (action == "KITCHEN" or action == "KITCHEN" or action == "K" or action == "k"):
        print(new_line + 'You walk into the Kitchen.')
        time.sleep(2)
        kitchen()
    elif (action == "BATHROOM" or action == "bathroom" or action == "B" or action == "b"):
        print(new_line + 'You walk into the Bathroom.')
        time.sleep(2)
        bathroom()
    else:
        huh()
        living_room()


os.system('cls')
print(red_bd + welcome_banner.center(50,' ') + normal + new_line)
instructions = input('Do you want instructions [Y/N]? ')

if (instructions == "Y" or instructions == "y"):
    instruct()
elif (instructions == "N" or instructions == "n"):
    living_room()
else:
    print('Thank you for playing, bye.')
    


