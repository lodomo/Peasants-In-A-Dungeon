# Loren Haskins
import os
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
BossRoom = 'Boss Room'

# Room Characteristics
RoomName = 'Room Name'
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
generic_help = 'This room is finished. You can check your BAG if you\'d like'

# Items
Hammer = 'Hammer'
Prism = 'Prism'
Towel = 'Towel'
Sword = 'Sword'
Cheese = 'Cheese'
Key = 'Key'
Jar = 'Jar Of Flies'
inventory = []

# Input alternatives
inventory_alternatives = ['Inventory', 'Bag', 'Satchel']

# Please excuse the vulgarity. If you say all the bad words in the riddle, it gives you the answer.
bad_words = ['Sword', 'Shit', 'Piss', 'Fuck', 'Cunt', 'Cocksucker', 'Motherfucker', 'Tits']

# Initialize user_input variable.
user_input = ''

# 0 is Ice, 1 is Dirt, 2 is Lock.
mirror_room_status = [True, True, True]


# This handles all the artwork switching for the mirror room.
def mirror_room_artwork():
    artwork = []
    ice = []
    mirror = []
    lock = []
    if mirror_room_status[0]:
        ice = art.ice
    else:
        ice = art.no_ice

    if mirror_room_status[1]:
        mirror = art.dirty_mirror
    else:
        mirror = art.clean_mirror

    if mirror_room_status[2]:
        lock = art.lock
    else:
        lock = art.broken_lock

    i = 0
    for lines in ice:
        artwork.append(ice[i] + mirror[i] + lock[i])
        i += 1

    return artwork


