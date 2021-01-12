# Loren Haskins
import os
import sys
import time
from os import system, name

# Forces screen size to start at 80 chars by 40 chars. Makes it a pretty nice square. I like it.
cmd = 'mode 80,40'
os.system(cmd)

# Directions
North = 'North'
East = 'East'
South = 'South'
West = 'West'
Cardinal_Directions = [North, South, East, West]

# Rooms
Chamber = 'Chamber'
ChestRoom = 'Chest Room'
MouseRoom = 'Mouse Room'
PrismRoom = 'Prism Room'
Bathroom = 'Bathroom'
RiddleRoom = 'Riddle Room'
SkeletonRoom = 'Skeleton Room'
MirrorRoom = 'Mirror Room'
KeyRoom = 'Key Room'
FrogRoom = 'Frog Room'

# Room Characteristics
Doors = 'Doors'

rooms = {
    Chamber: {
        Doors: {East: ChestRoom, West: MouseRoom, North: PrismRoom}
    },
    MouseRoom: {
        Doors: {East: Chamber}
    },
    ChestRoom: {
        Doors: {West: Chamber}
    },
    PrismRoom: {
        Doors: {South: Chamber, West: Bathroom, North: RiddleRoom}
    },
    Bathroom: {
        Doors: {East: PrismRoom}
    },
    RiddleRoom: {
        Doors: {South: PrismRoom, North: SkeletonRoom}
    },
    SkeletonRoom: {
        Doors: {South: RiddleRoom, East: MirrorRoom}
    },
    MirrorRoom: {
        Doors: {North: FrogRoom, South: KeyRoom, West: SkeletonRoom}
    },
    KeyRoom: {
        Doors: {North: MirrorRoom}
    },
    FrogRoom: {
        Doors: {South: MirrorRoom}
    }
}


# Clear The Screen
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Wait to do anything
def wait(fl):
    time.sleep(fl)


def print_top_border():
    print('  ╔', end='')
    for i in range(74):
        print('═', end='')
    print('╗')


def print_bottom_border():
    print('  ╚', end='')
    for i in range(74):
        print('═', end='')
    print('╝')


def print_string_in_border(string):
    print('  ║ ', end='')
    print(string, end='')
    for i in range(80 - (len(string) + 7)):
        print(' ', end='')
    print('║')


def print_strings_in_border(strings):
    print_top_border()
    for string in strings:
        print_string_in_border(string)
    print_bottom_border()


def title_art():
    art = [
        '\n\n\n\n\n\n\n\n'
        '       ██████╗ ███████╗ █████╗ ███████╗ █████╗ ███╗   ██╗████████╗███████╗',
        '       ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗████╗  ██║╚══██╔══╝██╔════╝',
        '       ██████╔╝█████╗  ███████║███████╗███████║██╔██╗ ██║   ██║   ███████╗',
        '       ██╔═══╝ ██╔══╝  ██╔══██║╚════██║██╔══██║██║╚██╗██║   ██║   ╚════██║',
        '       ██║     ███████╗██║  ██║███████║██║  ██║██║ ╚████║   ██║   ███████║',
        '       ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝',
        '                          ██╗███╗   ██╗     █████╗',
        '                          ██║████╗  ██║    ██╔══██╗',
        '                          ██║██╔██╗ ██║    ███████║',
        '                          ██║██║╚██╗██║    ██╔══██║',
        '                          ██║██║ ╚████║    ██║  ██║',
        '                          ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝',
        '        ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗',
        '        ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║',
        '        ██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║',
        '        ██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║',
        '        ██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║',
        '        ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝',
        '\n\n\n'
    ]
    for i in art:
        print(i)
        wait(0.1)

    input('                             PRESS ENTER TO START')
    cls()


# Introduction to game.
def introduction():
    lines = ['You open your eyes, and you still see nothing but darkness.',
             'Your hands are bound with rope.'
             'A burlap sack is over your head.',
             'It\'s scratchy on your nose.',
             'Do you remain QUIET or SCREAM for help?']
    print_strings_in_border(lines)
    while True:
        quiet_or_scream = input().upper()
        if quiet_or_scream == 'QUIET':
            quiet = ['Maybe if you remain quiet, there\'s a chance you will survive.',
                     'You jostle from left to right. You must be in a cart of some sort.',
                     'There is an incredibly foul stench coming through the burlap.',
                     'The cart slows to a halt. Thoughts of terror rush through your brain.',
                     ]
            print_strings_in_border(quiet)
            break
        elif quiet_or_scream == 'SCREAM':
            scream = ['You scream at the top of your lungs for help.',
                      '\"OI! SHU-CHOR MOUF BACK DERE, NO\'ON CAN \'EAR YOU OUT \'ERE\"',
                      'Before you can comprehend anything a blow to your head knocks',
                      'you unconscious']
            print_strings_in_border(scream)
            break
        else:
            print('Sorry that is not an option right now. Do you SCREAM or keep QUIET?')

    halt = ['Wakey, Wakey wee peasant.']


if __name__ == '__main__':
    title_art()
    introduction()
    input()
