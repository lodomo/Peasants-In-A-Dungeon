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


if __name__ == '__main__':
    # title_art()
    garbage = ['i am a milk man', 'i go with the milk plan', 'cannot stop me from milk land']
    print_strings_in_border(garbage)
    input()
