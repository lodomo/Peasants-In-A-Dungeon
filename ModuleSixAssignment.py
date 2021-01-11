# Loren Haskins

import sys
import time
from os import system, name

# Directions
North = 'North'
East = 'East'
South = 'South'
West = 'West'
Cardinal_Directions = [North, South, East, West]

#Rooms
Chamber = 'Chamber'
ChestRoom = 'Chest Room'
Shop = 'Shop'
PrismRoom = 'Prism Room'
Bathroom = 'Bathroom'
RiddleRoom = 'Riddle Room'
SkeletonRoom = 'Skeleton Room'
MirrorRoom = 'Mirror Room'
KeyRoom = 'Key Room'
FrogRoom = 'Frog Room'

#Globals
global type_speed
type_speed = 0.0125

# Dictionary of all rooms and their doors
rooms = {
    Chamber: {East: ChestRoom, West: Shop, North: PrismRoom},
    Shop: {East: Chamber},
    ChestRoom: {West: Chamber},
    PrismRoom: {South: Chamber, West: Bathroom, North: RiddleRoom},
    Bathroom: {East: PrismRoom},
    RiddleRoom: {South: PrismRoom, North: SkeletonRoom},
    SkeletonRoom: {South: RiddleRoom, East: MirrorRoom},
    MirrorRoom: {North: FrogRoom, South: KeyRoom, West: SkeletonRoom},
    KeyRoom: {North: MirrorRoom},
    FrogRoom: {South: MirrorRoom}
}


# Clear the screen.
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# If I need to pause anything I can pause it for fl time. Also for slowly printing text
def wait(fl):
    time.sleep(fl)

# Slowly print text onto screen instead of huge blocks of text instantly
def print_type(string):
    if type_speed == 0:
        print(string)
    else:
        string = string.split()
        length = range(len(string))
        for i in length:
            word = list(string[i])
            for char in word:
                print(char, end='')
                sys.stdout.flush()
                wait(type_speed)
            if i != length:
                print(' ', end='')
                wait(type_speed)
        print()

# Ask user if they want text to appear suddenly to be typed out.
def set_type_effect_speed():
    print_type('Before we begin, would you like to turn off this typing effect?')
    while True:
        global type_speed
        set_type = input().upper()
        if set_type == 'Y' or set_type == 'YES':
            type_speed = 0.0
            break
        elif set_type == 'N' or set_type == 'NO':
            break
        else:
            print_type('Sorry that is not an option. Try again.')
            print_type('Would you like to turn off this typing effect? Y or N')
    clear_screen()


# This is just the intro. You go down into the hole no matter what.
def introduction():
    print_type('Welcome to the prologue to Peasants in a Dungeon.')
    print()
    print_type('You find yourself on a bumpy road in the middle of nowhere. Two paladins are taking you farther away ')
    print_type('from your home than you have ever been before, but how often do you get offered a job from the king?!')
    print_type('The Mad King Miller offered you more money than you have made in your entire gnome life!')
    print()
    print_type('How hard could this be?!')
    print()
    print_type('One afternoon\'s work and you will be able to surprise your wife with a farm and an honest life.')
    print()
    print_type('The cart suddenly stops in the middle of a field.')
    print_type('\"OHWL ROIGHT LIDDLE ONE. DOWN THE WELL\" shouts one of the paladins.')
    print_type('There is a well a few feet away from the cart.')
    print_type('Do you GO DOWN or DEFY?')

    # Get different dialogue for going down, or defying the paladins
    while True:
        down_or_defy = input().upper()
        if down_or_defy == 'GO DOWN' or down_or_defy == 'DOWN':
            print_type('You take a deep breath and look down the well. It looks like a pretty far drop, but you have ')
            print_type('to remember. This is for your family\'s future. Your grandchildren will live off this farm.')
            print_type('You hop into the well. Everything fades to black.')
            break
        elif down_or_defy == 'DEFY':
            print_type('\"THIS WAS NOT PART OF THE DEAL! I am here to clean for--\"')
            print_type('Before you can finish your sentence, one of the paladins cracks you in the nose with the hilt ')
            print_type('of his sword. Everything fades to black.')
            break
        else:
            # Gets the proper input from the user.
            print_type('Sorry, that\'s not an option. Do you GO DOWN or DEFY?')

    # Delays the text to fly up the screen to simulate falling. Different if the text is typing or not.
    if type_speed != 0:
        wait(2)
    else:
        wait(4)

    for i in range(30):
        print()
        wait(0.05)

    clear_screen()
    print_type('You wake up on a cold stone floor. A voice is heard in the distance')
    print_type('\"OI! You must be the new room checker. Can you make sure you go into all ten rooms?\"')

