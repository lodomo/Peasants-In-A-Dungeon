# Loren Haskins
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
type_speed = 0.03

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
    FrogRoom: {South: MirrorRoom, Down: BossRoom},
    BossRoom: {}
}


def wait(fl):
    time.sleep(fl)


def type(string):
    if type_speed != 0:
        string = string.split()
        length = range(len(string))
        for i in length:
            word = list(string[i])
            for char in word:
                print(char, end='')
                wait(type_speed)
            if i != length:
                print(' ', end='')
                wait(type_speed)
        print('')
    else:
        print(string)


'''GAME STARTS HERE'''

type('Welcome to the prologue to Peasants in a Dungeon.')
type('Before we begin, would you like to turn off this typing effect? Y or N')

while True:
    set_type = input().upper()
    if set_type == 'Y' or set_type == 'YES':
        type_speed = 0
        type('That\'s okay. It\'s not like I spent a lot of time creating an immersive experience')
        break
    elif set_type != 'N' or set_type == 'NO':
        type('Sorry that is not an option. Try again.')
        type('Would you like to turn off this typing effect? Y or N')
    else:
        type('Thank you.')
        break
