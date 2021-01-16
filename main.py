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
Info = 'Info'
Item = 'Item'
Art = 'Art'

art_placeholder = [
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░██████░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░██████░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░██████░░░░██░░░░░░░░████░░░░░░████░░██████░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░░░██░░░░██░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░██░░░░██░░██░░░░░░██░░░░██░░██░░░░░░██████░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░██████░░░░██░░░░░░████████░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░██░░░░░░░░██████░░██░░░░██░░░░████░░██████░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░██░░░░██░░░░████░░░░██░░░░░░██████░░░░██████░░██████░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░██░░░░██░░██░░░░██░░██░░░░░░██░░░░██░░██░░░░░░██░░░░██░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░████████░░██░░░░██░░██░░░░░░██░░░░██░░██████░░██░░░░██░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░██░░░░██░░██░░░░██░░██░░░░░░██░░░░██░░██░░░░░░██████░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░██░░░░██░░░░████░░░░██████░░██████░░░░██████░░██░░░░██░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
    '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░',
]

rooms = {
    Chamber: {
        Info: 'The room is made of stone. It is cold and damp.',
        Item: 'None',
        Art: art_placeholder,
        Doors: {East: ChestRoom, West: MouseRoom, North: PrismRoom},
    },
    MouseRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {East: Chamber}
    },
    ChestRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {West: Chamber}
    },
    PrismRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {South: Chamber, West: Bathroom, North: RiddleRoom}
    },
    Bathroom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {East: PrismRoom}
    },
    RiddleRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {South: PrismRoom, North: SkeletonRoom}
    },
    SkeletonRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {South: RiddleRoom, East: MirrorRoom}
    },
    MirrorRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {North: FrogRoom, South: KeyRoom, West: SkeletonRoom}
    },
    KeyRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {North: MirrorRoom}
    },
    FrogRoom: {
        Info: 'Information on room',
        Item: 'None',
        Art: art_placeholder,
        Doors: {South: MirrorRoom}
    }
}


# Clear The Screen
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Prints Blank Lines to buffer artwork
def blank(int):
    for i in range(int):
        print('')


# Wait to do anything
def wait(fl):
    time.sleep(fl)


def text_box(strings):
    # Print Top Border
    print('  ╔', end='')
    for i in range(74):
        print('═', end='')
    print('╗')

    # Fill Block with Blanks
    while len(strings) < 4:
        strings.append('')

    # Print Text
    for string in strings:
        print('  ║ ', end='')
        print(string, end='')
        for i in range(80 - (len(string) + 7)):
            print(' ', end='')
        print('║')

    # Print Bottom Border
    print('  ╚', end='')
    for i in range(74):
        print('═', end='')
    print('╝')


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
        wait(0.05)

    input('                             PRESS ENTER TO START')
    cls()


def print_art(artwork):
    for art in artwork:
        print(art)


# Introduction to game.
def introduction():
    print_art(art_placeholder)
    lines = ['You open your eyes, and you can\'t make out anything.',
             'Your hands are bound with rope. A burlap sack is over your head.',
             'It\'s scratchy on your nose.',
             'Do you remain QUIET or SCREAM for help?']
    text_box(lines)
    while True:
        quiet_or_scream = input().upper()
        cls()
        if quiet_or_scream == 'QUIET':
            print_art(art_placeholder)
            quiet = ['Maybe if you remain quiet, there\'s a chance you will survive.',
                     'You jostle from left to right. You must be in a cart of some sort.',
                     'There is an incredibly foul stench coming through the burlap.',
                     'The cart slows to a halt. Thoughts of terror rush through your brain.',
                     ]
            text_box(quiet)
            break
        elif quiet_or_scream == 'SCREAM':
            print_art(art_placeholder)
            scream = ['You scream at the top of your lungs for help.',
                      '\"OI! SHU-CHOR MOUF BACK DERE, NO\'ON CAN \'EAR YOU OUT \'ERE\"',
                      'Before you can comprehend anything a blow to your head knocks',
                      'you unconscious']
            text_box(scream)
            break
        else:
            print_art(art_placeholder)
            error = [
                'Sorry that is not an option right now. Do you SCREAM or keep QUIET?'
            ]
            text_box(error)
    input('Press Enter To Continue')
    cls()
    down_the_well = [
        'Alroight, peasant. \'ere\'s the roo\'s.',
        'Solve the puzzo\', kill the beast',
        'It ain\'t \'ard, yet no one seems to \'ave done it.',
        'Down the well wiff \'ya.'
    ]

    print_art(art_placeholder)
    text_box(down_the_well)

    input('Press Enter To Continue')


def room_data(room_name):
    cls()
    cur_room = rooms[room_name]
    rm_name = 'You have entered the ' + room_name
    data = cur_room[Info]
    item = cur_room[Item]
    if item == 'None':
        item = 'There are no items in this room.'
    else:
        item = 'There is a ' + item + ' in this room.'
    doors = cur_room[Doors]
    door_count = len(doors)
    if door_count == 1:
        print_doors = 'There is a door to the ' + list(doors)[0]
    else:
        print_doors = 'There are ' + str(door_count) + ' doorways: '
        for door in doors:
            if door == list(doors)[-1]:
                print_doors += 'and '
            print_doors += door + ' '

    print_art(cur_room[Art])
    text_for_room = [rm_name, data, item, print_doors]
    text_box(text_for_room)
    return cur_room


def game_loop():
    current_room = room_data(Chamber)
    while True:
        user_input = input().capitalize()

        if user_input in current_room[Doors]:
            current_room = room_data(current_room[Doors][user_input])
        elif user_input in Cardinal_Directions:
            print('Sorry! There are no doors in that direction.')


if __name__ == '__main__':
    # title_art()
    # introduction()
    game_loop()
    input()
