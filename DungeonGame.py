# Shannon Hepburn
"Our game map is a 2d array"
"Our bag will be a set. can not have the same items twice"
"Our rooms will be a dictionary of ints to tuples of prompts and items to collect"

"game map, ints greater than 0 are rooms. 0s are hall ways"
gameMap = [[0, 1, 2, 0, 0, 3], [4, 0, 5, 0, 0, 6], [0, 7, 0, 0, 8, 9]]

"player position, start player at 0,0"
playerPos = [0, 0]

"list for storing items along journey"
bag = set( )

"rooms and items in dictionary"
"----------------------------------------------------------------"
rooms = dict( )

rooms[1] = ("This is the first room, the kitchen, there is a bottle of Hennessy.", "henny bottle")

rooms[2] = ("This is the second room, the cafeteria, here is a lamp", "lamp")

rooms[3] = ("This is the third room, the storage room, here is a shield", "shield")

rooms[4] = ("This is the fourth room, the armoury, here is a bow", "bow")

rooms[5] = ("This is the fifth room, the vault, here are some arrows", "arrows")

rooms[6] = ("This is the sixth room, the cooler, here is a helmet", "helmet")

rooms[7] = ("This is the seventh room, enchanted hall, there are magic timberland's", "boots")

rooms[8] = ("This is the last room, the courtyard, there is a dagger", "dagger")

"----------------------------------------------------------------------"

"game prompt"
prompt = "What is your move: \n>rooms \n>bag \n>map \n>right \n>left \n>up \n>down \n >>>>>"

"valid moves"
moves = ["rooms", "bag", "map", "left", "right", "up", "down"]

"prints player map"


def printPlayer(gameMap, x, y):
    "navigation: a 1 is place where player is currently"
    navigation = [[0] * len( gameMap[0] ), [0] * len( gameMap[0] ), [0] * len( gameMap[0] )]
    navigation[x][y] = 1

    for x in gameMap:
        print( x )

    print( "----------------------------------------" )

    for x in navigation:
        print( x )


"Game play"

print(
    "You are the SHIESTY WARRIOR!!! Here is where the journey begins. Collect all the items to defeat the Evils of the world!!!" )

while (len( bag ) < 8):
    x = playerPos[0]
    y = playerPos[1]

    if gameMap[x][y] == 9 and len( bag ) < 8:
        print( "YOU LOSE. You did not have all the things to win the battle" )
        break

    "if not zero, is a room with an item"
    if gameMap[x][y] > 0:
        "if item in bag, no need to add again"
        if rooms[gameMap[x][y]][1] not in bag:
            print( rooms[gameMap[x][y]][0] )
            print( rooms[gameMap[x][y]][1] + " added to bag" )
            bag.add( rooms[gameMap[x][y]][1] )

    move = input( prompt )
    "check for valid move"

    if move not in moves:
        print( "Please use a valid move!" )
        continue

    "give user view of bag"
    if move == "bag":
        print( bag )
        print( "You have " + str( len( bag ) ) + " items" )
        print( str( 8 - len( bag ) ) + " to go" )

    "display room info"
    if move == "rooms":
        for key in rooms.keys( ):
            print( str( key ) + ": " + rooms[key][0] )

    "Show user the map"
    if move == "map":
        printPlayer( gameMap, playerPos[0], playerPos[1] )

    "west move"
    if move == "left":
        if playerPos[1] == 0:
            print( "can not leave bunker" )
            continue

        playerPos[1] -= 1

    "east move"
    if move == "right":
        if playerPos[1] == 5:
            print( "can not leave bunker" )
            continue
        playerPos[1] += 1

    "north move"
    if move == "up":
        if playerPos[0] == 0:
            print( "can not leave bunker" )
            continue

        playerPos[0] -= 1

    "south move"
    if move == "down":
        if playerPos[1] == 2:
            print( "can not leave bunker" )
            continue
        playerPos[0] += 1

if len( bag ) == 8:
    print( "You made it! You WON! You had everything you needed to fight Evil. It was a flawless victory." )




