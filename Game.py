on = True

story = """
    Welcome to Castle Adventure!

    Before you stands an ominous black castle,
    it's tower vanishing into the clouds.
    You push open the heavy metal door—
    bats burst forth, quickly obscuring your view.
    You step inside, finding yourself in the vast,
    echoing room.

    """
print(story)

player = 'MainHall'
key = False
    #slaughterroom checks
CrazyMan = True
DoorCheck = False
SlaughterRoomCheck = False
DoorUnlock = False
    #jail cells checks
manFree = False
info = False

    #vampire section
SeenCoffin = False
Sword = False

while on:
    if player == "MainHall":
        if not SlaughterRoomCheck:
            print("""
        "Before you stands 3 paths."
                  
        1. Left door (kitchen?).
        2. Staircase up.
        3. Right closed door.
        """)
        else:
            print("""
        "Before you stands 3 paths."
                  
        1. Slaughter Room.
        2. Staircase up.
        3. Right closed door.
        """)

        choice = input("Which path do you choose? ")

        if choice == '1':
            player = "SlaughterRoom"
        elif choice == '2':
            player = "VampireStairs"
        elif choice == '3':
            player = "CellularDoor"


    ############################
        #SlaughterRoom Section
    elif player == "SlaughterRoom":
        if CrazyMan:
            SlaughterIntro = """
            "You proceed to what you think is a kitchen."
            "But quickly you realize this is a slaughter room."
            "A man with a hatchet charges at you!"
            "You swiftly dodge the attack, countering the clumsy man."
            "Striking him down, before he lets out an unknown language."
            "After catching your breath, you scan the room."
            "Nothing but blood and guts everywhere,"
            "the sight would make any sane person throw up."
                    """
            print(SlaughterIntro)
            CrazyMan = False
            SlaughterRoomCheck = True
        else:
            AfterIntro = """
        "You Look around the Slaughter Room." 

        1. Search the man.
        4. Leave the horrid room.
                    """
            
                # OP 1 Searching man
            print(AfterIntro)
            action = input("What do u decide to do?")
            if action == '1':
                #1st time checking body 
                if not key:
                    #did check locked door
                    if DoorCheck:
                        print("You find a key. Maybe it unlocks that door.")
                        key = True
                    #didnt check locked door
                    else:
                        print("You find a key. You wonder what it is for.")
                        key = True
                #2nd time checking body
                else:
                    print("You find nothing more but the smell of old blood...")
            elif action == '4':
                print("You leave the dreadful room.")
                player = 'MainHall'
    ############################        

            


    ############################ 
            #Vamppire's Entrance     
    elif player == "VampireStairs":
        if info:
            VampEntWithInfo = """
        "You proceed up the staircase, you feel a strong pulsing
        through your body. As if every fiber in your being is telling you
        to turn back.
                This is where the vampire is."

        1. Enter.
        2. Go back.
            """
            print(VampEntWithInfo)
            EntranceAction = input()
            if EntranceAction == '1':
                player = "VampireCoffin"
            else:
                player = "MainHall"

        else:
            VampEntWithNoInfo = """
        "You proceed up the staircase, you feel a strong pulsing
        through your body. As if every fiber in your being is telling you
        to turn back.

        Maybe you should turn back."

        1. Nah, lets go in anyway, what's the worst that can happen!
        2. Go back.
            """
            print(VampEntWithNoInfo)
            EntranceAction = input()
            if EntranceAction == '1':
                player = "VampireCoffin"
            else:
                player = "MainHall"

    ############################

            #Vampire Coffin Room
    elif player == "VampireCoffin":
        if SeenCoffin:
            Coffin = """
        "You enter the room with the coffin."

        1. Approach the coffin.
        2. Find that the room's door.
        3. Go back to MainHall.

            """
            print(Coffin)
            CoffinActions = input()
            if CoffinActions == '1':
                player = "Coffin"
            elif CoffinActions == '2':
                player = "VampRoom"
            else:
                player = "MainHall"   

        elif info:
            CoffinIntro = """
        "You enter a vast chamber, making you feel small in comparison.
        In the dead center, there is a coffin resting on a dais.
        This is where the vampire is sleeping.
        Remembering what the man said, you know you should not open the coffin."

        1. Approach the coffin.
        2. Find the room's door.
        3. Go back to the MainHall.

            """
            print(CoffinIntro)
            SeenCoffin = True
            CoffinActions = input()
            if CoffinActions == '1':
                player = "Coffin"
            elif CoffinActions == '2':
                player = "VampRoom"
            else:
                player = "MainHall"
        
            # no Info and no Sword
        else:
            UnknownIntro = """
        "You enter a vast chamber, making you feel small in comparison.
        In the dead center there is a coffin resting on a dais."

        1. Approach coffin.
        2. Look around.
        3. Go back.
     """
            print(UnknownIntro)
            UnknownActions = input("Choose an action: ")
            if UnknownActions == '1':
                player = "Coffin"
            elif UnknownActions == '2':
                player = "VampRoom"
            else:
                player = "MainHall"

        
    ############################

    ############################
            #Coffin
    elif player == "Coffin":
        if Sword:
            print("You win!" \
            "Update coming soon")
        else:
            BadEnding = """
        You approach the coffin, without thinking you
        remove the top.
    
            """
            print("You die!")

        print("Thank you for playing! " \
            "Update coming soon")
        exit()

    ############################

    ############################
            #Vampire's Room
    elif player == "VampRoom":
        if Sword:
            print("you find nothing more. You go back")
            player = "VampireCoffin"
        elif info:
            RoomIntro = """
        "You find the room the man told you about.
        Once inside, you begin searching for the sword.
        You discover it inside a cabinet.
        You go back."

        """
            print(RoomIntro)
            Sword = True
            player = "VampireCoffin"
        else:
            Room = """
        "You enter a fancy room.
        But you find nothing of special.
        You go back."
        """
            print(Room)
            player = "VampireCoffin"

    ############################


    ############################
            #CellularDoor
    elif player == "CellularDoor":
        if key:
                #checked door before
            if DoorCheck:
                print("You open the door")
                DoorUnlock = True
                Jailintro = '''
        "Upon looking inside you see a long hall way leading to
        a staircase leading down."

        1. Do you proceed inside.
        2. Go back.
                '''
                print(Jailintro)
                enter = input()
                if enter == '1':
                    player = "Cellular"
                else:
                    player = "MainHall"
                #didn't check door
            else:
                DoorIntro = """
        "You try to open the door, but it seems locked.
        However, you pull out the key you found
        and unlock the door."

                    """
                print(DoorIntro)
                DoorCheck = True
                DoorUnlock = True
                Jailintro = '''
        "Upon looking inside you see a long hall way leading to
        a staircase leading down."

        1. Do you proceed inside.
        2. Go back.
                '''
                print(Jailintro)
                enter = input()
                if enter == "1":
                    player = "Cellular"
                else:
                    player = "MainHall"
            #no key
        else:
            CellularDoorIntro = """
        "You approach the door and try to open it
        However it appears locked.
        You go back."
                """
            print(CellularDoorIntro)
            DoorCheck = True
            player = "MainHall"

    ############################        

    ############################    
        #   Cellular
    elif player == "Cellular":
        if manFree:
            Cellur = """
        "You return to the now 'empty' cellular.
        Nothing of note to find."

        1. Go back to MainHall.
            """
            print(Cellur)
            jailActions = input("" )
            if jailActions == "1":
                player = "MainHall"
        else:
            CellurIntro = """
        "You enter a room that seems to be a jail cell block.
        Making your way past the cells, you notice they are either
        empty or filled with dead bodies.
        Near the end, you hear a faint cry—
        one of the cells has a soldier inside, barely clinging to life.
        He warns you of the monster that lives in the castle:
        it's a vampire. He then musters up the strength to say,
        'Do not open the coffin!'
        Adding that there is a sword...
        In the room behind the coffin, the army kept a blade
        that was able to pierce the monster's skin.
        Too exhausted to speak further, you break the cell's lock
        and carry the man back to the Main Hall."
            """
            print(CellurIntro)
            manFree = True
            info = True
            player = "MainHall"

    ############################      

