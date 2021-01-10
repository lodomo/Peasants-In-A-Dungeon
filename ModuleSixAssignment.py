# Loren Haskins
import sys
import time

# Constants
North = 'North'
East = 'East'
South = 'South'
West = 'West'
Down = 'Down'
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
BossRoom = 'Boss Room'
type_speed = 0.025

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
    FrogRoom: {South: MirrorRoom, Down: BossRoom}
}


def wait(fl):
    time.sleep(fl)


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
        print('')


'''GAME STARTS HERE'''
input()
print_type('Before we begin, would you like to turn off this typing effect?')

while True:
    set_type = input().upper()
    if set_type == 'Y' or set_type == 'YES':
        type_speed = 0
        print_type('That\'s okay. It\'s not like I spent a lot of time creating an immersive experience')
        break
    elif set_type == 'N' or set_type == 'NO':
        print_type('Thank you.')
        break
    else:
        print_type('Sorry that is not an option. Try again.')
        print_type('Would you like to turn off this typing effect? Y or N')

print()
print_type('Welcome to the prologue to Peasants in a Dungeon.')
print()
print_type('You find yourself on a bumpy road in the middle of nowhere. Two paladins are taking you farther away from')
print_type('your home than you have ever been before, but how often do you get offered a job from the king?!')
print_type('The Mad King Miller offered you more money than you have made in your entire gnome life')
print()
print_type('How hard could this be?!')
print()
print_type(' One afternoon\'s work and you will be able to surprise your wife with a farm and an honest life')
print_type('')

input()