# Dictionary containing all rooms, and their characteristics.
rooms = {
    Chamber: {
        RoomName: Chamber,
        Info: 'The room is made of stone. It is cold and damp.',
        Info2: 'You wonder if you could get HELP',
        Help: 'You should try going through one of these doors. what DIRECTION will you go?',
        Item: 'None',
        Art: art.chamber,
        Special: 'None',
        Doors: {East: ChestRoom, West: MouseRoom, North: PrismRoom},
    },
    MouseRoom: {
        RoomName: MouseRoom,
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
        GiveHelp: generic_help,
        Doors: {East: Chamber}
    },
    ChestRoom: {
        RoomName: ChestRoom,
        Info: 'A chest sit patiently awaiting a key in the center of the room',
        Info2: 'Bzzzzz, bzzzzzz, bzzzzzz',
        Help: 'Your hear buzzing from inside the chest! You need to find a KEY!',
        Item: 'None',
        Art: art.chest_closed,
        Special: ['Use Key', 'Open Chest'],
        TakeArt: art.chest_open,
        TakeInfo: 'dadadada dadadada dada... da... da... DA DA DA DAAAHHHH!',
        TakeInfo2: 'Inside the chest is a Jar of Flies. Was this a jar of maggots before?',
        Doors: {West: Chamber}
    },
    PrismRoom: {
        RoomName: PrismRoom,
        Info: 'A bright white light turns into the most beautiful colors imaginable.',
        Info2: '',
        Help: 'You should TAKE the PRISM, it might come in handy.',
        Item: Prism,
        Art: art.prism_in_prism_room,
        TakeArt: art.no_prism_in_prism_room,
        TakeInfo: 'A bright white light beams across the room uninterrupted.',
        TakeInfo2: 'You wonder if you\'re just another brick in the wall.',
        TakeHelp: generic_help,
        Special: 'None',
        Doors: {South: Chamber, West: Bathroom, North: RiddleRoom}
    },
    Bathroom: {
        RoomName: Bathroom,
        Info: 'This bathroom is remarkably clean... all things considered.',
        Help: 'Don\'t Panic, and don\'t forget to bring a towel.',
        Item: Towel,
        Art: art.bath_room_with_towel,
        Special: 'None',
        TakeArt: art.bath_room_toilet_only,
        TakeInfo: 'A toilet sits alone in the room. There\'s no towel and no sink...',
        TakeInfo2: 'A traveler always has a towel, this should come in handy',
        TakeHelp: generic_help,
        Doors: {East: PrismRoom}
    },
    RiddleRoom: {
        RoomName: RiddleRoom,
        Info: 'A gnome has something shiny behind him. Only a true hero can have it',
        Info2: 'You must say the only curse word a hero is allowed to use.',
        Help: 'You cannot say the FWORD, maybe you can say a different _WORD',
        Item: 'None',
        Special: bad_words,
        Art: art.gnome_with_sword,
        TakeArt: art.gnome_without_sword,
        TakeInfo: 'Good job, hero! Here is your sword!',
        TakeInfo2: 'Most peasants swear like George Carlin and die to the beast.',
        TakeHelp: generic_help,
        Doors: {South: PrismRoom, North: SkeletonRoom}
    },
    SkeletonRoom: {
        RoomName: SkeletonRoom,
        Info: 'A rainbow light shines upon a pedestal with a triangular hole.',
        Info2: 'There is a skeleton in the corner minding his own business',
        Help: 'Maybe you should SEARCH the SKELETON, and PLACE an ITEM in the hole',
        Item: 'None',
        Art: art.pedestal_skeleton,
        Special: ['Place Prism', 'Put Prism', 'Set Prism', 'Search Skeleton'],
        GiveArt: art.pedestal_skeleton_prism,
        GiveInfo: 'A blast of white light makes its way into the Mirror Room',
        TakeInfo: 'Hey! The skeleton was saving that for later.',
        Doors: {South: RiddleRoom, East: MirrorRoom}
    },
    MirrorRoom: {
        RoomName: MirrorRoom,
        Info: 'A dirty mirror sits in the middle of the room. Ice blocks the north door.',
        Info2: 'A rusted lock stops you from going south.',
        Help: 'You should CLEAN the MIRROR, and BASH the LOCK.',
        Item: 'None',
        Art: mirror_room_artwork(),
        Special: ['Bash Lock', 'Break Lock', 'Clean Mirror'],
        Doors: {West: SkeletonRoom}
    },
    KeyRoom: {
        RoomName: KeyRoom,
        Info: 'There\'s literally just a key in this room. What a waste of space!',
        Info2: '',
        Help: 'TAKE the KEY, dingus.',
        Item: Key,
        Art: art.key,
        TakeInfo: 'There\'s literally nothing left in this room except a dust outline.',
        TakeArt: art.no_key,
        TakeInfo2: 'So much room for activities!',
        TakeHelp: generic_help,
        Special: 'None',
        Doors: {North: MirrorRoom}
    },
    FrogRoom: {
        RoomName: FrogRoom,
        Info: 'A frog sits in the room with a sign that says FEED ME.',
        Info2: 'He looks so hungry.',
        Help: 'Frogs eat flies. You need to feed him flies. OPEN him a JAR of flies.',
        Item: 'None',
        Art: art.frog_with_sign,
        Special: ['Open Jar', 'Give Jar', 'Feed Frog'],
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


# Creates a box around a list of strings. If the list is smaller than 4, it makes it a bigger box.
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


# Prints artwork from the art.py into the game.
def print_art(artwork):
    for arts in artwork:
        print(arts)


# Introduction to game.
def introduction():
    print_art(art.burlap)
    lines = ['You open your eyes, and you can\'t make out anything.',
             'Your hands are bound with rope. A burlap sack is over your head.',
             'It\'s scratchy on your nose.',
             'Do you remain QUIET or SCREAM for help?']
    text_box(lines)
    while True:
        quiet_or_scream = input().title()
        if quiet_or_scream == 'Quiet':
            print_art(art.burlap)
            quiet = ['Maybe if you remain quiet, there\'s a chance you will survive.',
                     'You jostle from left to right. You must be in a cart of some sort.',
                     'There is an incredibly foul stench coming through the burlap.',
                     'The cart slows to a halt. Thoughts of terror rush through your brain.',
                     ]
            text_box(quiet)
            break
        elif quiet_or_scream == 'Scream':
            print_art(art.help_art)
            scream = ['You scream at the top of your lungs for help.',
                      '\"OI! SHU-CHOR MOUF BACK DERE, NO\'ON CAN \'EAR YOU OUT \'ERE\"',
                      'Before you can comprehend anything a blow to your head knocks',
                      'you unconscious']
            text_box(scream)
            break
        elif quiet_or_scream in inventory_alternatives:
            print('Your hands are bound. You can SCREAM or keep QUIET')
        else:
            print('Sorry that is not an option right now. Do you SCREAM or keep QUIET?')

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

    # Creates the illusion you're falling down a well.
    for line in art.fall_well:
        print(line)
        wait(0.0125)

    input()


# Generates the text box for each normal room.
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
    elif door_count > 1:
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


# Main loop for the main rooms.
def game_loop():
    current_room = room_data(Chamber)
    carlin_points = 0
    prism_set = False
    while True:
        user_input = input().title()
        # Fixed Take THE item.
        user_input = user_input.replace(' The', '')
        # Fixes Pickup as 1 or two words.
        user_input = user_input.replace('Pick Up', 'Pickup')

        # Checks the status of doors and moves the player.
        if user_input in current_room[Doors]:
            current_room = room_data(current_room[Doors][user_input])
        elif user_input in Cardinal_Directions:
            print('Sorry! You can\'t go that way.')
        # Shows help options.
        elif user_input == Help:
            print(current_room[Help])
        # If theres an item in the room, the player can take it.
        elif user_input == 'Take ' + current_room[Item] or user_input == 'Pickup ' + current_room[Item]:
            if current_room[Item] != 'None':
                inventory.append(current_room[Item])
                print(current_room[Item] + ' added to your BAG')
                current_room[Item] = 'None'

                # Updates all the information for each room.
                if TakeInfo in current_room.keys():
                    current_room[Info] = current_room[TakeInfo]
                if TakeInfo2 in current_room.keys():
                    current_room[Info2] = current_room[TakeInfo2]
                if TakeHelp in current_room.keys():
                    current_room[Help] = current_room[TakeHelp]
                if TakeArt:
                    current_room[Art] = current_room[TakeArt]
                    room_data(current_room[RoomName])

        # Allows user to check their inventory. They can use 'bag, inventory, or satchel'
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

        # This handles all the special commands. If there are no special commands for the room this is
        # skipped entirely.
        elif user_input in current_room[Special]:

            # Mouse Room Special
            if user_input == 'Give Cheese':
                if Cheese in inventory:
                    if Hammer in inventory:
                        print('He\'s frozen stiff. He doesn\'t take the cheese.')
                    else:
                        inventory.remove(Cheese)
                        inventory.append(Hammer)
                        current_room[Art] = current_room[GiveArt]
                        current_room[Info] = current_room[GiveInfo]
                        current_room[Info2] = current_room[GiveInfo2]
                        current_room[Help] = current_room[GiveHelp]
                        current_room[Item] = 'None'
                        room_data(current_room[RoomName])
                else:
                    print('You have no cheese to give.')

            # Riddle Room special rules.
            if user_input == 'Sword':
                inventory.append('Sword')
                current_room[Art] = current_room[TakeArt]
                current_room[Info] = current_room[TakeInfo]
                current_room[Info2] = current_room[TakeInfo2]
                current_room[Help] = current_room[TakeHelp]
                current_room[Special] = []
                room_data(current_room[RoomName])
            elif user_input in bad_words:
                carlin_points += 1
                bad_words.remove(user_input)
                print('Please refrain from using profanity. Try again.')
                if carlin_points == 7:
                    print('You need to wash your mouth out with soap. You know the major dirty words but you don\'t '
                          'know the word SWORD?')

            # Skeleton Room special rules.
            if user_input == 'Place Prism' or user_input == 'Put Prism' or user_input == 'Set Prism':
                if Prism in inventory:
                    current_room[Art] = current_room[GiveArt]
                    current_room[Info] = current_room[GiveInfo]
                    current_room[Special].remove(user_input)
                    prism_set = True
                    if not mirror_room_status[1]:
                        mirror_room_status[0] = False
                        rooms[MirrorRoom][Info] = 'The mirror reflects the light from the other room and melts the ice!'
                        rooms[MirrorRoom][Art] = mirror_room_artwork()
                        rooms[MirrorRoom][Doors][North] = FrogRoom
                    inventory.remove(Prism)
                    room_data(current_room[RoomName])
                else:
                    print('You don\'t have a prism')
            elif user_input == 'Search Skeleton':
                print('You search the pile of bones and find some cheese!')
                print('You put the cheese in your bag.')
                inventory.append(Cheese)
                current_room[Special].remove(user_input)

            # Mirror Room special rules.
            if user_input == 'Clean Mirror':
                if Towel in inventory:
                    mirror_room_status[1] = False
                    if prism_set:
                        mirror_room_status[0] = False
                        current_room[Info] = 'The mirror reflects the light from the other room and melts the ice!'
                        current_room[Doors][North] = FrogRoom
                    else:
                        current_room[Info] = 'The mirror is hungry for light. The ice still blocks the north door.'
                    current_room[Art] = mirror_room_artwork()
                    current_room[Special].remove(user_input)
                    room_data(MirrorRoom)
                else:
                    print('You don\'t have anything to use to clean the mirror.')
            elif user_input == 'Bash Lock' or user_input == 'Break Lock':
                if Hammer in inventory:
                    mirror_room_status[2] = False
                    current_room[Art] = mirror_room_artwork()
                    current_room[Info2] = 'The lock is broken. The door is open to the south.'
                    current_room[Doors][South] = KeyRoom
                    current_room[Special].remove(user_input)
                    room_data(MirrorRoom)
                else:
                    print('You don\'t have a Hammer')

            # Chest Special Rules.
            if user_input == 'Use Key' or user_input == 'Open Chest':
                if Key in inventory:
                    current_room[Art] = current_room[TakeArt]
                    current_room[Info] = current_room[TakeInfo]
                    current_room[Info2] = current_room[TakeInfo2]
                    current_room[Special].remove(user_input)
                    inventory.remove(Key)
                    inventory.append(Jar)
                    room_data(ChestRoom)
                else:
                    print('You don\'t have a Key')

            # Frog room special rules.
            if user_input == 'Open Jar' or user_input == 'Give Jar' or user_input == 'Feed Frog':
                if Jar in inventory:
                    inventory.remove(Jar)
                    fall_again()
                    break
                else:
                    print('You don\'t have a frog food')
        else:
            # If the user puts an invalid input it'll print an error.
            bad_input()


# This is for the fall after the frog becomes large.
def fall_again():
    cls()
    text = [
        'The flies quickly fly out of the jar and expand into gargantuan size.',
        'Mr. Frog gobbles them up with ease, but as the flies grow...',
        '... so does the frog. The ground starts to crack beneath your feet',
        'Looks like you\'re going to fall again.'
    ]
    print_art(art.fly_jar)
    text_box(text)
    input('Press enter to continue')


# Creates an un-escapable boss room.
def boss_fight():
    for line in art.fall_boss:
        print(line)
        wait(0.0125)
    cls()
    print_art(art.pig_king)
    prepare_for_battle = [
        'A huge crowd cheers from all sides. What is happening?.',
        'You start to make out the words from the crowd.',
        '\"Gangyls! Gangyls! Gangyls! Gangyls!\"',
        'A booming voice comes from across  the room. The king... is a pig?',
        'WELCOME PEASANT TO THE FINAL BATTLE.',
        'DRAW YOUR SWORD AND PLUNGE IT INTO THE BEAST',
        'OR ELSE PERISH IN HIS BELLY'
    ]
    text_box(prepare_for_battle)
    input('Press enter to continue')
    cls()
    for line in art.hungry_frog:
        print(line)
        wait(0.1)
    battle_text = [
        'You heard the king. DRAW your SWORD'
    ]
    text_box(battle_text)
    invalid_input = 0
    while True:
        user_input = input().title()
        # If the user has a sword and draws it, wins the game. If they don't have a sword they get eaten.
        if user_input == 'Draw Sword':
            if Sword in inventory:
                print('You plunge the sword deep into the frogs chest. Killing him instantly.')
                input('\n\nPress Enter to Continue')
                return 'Win'
            else:
                print('You never retrieved the sword. SWORD. S-WORD. Get it? S WORD?')
                print('The Frogs tongue lunges from his mouth.')
                input('\n\nPress Enter to Continue')
                return 'Lose'
        if user_input == 'Help':
            print('DRAW your SWORD. If you don\'t have one, you best pray your death be swift')
        if user_input == 'Pray':
            print('A bright white light flashes in the room. The frog returns back to the gnome he once was. You'
                  ' have not only saved yourself, but you saved the life of another. ',
                  'Gods be praised.')
            input('\n\nPress Enter to Continue')
            return 'Win'
        else:
            print('You can\'t do that now. Draw your sword before you get eaten!')
        invalid_input += 1

        if invalid_input >= 5:
            print('You never retrieved the sword. SWORD. S-WORD. Get it? S WORD?')
            print('The Frogs tongue lunges from his mouth.')
            input('\n\nPress Enter to Continue')
            return 'Lose'


def bad_input():
    print('Sorry, I don\'t understand what you want to do. Type HELP if you\'re stuck')


if __name__ == '__main__':
    while True:
        introduction()
        game_loop()
        boss_result = boss_fight()
        if boss_result == 'Win':
            print_art(art.the_end)
            input()
            break
        else:
            print_art(art.you_died)
            input()
            break
