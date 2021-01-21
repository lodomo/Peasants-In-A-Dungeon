# Loren Haskins
import os
import sys
import time
import art
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
Room_Name = 'Room Name'
Doors = 'Doors'
Info = 'Info'
Info2 = 'Info2'
Item = 'Item'
Art = 'Art'
Help = 'Help'
Action = 'Action'
TakeArt = 'Take Art'
TakeInfo = 'Take Info'
TakeInfo2 = 'Take Info2'
TakeHelp = 'Take Help'
Special = 'Special'
GiveArt = 'Give Art'
GiveInfo = 'Give Info'
GiveInfo2 = 'Give Info2'
GiveHelp = 'Give Help'

# Items
Hammer = 'Hammer'
Prism = 'Prism'
Towel = 'Towel'
Sword = 'Sword'
Cheese = 'Cheese'
Key = 'Key'
Jar = 'Jar Of Flies'

# Input alternatives
inventory_alternatives = ['Inventory', 'Bag', 'Satchel']

items = [Hammer, Prism, Towel, Sword, Cheese, Key, Jar]
bad_words = ['Sword', 'Shit', 'Piss', 'Fuck', 'Cunt', 'Cocksucker', 'Motherfucker', 'Tits']
user_input = ''

rooms = {
    Chamber: {
        Room_Name: Chamber,
        Info: 'The room is made of stone. It is cold and damp.',
        Info2: 'You wonder if you could get HELP',
        Help: 'You should try going through one of these doors. what DIRECTION will you go?',
        Item: 'None',
        Art: art.chamber,
        Special: 'None',
        Doors: {East: ChestRoom, West: MouseRoom, North: PrismRoom},
    },
    MouseRoom: {
        Room_Name: MouseRoom,
        Info: 'A mouse protects his hammer. It is far too big for him to use.',
        Info2: 'He says he\'ll trade it for some cheese',
        Help: 'GIVE the mouse some CHEESE... unless you\'re a thief.',
        Item: Hammer,
        Art: art.mouse_with_hammer,
        Special: 'Give Cheese',
        TakeArt: art.surprised_mouse,
        TakeInfo: 'The mouse is surprised you were able to take his hammer with ease.',
        TakeInfo2: 'Your BAG now contains a Hammer, but the guilt is much heavier.',
        TakeHelp: 'HOW DARE YOU ASK FOR HELP, YOU THIEF!',
        GiveArt: art.mouse_without_hammer,
        GiveInfo: 'Thank you kind, peasant. Here is my hammer.',
        GiveInfo2: 'It\'s good to BASH with it. Especially rusty objects.',
        GiveHelp: 'Nothing left to do in this room',
        Doors: {East: Chamber}
    },
    ChestRoom: {
        Room_Name: ChestRoom,
        Info: 'A chest sit patiently awaiting a key in the center of the room',
        Info2: 'Bzzzzz, bzzzzzz, bzzzzzz',
        Help: 'Your hear buzzing from inside the chest! You need to find a KEY!',
        Item: 'None',
        Art: art.chest_closed,
        Special: 'None',
        Doors: {West: Chamber}
    },
    PrismRoom: {
        Room_Name: PrismRoom,
        Info: 'A bright white light turns into the most beautiful colors imaginable.',
        Info2: '',
        Help: 'I should PICKUP the PRISM, it might come in handy.',
        Item: Prism,
        Art: art.prism_in_prism_room,
        TakeArt: art.no_prism_in_prism_room,
        TakeInfo: 'A bright white light beams across the room uninterrupted.',
        TakeInfo2: 'You wonder if you\'re just another brick in the wall.',
        TakeHelp: 'Nothing left to do in this room',
        Special: 'None',
        Doors: {South: Chamber, West: Bathroom, North: RiddleRoom}
    },
    Bathroom: {
        Room_Name: Bathroom,
        Info: 'This bathroom is remarkably clean... all things considered.',
        Help: 'Don\'t Panic, and don\'t forget to bring a towel.',
        Item: Towel,
        Art: art.bath_room_with_towel,
        Special: 'None',
        TakeArt: art.bath_room_toilet_only,
        TakeInfo: 'A toilet sits alone in the room. There\'s no towel and no sink...',
        TakeInfo2: 'A traveler always has a towel, this should come in handy',
        TakeHelp: 'Nothing left for you here to do.',
        Doors: {East: PrismRoom}
    },
    RiddleRoom: {
        Room_Name: RiddleRoom,
        Info: 'A gnome has something shiny behind him. Only a true hero can have it',
        Info2: 'You must say the only curse word a hero is allowed to use.',
        Help: 'You cannot say the FWORD, maybe you can say a different _WORD',
        Item: 'None',
        Special: bad_words,
        Art: art.gnome_with_sword,
        TakeArt: art.gnome_without_sword,
        TakeInfo: 'Good job, hero! Here is your sword!',
        TakeInfo2: 'Most peasants swear like George Carlin and die to the beast.',
        TakeHelp: 'Nothing left for you here to do.',
        Doors: {South: PrismRoom, North: SkeletonRoom}
    },
    SkeletonRoom: {
        Room_Name: SkeletonRoom,
        Info: 'A rainbow light shines upon a pedestal with a triangular hole.',
        Info2: 'There is a skeleton in the corner minding his own business',
        Help: 'Maybe I should SEARCH the SKELETON, and PLACE an ITEM in the hole',
        Item: 'None',
        Art: art.pedestal_skeleton,
        Special: ['Place Prism', 'Search Skeleton'],
        GiveArt: art.pedestal_skeleton_prism,
        GiveInfo: 'A blast of white light makes its way into the Mirror Room',
        TakeInfo: 'Hey! The skeleton was saving that for later.',
        Doors: {South: RiddleRoom, East: MirrorRoom}
    },
    MirrorRoom: {
        Room_Name: MirrorRoom,
        Info: 'A block of ice blocks the north door. A door with a rusted lock blocks',
        Info2: 'the south door. A dirty mirror sits in the middle of the room',
        Help: 'You should CLEAN the MIRROR, and BASH the LOCK.',
        Item: 'None',
        Art: art.mr_ice_dm_lock,
        'Art1': art.mr_ice_cm_lock,
        'Art2': art.mr_cm,
        'Art3': art.mr_ice_cm,
        'Art4': art.mr_ice_dm,
        'Art5': art.mr_cm_lock,
        Special: ['Bash Lock', 'Clean Mirror'],
        Doors: {West: SkeletonRoom, South: KeyRoom, North: FrogRoom}
    },
    KeyRoom: {
        Room_Name: KeyRoom,
        Info: 'There\'s literally just a key in this room. What a waste of space!',
        Help: 'TAKE the KEY, dingus.',
        Item: Key,
        Art: art.key,
        Special: 'None',
        Doors: {North: MirrorRoom}
    },
    FrogRoom: {
        Room_Name: FrogRoom,
        Info: 'A frog sits in the room with a sign that says FEED ME.',
        Info2: 'He looks so hungry.',
        Help: 'Frogs eat flies. You need to feed him flies. OPEN him a JAR of flies.',
        Item: 'None',
        Art: art.frog_with_sign,
        Special: 'None',
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
    print('\n  ╔', end='')
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


def print_art(artwork):
    for art in artwork:
        print(art)


# Introduction to game.
def introduction():
    print_art(art.burlap)
    lines = ['You open your eyes, and you can\'t make out anything.',
             'Your hands are bound with rope. A burlap sack is over your head.',
             'It\'s scratchy on your nose.',
             'Do you remain QUIET or SCREAM for help?']
    text_box(lines)
    while True:
        quiet_or_scream = input().upper()
        cls()
        if quiet_or_scream == 'QUIET':
            print_art(art.burlap)
            quiet = ['Maybe if you remain quiet, there\'s a chance you will survive.',
                     'You jostle from left to right. You must be in a cart of some sort.',
                     'There is an incredibly foul stench coming through the burlap.',
                     'The cart slows to a halt. Thoughts of terror rush through your brain.',
                     ]
            text_box(quiet)
            break
        elif quiet_or_scream == 'SCREAM':
            print_art(art.help_art)
            scream = ['You scream at the top of your lungs for help.',
                      '\"OI! SHU-CHOR MOUF BACK DERE, NO\'ON CAN \'EAR YOU OUT \'ERE\"',
                      'Before you can comprehend anything a blow to your head knocks',
                      'you unconscious']
            text_box(scream)
            break
        else:
            print_art(art.burlap)
            error = [
                'Sorry that is not an option right now. Do you SCREAM or keep QUIET?'
            ]
            text_box(error)
    input('Press Enter To Continue')
    cls()

    meet_the_thugs = [
        'Two thugs pull you from the cart.',
        'They rip the burlap from off your head.',
        'These guys were probably where the smell was coming from'
    ]

    down_the_well = [
        'Alroight, peasant. \'ere\'s the roo\'s.',
        'Solve the puzzo\', kill the beast',
        'It ain\'t \'ard, yet no one seems to \'ave done it.',
        'Down the well wiff \'ya.'
    ]

    print_art(art.well)
    text_box(meet_the_thugs)

    input('Press Enter To Continue')
    cls()
    print_art(art.well)
    text_box(down_the_well)

    input('Press Enter To Continue')

    for line in art.fall_well:
        print(line)
        wait(0.0125)

    input()


def room_data(room_name):
    cls()
    cur_room = rooms[room_name]
    rm_name = 'You are in the ' + room_name
    data = cur_room[Info]

    item = cur_room[Item]
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

    if item != 'None':
        item = 'There is a ' + item + ' in this room.'
        text_for_room = [rm_name, data, item, print_doors]
    else:
        text_for_room = [rm_name, data, cur_room[Info2], print_doors]

    text_box(text_for_room)
    return cur_room


def game_loop():
    current_room = room_data(Chamber)
    carlin_points = 0
    inventory = []

    while True:
        user_input = input().title()
        if user_input in current_room[Doors]:
            current_room = room_data(current_room[Doors][user_input])
        elif user_input in Cardinal_Directions:
            print('Sorry! You can\'t go that way.')
        elif user_input == Help:
            print(current_room[Help])
        elif user_input == 'Take ' + current_room[Item]:
            if current_room[Item] != 'None':
                inventory.append(current_room[Item])
                print(current_room[Item] + ' added to your BAG')
                current_room[Item] = 'None'

                if TakeInfo in current_room.keys():
                    current_room[Info] = current_room[TakeInfo]
                if TakeInfo2 in current_room.keys():
                    current_room[Info2] = current_room[TakeInfo2]
                if TakeHelp in current_room.keys():
                    current_room[Help] = current_room[TakeHelp]
                if TakeArt:
                    current_room[Art] = current_room[TakeArt]
                    room_data(current_room[Room_Name])
        elif user_input in inventory_alternatives:
            if not inventory:
                print('You do not have any items')
            else:
                bag_contents = 'Your bag contains '
                i = 0
                for item in inventory:
                    if item == inventory[-1]:
                        if i == 0:
                            bag_contents += 'a ' + item
                        else:
                            bag_contents += 'and a ' + item
                    else:
                        bag_contents += 'a ' + item + ', '
                    i += 1
                print(bag_contents)
        elif user_input in current_room[Special]:

            # Mouse Room Special
            if user_input == 'Give Cheese':
                if Cheese in inventory:
                    inventory.remove(Cheese)
                    inventory.append(Hammer)
                    current_room[Art] = current_room[GiveArt]
                    current_room[Info] = current_room[GiveInfo]
                    current_room[Info2] = current_room[GiveInfo2]
                    current_room[Help] = current_room[GiveHelp]
                    current_room[Item] = 'None'
                    room_data(current_room[Room_Name])
                else:
                    print('You have no cheese to give.')

            # Riddle Room special rules.
            if user_input == 'Sword':
                inventory.append('Sword')
                current_room[Art] = current_room[TakeArt]
                current_room[Info] = current_room[TakeInfo]
                current_room[Info2] = current_room[TakeInfo2]
                current_room[Help] = current_room[TakeHelp]
                room_data(current_room[Room_Name])
            elif user_input in bad_words:
                carlin_points += 1
                bad_words.remove(user_input)
                print('Please refrain from using profanity. Try again.')
                if carlin_points == 7:
                    print('You need to wash your mouth out with soap. You know the major dirty words but you don\'t '
                          'know the word SWORD?')

            # Skeleton Room special rules.
            if user_input == 'Place Prism':
                if Prism in inventory:
                    current_room[Art] = current_room[GiveArt]
                    current_room[Info] = current_room[GiveInfo]
                    room_data(current_room[Room_Name])
            elif user_input == 'Search Skeleton':
                print('You search the pile of bones and find some cheese!')
                print('You put the cheese in your bag.')
                inventory.append(Cheese)
                current_room[Special].remove(user_input)

            # Mirror Room special rules.
            if user_input == 'Clean Mirror':
                if Towel in inventory:
                    # TODO
                    print()     # DELETE ME
                else:
                    print('You don\'t have anything to use to clean the mirror.')
        else:
            bad_input()


def bad_input():
    print('Sorry, I don\'t understand what you want to do. Type HELP if you\'re stuck')


if __name__ == '__main__':
    # introduction()
    game_loop()
    input()