# Keeps the user in a loop of rooms.
def room_loop():
    # Set current room to starting room.
    current_room = rooms[Chamber]
    # Keeps track of all the rooms the user has entered
    rooms_entered = []

    #Get put into a loop
    while True:
        # Count the amount of doors in the room
        door_count = len(current_room)

        # Set dialogue for only amount of doors door
        if door_count == 1:
            for door in current_room:
                string_to_print = 'There is 1 door to the ' + door
                print(string_to_print)
        else:
            string_to_print = 'There are ' + str(door_count) + ' doorways: '
            for door in current_room:
                if door == list(current_room)[-1]:
                    string_to_print += 'and '
                string_to_print += door + ' '
            print(string_to_print)

        # Get inputs for North south east or west. All inputs get capitalized for easy checking.
        print_type('Which way do you want to go?')
        change_room = input().capitalize()

        #Check to see if the user is going in a proper cardinal direction
        if change_room in Cardinal_Directions:
            # Check if the input is a valid door to the room. If not, reset the prompt.
            if change_room in current_room:
                # Create the string to tell the user their current room.
                string_to_print = 'You have entered the ' + current_room[change_room]

                # Add current room to list of entered rooms
                if current_room[change_room] not in rooms_entered:
                    rooms_entered.append(current_room[change_room])

                # Tell player the room they're about to enter
                print_type(string_to_print)

                #Set current room
                current_room = rooms[current_room[change_room]]

                # if the user has found 10 rooms, tell them to go to the frog room.
                # if they're in the frog room, run the finale.
                if len(rooms_entered) == 10:
                    if current_room != rooms[FrogRoom]:
                        print_type('Head to the FROG ROOM... Quickly!')
                    else:
                        finale()
                        break
            else:
                print('There is no door to the ' + change_room)
        elif change_room == 'Exit':
            # Part of the prompt was for an exit room. Here it is. This will end the game.
            print_type('You\'ve entered into a room called exit, there are no windows or doors')
            print_type('You can hear your own heart beating. How long will you be trapped here?')
            break
        else:
            print_type('Sorry, You can\'t do that. Please enter a cardinal direction to move to a new room.')

# This is the finale scene, you're turned into a frog.
def finale():
    print_type('The door to the Frog Room suddenly slams shut and your body is hurled into the middle of the room.')
    print_type('High pitched crackles deafen your ears as the door forms into a giant block of ice.')
    print_type('A voice comes from the dark corners of the room.')
    print_type('\"I told those oafs to bring me a large creature. Not a grubby little gnome\"')
    print_type('The owner of the voice creeps from the shadows.')
    print_type('An old man draped in robes, his cane quivering under his weight.')
    print_type('\"You will have to do, we haven\'t much time.\"')
    print_type('\"RHINELLA MARINA!\"')
    print_type('Your tiny body grows even smaller. Your skin starts to turn green. You\'ve been turned into a toad!')

    # any input is assumed to be words, but you're a frog you can only say RIBBIT.
    while True:
        print_type('\"Any questions, Mr. Toad?\" the old wizard says, looking quite pleased with his spell.')
        input()
        print_type('Sorry, RIBBIT is an invalid action. Try again.')
        input()
        print_type('Sorry, RIBBIT is an invalid action. Try again.')
        input()
        print_type('You are hopeless, aren\'t you? Hope you don\'t get too hungry down here.')
        print()
        print()
        print_type('END PROLOGUE.')
        break

def main():
    set_type_effect_speed()
    introduction()
    room_loop()
    input()


if __name__ == "__main__":
    main()
