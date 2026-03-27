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

        #starting location
player = 'MainHall'

########################################################

                        #Checks
        #slaughterroom
CrazyMan = True
SlaughterRoomCheck = False
Girl = False

        #cellar door
DoorUnlock = False
DoorCheck = False
key = False

        #prisoner
manFree = False
info = False

        #coffin
SeenVampire = False
SeenCoffin = False
sword = False

########################################################

while on:

########################################################

        #MainHall options
    if player == "MainHall":

            #   Default
        if not SlaughterRoomCheck:
            print("""
        "3 paths are before you."
                  
        1. Left door (kitchen?).
        2. Staircase forward.
        3. Right closed door.
        """)
            
            #   Unlocked Door
        elif DoorUnlock:
            print("""
        "3 paths are before you."
                  
        1. Slaughter Room.
        2. Staircase forward.
        3. Cellar.
        """)
            
            #   Seen Kitchen
        else:
            print("""
        "3 paths are before you."
                  
        1. Slaughter Room.
        2. Staircase forward.
        3. Right closed door.
        """)

        choice = input("Which path do you choose? ")

        if choice == '1':
            player = "SlaughterRoom"
        elif choice == '2':
            player = "VampireStairs"
        elif choice == '3':
            player = "CellarDoor"


########################################################


        #SlaughterRoom Section
    elif player == "SlaughterRoom":

            #1st encounter in kitchen
                #man = dead, location = update
        if CrazyMan:
            SlaughterIntro = """
        "You proceed to what you think is a kitchen.
        But quickly you realize this is a slaughter room.
        A man with a hatchet charges at you!
        You swiftly dodge the attack, countering the clumsy man.
        Striking him down, before he lets out an unknown language.
        After catching your breath, you scan the room.
        Nothing but blood and guts everywhere,
        the sight would make any sane person throw up."
                    """
            print(SlaughterIntro)
                #updates
            CrazyMan = False
            SlaughterRoomCheck = True
            
        elif manFree:
            GirlsIntro = """
        "You approach the room's door, hearing strange noises from within...
        Peering inside, you are met with a grotesque sight:
        a small, sweet-looking girl feasting on one of the bodies.

        She is far too engrossed to notice you watching."

        1. Comfront her!
        2. Leave quietly.
                """
            print(GirlsIntro)

            action = input("What do you decide to do?")
            if action == '1':
                if sword:
                    GoodEnding = """
        "You charge at the girl, hoping she is too distracted to react...
            
                Success! 

        Your sword impales her through the back.
        With a face of horror, she stares at the blade lodged in her body...
            
        Slowly, she lifts her eyes to meet yours, letting out a chilling grin.

                "You idiot... you think this dull sword can kill me?"

        She tries tp pull the weapon out, but her hands burn from touching it.
        In pain, she screams:

                "What... how is this possible!"

        With a final lunge, you drive the sword deeper in, killing her.

        Returning back to the main hall, you help the wounded solider out.
        The story ends

                                You Win!
            "    
                """
                    print(GoodEnding)
                    exit()

                else:
                    BadEnding = """
        "You charge at the girl, hoping she is too distracted to react...
            
                Success! 

        Your sword impales her through the back.
        With a face of horror, she stares at the blade lodged in her body...
            
        Slowly, she lifts her eyes to meet yours, letting out a chilling grin.

                "You idiot... you think this dull sword can kill me?"

        She pulls the weapon out as if removing a bandage.
        Too shocked to move, you freeze as she lunges forward and sinks her teeth into your neck.

                                You Die!
            "    
                """
                    print(BadEnding)
                    exit()                

            else:
                print("You leave returning to the main hall.")
                player = 'MainHall'



            # after encounter
        else:
            AfterIntro = """
        "You Look around the Slaughter Room." 

        1. Search the man.
        2. Search around.
        3. Leave the horrid room.
                    """
            
                # 1 - Searching man
            print(AfterIntro)
            action = input("What do u decide to do?")
            if action == '1':

                # 1st time
                    #getting key 
                if not key:
                        #did check locked door
                    if DoorCheck:
                        print("You find a key. Maybe it unlocks that door.")
                        key = True
                        #didnt check locked door
                    else:
                        print("You find a key. You wonder what it is for.")
                        key = True

                #2nd time
                else:
                    print("You find nothing more but the smell of old blood...")

                # 2 - Searching around

            elif action == '2':

                # 1st time
                    #seeing girl
                if not Girl:
                    GirlIntro = """
        "You search around, nothing but dead bodies,
        upon investigating one of them, you notice
        two strange marks on the victim's neck...
        Suddenly, you hear rattling coming from a cabinet.
        Opening the doors you discover a young girl.
        She lunges at you, crying:

                "Thank you, sir! I was so terrified I was next!"

        Through her tears, you notice she is wearing a dress
        however it doesn't have a single drop of blood on it.

        You quickly take the girl out of the room, back to the main hall.

        You suggest that she leave the castle at once.
        However she says:

                "Sir, but it's too scary to wander outside,
                 I will stay here until you are finished."

        Seeing no other option, you agree.

                    You are in the MainHall
        """
                    print(GirlIntro)
                    Girl = True
                    player = 'MainHall'

                # 2nd time
                    #no girl
                else:
                    print("You discover nothing more.")


                # 3 - Searching around

            else:
                print("You leave the dreadful room.")
                player = 'MainHall'

    ########################################################        

            


    ########################################################
            #Vampire's Entrance     
    elif player == "VampireStairs":

            # going up 2nd time
        if SeenVampire:
            Info = """
        "You proceed up the staircase,
            """
            player = "VampireCoffin"

            # going up 1st time with info
        elif info:
            print("You go up the stairs to the coffin.")
            player = "VampireCoffin"

            #1st time entering (no info)
        else:
            NoInfo = """
        "You proceed up the staircase, you feel a strong pulsing
        through your body. As if every fiber in your being is telling you
        to turn back.

        Maybe you should turn back."

        1. Nah, lets go in anyway, what's the worst that can happen!
        2. Go back.
            """
            print(NoInfo)
            EntranceAction = input()
            if EntranceAction == '1':
                player = "VampireCoffin"
            else:
                player = "MainHall"

    ########################################################

            #Vampire Coffin Room
    elif player == "VampireCoffin":

            # 2nd time BUT no info
        if SeenVampire:
            Coffin = """
        "You enter the room with the coffin."

        1. Approach the coffin.
        2. Look around.
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

                # 2nd time AND info
        elif info and SeenCoffin:
            Coffin = """
        "You enter the room with the coffin."

        1. Approach the coffin.
        2. Find the room's door.
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

                # 1st time WITH info
        elif info:
            CoffinIntro = """
        "You enter a vast chamber, making you feel small in comparison.
        In the dead center, there is a coffin resting on a dais."

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
        

            # 1st time AND no Info 
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

        
    ########################################################

    ########################################################
                        #Coffin

    elif player == "Coffin":
            # Seen dead vampire
        if SeenVampire:
            print("\"Still a very dead vampire in the coffin\"")
            player = "VampireCoffin"

            #1st time seeing vampire
        else:
            VampireIntro = """
        "You approach the coffin, removing the pall
        You find a very old man sleeping inside...
        Observing him further it seems as if he is dead.
        Nothing more to say."

                You go back.
            """
            print(VampireIntro)
            SeenVampire = True
            player = "VampireCoffin"

    ########################################################



    ########################################################

                        #Vampire's Room

    elif player == "VampRoom":

                # 2nd (has sword)
        if sword:
            print("\"You find nothing more. You go back\"")
            player = "VampireCoffin"

                # 1st time with info 
        elif info:
            RoomIntro = """
        "You find the room the man told you about.
        Once inside, you begin searching for the sword.
        You discover it inside a cabinet.
        You go back."
            """
            print(RoomIntro)
            sword = True
            player = "VampireCoffin"

                # 1st time with no info
        else:
            Room = """
        "You enter a fancy room.
        But you find nothing of special.
        You go back."
            """
            print(Room)
            player = "VampireCoffin"

    ########################################################



    ########################################################
                        #CellarDoor

    elif player == "CellarDoor":
            # has key      
        if key:
        #2nd time entering
            if manFree:
                Jailintro = '''
        "Staircase to jail cells."

        1. Go down.
        2. Go back.
                '''
                print(Jailintro)
                enter = input()
                if enter == '1':
                    player = "Cellar"
                else:
                    player = "MainHall"

        #1st time entering
                    # AND
                #checked door before
            elif DoorCheck:
                print("\"You open the door with the key...\"")
                DoorUnlock = True
                Jailintro = '''
        "Upon looking inside you see a long hallway leading to
         a staircase leading down."

        1. Do you proceed inside?
        2. Go back.
                '''
                print(Jailintro)
                enter = input()
                if enter == '1':
                    player = "Cellar"
                else:
                    player = "MainHall"

                    # BUT
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
        "Upon looking inside you see a long hallway leading to
        a staircase leading down."

        1. Proceed inside?
        2. Go back.
                '''
                print(Jailintro)
                enter = input()
                if enter == "1":
                    player = "Cellar"
                else:
                    player = "MainHall"

            #NO key
        else:
            CellarDoorIntro = """
        "You approach the door and try to open it
        However it appears locked.
        You go back."
                """
            print(CellarDoorIntro)
            DoorCheck = True
            player = "MainHall"

    ########################################################        



    ########################################################    
                        #   Cellar

    elif player == "Cellar":
                # Released man
        if manFree:
            Cellar = """
        "You return to the now 'empty' cellar.
        Nothing of note to find."

        1. Go back to main hall.
            """
            print(Cellar)
            jailActions = input("" )
            if jailActions == "1":
                player = "MainHall"

                # 1st time meeting man

                    # Have NOT seen girl
                    # Have NOT seen vampire
        elif not Girl and not SeenVampire:
            CellarIntro1 = """
        "You enter a room that seems to be a jail cell block.
        Making your way past the cells, you notice they are either
        empty or filled with dead bodies.
        Near the end, you hear a faint cry—
        one of the cells has a soldier inside, barely clinging to life.
        He warns you of the monster that lives in the castle:
        it's a vampire. He then musters up the strength to say:

                "Be careful of the little girl, she is an abomination of horror!"
        
        He goes on telling you of a sword hidden within the vampire's chambers
        that is able to pierce the girl's skin.
        Saying not to face her without it.

        You break the jail cell's door and carry the man back to the main hall.

                You are in the main hall.

            """
            print(CellarIntro1)
            manFree = True
            info = True
            player = "MainHall"


                    # Have seen girl
                    # Have NOT seen vampire
        elif Girl and not SeenVampire:
            CellarIntro2 = """
        "You enter a room that seems to be a jail cell block.
        Making your way past the cells, you notice they are either
        empty or filled with dead bodies.
        Near the end, you hear a faint cry—
        one of the cells has a soldier inside, barely clinging to life.
        He warns you of the monster that lives in the castle: a vampire.
        He then musters up the strength to say:

                "Be careful of the little girl, she is an abomination of horror!"

        You interrupt the man to say that you have already met the girl
        and she is upstairs.

        The man's eyes widen in shock.
        
                "How are you still alive?"

        He goes on telling you of a sword hidden within the vampire's chambers
        that is able to pierce the girl's skin.
        Saying not to face her without it.

        You break the jail cell's door and carry the man back to the cellar's door.
        You slowly open the door finding that the girl is nowhere to be seen.

                You are in the main hall.

        """
            print(CellarIntro2)
            manFree = True
            info = True
            player = "MainHall"


                    # Have NOT seen girl
                    # Have seen vampire
        elif not Girl and SeenVampire:

            CellarIntro3 = """
        "You enter a room that seems to be a jail cell block.
        Making your way past the cells, you notice they are either
        empty or filled with dead bodies.
        Near the end, you hear a faint cry—
        one of the cells has a soldier inside, barely clinging to life.
        He warns you of the monster that lives in the castle:
        it's a vampire. He then musters up the strength to say:

                "Be careful of the abomination upstairs."

        You interrupt him, explaining that you have already encountered 
        the vampire and that he now lies dead in his coffin. 
        He slowly nods his head...

                "It is a little girl..."

        He goes on telling you of a sword hidden within the vampire's chambers
        that is able to pierce the girl's skin.
        Saying not to face her without it.

        You break the jail cell's door and carry the man back to the main hall.

                You are in the main hall.
        """
            print(CellarIntro3)
            manFree = True
            info = True
            player = "MainHall"

                    # Have seen girl
                    # Have seen vampire
        else :
            CellarIntro4 = """
        "You enter a room that seems to be a jail cell block.
        Making your way past the cells, you notice they are either
        empty or filled with dead bodies.
        Near the end, you hear a faint cry—
        one of the cells has a soldier inside, barely clinging to life.
        He warns you of the monster that lives in the castle:
        it's a vampire. He then musters up the strength to say:

                "Be careful of the abomination upstairs."

        You interrupt him, explaining that you have already encountered 
        the vampire and that he now lies dead in his coffin. 
        He slowly nods his head...

                "It is a little girl..."

        You pause, telling him you have seen her as well...
        she is upstairs.

        The man's eyes widen in shock.
        
                "How are you still alive?"

        He goes on telling you of a sword hidden within the vampire's chambers
        that is able to pierce the girl's skin.
        Saying not to face her without it.

        You break the jail cell's door and carry the man back to the cellar's door.
        You slowly open the door finding that the girl is nowhere to be seen.

                You are in the main hall.

        """
            print(CellarIntro4)

            manFree = True
            info = True
            player = "MainHall"

    ############################      

