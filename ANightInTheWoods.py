########################################################
#Imports, music initialization and inventory initialization

import sys
import os
new_directory = "C:\\Users\\kcoe2\\OneDrive\\Desktop\\Games\\A Night in the Woods"
pygame_path = "C:\\users\\kcoe2\\appdata\\local\\programs\\python\\python39\\lib\\site-packages"
os.chdir(new_directory)
sys.path.append(pygame_path)
import pygame
import time
inventory = []
hiddenInventory = []
endings = []

#Imports, music initialization and inventory initialization
########################################################


########################################################
#Intial steup for A Night Among the Trees

def setupGameMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("electric-forest-168971.mp3")
    pygame.mixer.music.play(-1)
    inventory.append("employee keycard")
    inventory.append("factory key")

def printTitle():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("     /\\                          /\\")
    print("    /  \\                        /  \\")
    print("   --  --                      --  --")
    print("   /    \\          A           /    \\")
    print("  /      \\       Night        /      \\")
    print("  --    --       Among        --    --")
    print("  /      \\        the         /      \\")
    print(" /        \\      Tress       /        \\")
    print(" ----------                  ----------")
    print("    |  |                        |  |")
    print("    |  |                        |  |")
    print("    |  |                        |  |")
    print("    |  |                        |  |")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def startGame():
    print("Ready to walk among the trees?")
    if len(endings) != 0:
        print("(You can also type 'endings' to see what endings you have found!)")
    user_input = input("Your answer: ")
    if user_input == "yes" or "Yes" or "YES":
        print("The trees await...")
        pygame.mixer.music.fadeout(3000)
        time.sleep(3)
    elif user_input == "no":
        print("Perhaps the wise choice...")
        time.sleep(3)
        pygame.mixer.music.stop()
        sys.exit()
    elif user_input == "endings":
        endingsFound()
    else:
        print("The trees do not take kindly to that response...")
        startGame()

def endingsFound():
    print("\nYou have found the following endings:\n")
    if 1 in endings:
        print("Ending 1: A Watery Grave")
    elif 2 in endings:
        print("Ending 2: An Ungrateful Guest")
    elif 3 in endings:
        print("Ending 3: Too Much of a Good Thing")
    elif 4 in endings:
        print("Ending 4: The Hunter")
    elif 5 in endings:
        print("Ending 5: Harvested")
    elif 6 in endings:
        print("Ending 6: Slip and Fall")
    elif 7 in endings:
        print("Ending 7: One Day My Bus Will Come")
    elif 8 in endings:
        print("Ending 8: A Sudden Shock")
    print("\nTry to reach them all! Good luck.")
    input("Press enter to return to the title screen.")
    startGame()

def startingArea():
    print("\nYou are waiting for the bus after a long day of work.")
    print("The bus stop is empty except for you. Everyone else left work long ago.")
    print("But you closed the factory up for the winter, and now you wait alone.\n")
    time.sleep(10)
    print("The road is empty.\n")
    print("------------------------")
    print("\n")
    print(" --  --  --  --  --  --")
    print("\n")
    print("------------------------")
    time.sleep(3)
    print("\nThere is no bus in sight. The schedule says two should have come by now,\nyet no bus has traveled by.")
    print("The bus stop has a schedule and bench for you to rest on.")
    if "electricity" not in hiddenInventory:
        print("The bus stop is supposed to be illumated by a streetlight, but it isn't on.")
        print("Given the remote location, the light is powered by the factory generator, but the factory is closed.")
    else:
        print("The bus stop is illumated by a streetlight, allowing for an oasis of light in the dark.")
        print("Given the remote location, the light is powered by the factory generator.")
    time.sleep(8)
    print("\nTo your north is the road leading to the lumber factory where you work.")
    print("And to the east and west of you is a road stretching far beyond what your\neyes can see.")
    print("And surrounding all else...")
    time.sleep(8)
    pygame.mixer.music.load("Haunted Forest Sounds  Ghostly Murmurs  1 Hour.mp3")
    pygame.mixer.music.play(-1)
    print("The Woods.")
    time.sleep(8)
    startingChoice()

def startingChoice():
    if "electricity" in hiddenInventory and "lamp notice" not in hiddenInventory:
        print("\nAs you return to the bus stop you notice the streetlight is now on.")
        hiddenInventory.append("lamp notice")
        time.sleep(2)
    print("\nWhat would you like to do?")
    print("1. Wait for the bus.")
    print("2. Take a nap on the bench.")
    print("3. Walk down the road to the east.")
    print("4. Walk down the road to the west.")
    print("5. Walk towards the lumber factory.")
    print("6. Walk into the woods.")
    print("7. Check the items you have.")
    print("The trees demand that you answer with a single number.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForBus()
    elif user_input == "2":
        napTime()
    elif user_input == "3":
        lonelyBeaver()
    elif user_input == "4":
        rockslide()
    elif user_input == "5":
        factoryOutside()
    elif user_input == "6":
        woods()
    elif user_input == "7":
        print("\nYou check to see what you have.")
        time.sleep(3)
        print("\nYou currently have the following things:\n")
        for i in inventory:
                print(i)
        time.sleep(3)
        startingChoice()
    else:
        print("The trees are not pleased...")
        startingChoice()

#Intial steup for A Night Among the Trees
########################################################


########################################################
#Option 1: Wait for the bus

def waitForBus():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nIt doesn't seem like it's coming.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Wait some more.")
    print("2. Reconsider your options.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForBus2()
    else:
        print("\nYou realize the bus isn't coming.")
        startingChoice()

def waitForBus2():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nIt doesn't seem like it's coming.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Wait some more.")
    print("2. Reconsider your options.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForBus3()
    else:
        print("\nYou realize the bus isn't coming.")
        startingChoice()

def waitForBus3():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nIt doesn't seem like it's coming.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Wait some more.")
    print("2. Reconsider your options.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForBus3half()
    else:
        print("\nYou realize the bus isn't coming.")
        startingChoice()

def waitForBus3half():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nIt doesn't seem like it's coming.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Wait some more.")
    print("2. Reconsider your options.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForBus4()
    else:
        print("\nYou realize the bus isn't coming.")
        startingChoice()

def waitForBus4():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nDark purple headlights appear on the horizon.")
    time.sleep(3)
    print("\nA bus you've never seen before rolls up to the bus stop.")
    print('The design on its side reads "The Midnight Bus".\n')
    time.sleep(3)
    print("     _______________________________         ")
    print("    /_______________________________\\       ")
    print("    |    |    |    |    |  _____  |  |       ")
    print("    |____|____|____|____| |  |  | |__|       ")
    print("    |  THE MIDNIGHT BUS   |  |  |    |       ")
    print("    |_____________________|__|__|____|       ")
    print("-------|_|__|-----------------|_|__|---------")
    print("\n")
    print(" --  --  --  --  --  --  --  --  --  --  --  ")
    print("\n")
    print("---------------------------------------------")
    time.sleep(2)
    print("\nIts doors roll open, inviting you in.")
    print("But you cannot see the inside, its pitch black.")
    time.sleep(3)
    hiddenInventory.append("bus")
    print("\nWhat would you like to do?")
    print("1. Board the midnight bus.")
    print("2. Wait for the REAL bus.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou step onboard, and the doors close behind you.")
        print("The midnight bus start driving down the road.")
        time.sleep(3)
        midnightBus()
    else:
        print("\nThis is not your bus. You wait for it to go along its way.")
        time.sleep(3)
        waitForBus5()

def waitForBus5():
    print("\nYou wait for the bus.")
    time.sleep(8)
    print("\nYour bus REALLY doesn't seem to be coming.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. STILL continue to wait for your bus.")
    print("2. Reconsider your options.")
    user_input = input("I would like to... ")
    if user_input == "1":
        waitForever()
    else:
        print("\nYou realize the bus isn't coming.")
        startingChoice()

def waitForever():
    print("\nYou are steadfast. You are not moving from this spot until your bus comes.")
    time.sleep(3)
    print("And wait you do. You wait countless hours for your bus, but it never arrives.")
    print("You collapse due to dehydration. But you die peacefully knowing one day...")
    time.sleep(6)
    print("the bus will come.")
    time.sleep(3)
    gameOver(7)
    

def midnightBus():
    pygame.mixer.music.load("analogmannequin - milk cassette x.mp3 (1 hour loop).mp3")
    pygame.mixer.music.play(-1)
    print("\nThe bus starts rolling down the road.")
    time.sleep(3)
    print("\nAfter you board you notice there is only you, the driver, and one other")
    print("passenger about 3 rows ahead of the back.")
    print("The driver looks normal enough.")
    print("They're wearing a dark purple button down with a black tie and black pants.")
    print("They look to be about 50 and have a clean shaven face.")
    print("The passenger is staring out the window and looks to be a teenage girl.")
    print("She is wearing a large pale red hoodie.")
    print("The bus itself is lit by purple lighting and the seats look awfully cozy.")
    print("Windows line the sides, allowing you to see the dark woods outside as the bus rushes past.")
    time.sleep(12)
    print("\nThe driver turns to you.")
    print('"Bus pass please."')
    time.sleep(3)
    print("\nYou stare at him in confusion. You don't know about any 'bus pass'.")
    time.sleep(3)
    print("\nWhat do you do?")
    print("1. Give him something you have.")
    print("2. Inform him that you don't have a bus pass.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou check to see what you have.")
        time.sleep(3)
        print("\nYou currently have the following things:\n")
        for i in inventory:
                print(i)
        print("\nWhat would you like to show them?")
        print("The trees demand that you answer with an item, such as 'employee keycard'.")
        user_input2 = input("I would like to show them my... ")
        if user_input2 == "notebook":
            print("\nThe driver slowly nods.")
            time.sleep(3)
            print('"\nWelcome. Ride as long as you'+"'"+'d like."')
            time.sleep(3)
            boardedChoice()
        else:
            pygame.mixer.music.load("-110063.mp3.")
            pygame.mixer.music.play()
            print("\nThe driver slams on the breaks.")
            time.sleep(3)
            print('"You mean to tell me that you did not bring your pass?"')
            time.sleep(3)
            print("\nYou look around, unsure of what to say.")
            time.sleep(3)
            print("\nSuddenly you can't see anything.")
            print("You back up in confusion, but you don't bump into the side of the bus.")
            time.sleep(5)
            print("You try to run but you still make no contact with anything.")
            print("You scream, but your cries accomplish nothing.")
            print("You try to feel for the floor, but you feel nothing, as if nothing was there.")
            time.sleep(6)
            print("You are never seen again.")
            time.sleep(3)
            voidEnding()
    if user_input == "2":
        print("\nYou let them know you don't have a bus pass.")
        time.sleep(3)
        pygame.mixer.music.load("-110063.mp3.")
        pygame.mixer.music.play()
        print("\nThe driver slams on the breaks.")
        time.sleep(3)
        print('"You mean to tell me that you did not bring your pass?"')
        time.sleep(3)
        print("\nYou look around, unsure of what to say.")
        time.sleep(3)
        print("\nSuddenly you can't see anything.")
        print("You back up in confusion, but you don't bump into the side of the bus.")
        time.sleep(5)
        print("You try to run but you still make no contact with anything.")
        print("You scream, but your cries accomplish nothing.")
        print("You try to feel for the floor, but you feel nothing, as if nothing was there.")
        time.sleep(6)
        print("You are never seen again.")
        time.sleep(3)
        voidEnding()
    else:
        print("\nYou stare at them, not moving.")
        time.sleep(3)
        pygame.mixer.music.load("-110063.mp3.")
        pygame.mixer.music.play()
        print("\nThe driver slams on the breaks.")
        time.sleep(3)
        print('"You mean to tell me that you did not bring your pass?"')
        time.sleep(3)
        print("\nYou look around, unsure of what to say.")
        time.sleep(3)
        print("\nSuddenly you can't see anything.")
        print("You back up in confusion, but you don't bump into the side of the bus.")
        time.sleep(5)
        print("You try to run but you still make no contact with anything.")
        print("You scream, but your cries accomplish nothing.")
        print("You try to feel for the floor, but you feel nothing, as if nothing was there.")
        time.sleep(6)
        print("You are never seen again.")
        time.sleep(3)
        voidEnding()

def boardedChoice():
    print("\nWhat would you like to do?")
    print("1. Chat with the bus driver.")
    print("2. Strike up a conversation with the other rider.")
    print("3. Go stit down.")
    user_input = input("I would like to... ")
    if user_input == "1":
        driver()
    elif user_input == "2":
        passenger()
    elif user_input == "3":
        print("\nYou go sit down in an empty seat.")
        time.sleep(3)
        seat()
    else:
        print("\nYou mull over your options.")

def driver():
    pass

def passenger():
    pass

def seat():
    print("\nWhat would you like to do?")
    print("1. Reflect on your current situation.")
    print("2. Check the notebook, err, bus pass.")
    print("3. Stand up and do something else.")
    user_input = input("I would like to... ")
    if user_input == "1":
        reflect()
    elif user_input == "2":
        notebook()
    elif user_input == "3":
        print("You have had enough sitting and decide to do something else.")
        time.sleep(3)
        boardedChoice()
    else:
        print("\nYou consider what to do.")

def reflect():
    print("\nThis night has definitely turned into something else.")
    time.sleep(3)
    print("First off, you already had to close up the factory by yourself.")
    print("No one stuck around to help you.")
    print("\nAnd then the bus wasn't showing up.")
    if rockslide in hiddenInventory:
        print("That rockslide has completely cut you off any chance of it coming.")
    else:
        print("Why hasn't the bus come?")
    time.sleep(15)
    if figure in hiddenInventory:
        print("\nAnd that figure was very unnerving.")
        print("It's a miracle you were able to escape him.")
    time.sleep(6)
    if shop in hiddenInventory:
        print("\nAt least it was nice to see the old gift shop.")
        print("Even though there wasn't much to do there.")
    if backdoor in hiddenInventory:
        print("\nBut was with that backdoor? It's security was insane.")
        print("And for a gift shop backdoor?")
    time.sleep(6)
    print("\nAnd to top it all off you are now riding a mysterious bus.")
    time.sleep(3)
    print("\nYou stare out the window sprinkled with rain, contemplating the night's events.")
    time.sleep(2)
    print(" _____________________ ")
    print("[   / \\*/ \\  / \\ */ \\ ]")
    print("[ * --- -*-  --*  --- ]")
    print("[   *|   |*   | *  | *]")
    print("[  * |   |    |*   |  ]")
    print("[^^*^^^^^^*^^^*^^^^^^^]")
    print("[__*_______*______*___]")
    time.sleep(6)
    print("\nAt least this is peaceful.")
    time.sleep(3)
    seat()
    

def notebook():
    if notebookRealize in hiddenInventory:
        print("\nJust as S told you, the notebook now shows writing upder the purple glow.")
    else:
        print("\nSomehow, the notebook now has writing in it.")
    print("There seems to be X entries.")
    time.sleep(6)
    print("What would you like to do?")
    print("1. Read the first entry.")
    print("2. Read the second entry.")
    print("3. Read the third entry.")
    print("4. Read the fourth entry.")
    print("5. Do something else.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nThis is what is reads:")
        time.sleep(3)
        notebookFont()
        entryOne()
    elif user_input == "2":
        print("\nThis is what is reads:")
        time.sleep(3)
        notebookFont()
        entryTwo()
    elif user_input == "3":
        print("\nThis is what is reads:")
        time.sleep(3)
        notebookFont()
        entryThree()
    elif user_input == "4":
        print("\nThis is what is reads:")
        time.sleep(3)
        notebookFont()
        entryFour()
    elif user_input == "5":
        print("\nYou decide to do something else.")
        seat()
    else:
        print("\nThis is all so wild.")
        notebook()

def notebookFont():
    pygame.init()
    teen_font = pygame.font.SysFont("Inkfree.ttf", 36)
    return

def entryOne():
    print("\n\n\n")
    teen_font.render("This is the text you want to display with the custom font.", True, (0, 0, 0))
    return
        

#Option 1: Wait for the bus
########################################################


########################################################
#Option 2: You sleep on the bench
def napTime():
    time.sleep(1)
    print("\nYou rest your head on the cold, metal bench.")
    print("Closing your eyes, you try to not imagine all the horrors that\ncould be lurking in the woods.")
    print("You manage to fall asleep.")
    time.sleep(8)
    print("\nYou open your eyes after some time, still tired despite your slumber.")
    time.sleep(4)
    print("A shadowy figure stands across the road from you.\n")
    hiddenInventory.append("figure")
    time.sleep(4)
    print("           --  ")
    print("          /oo\\ ")
    print("      |  /    \\")
    print("      ---|    |")
    print("      |  |    |")
    print("      |  ......")
    print("------------------------")
    print("\n")
    print(" --  --  --  --  --  --")
    print("\n")
    print("------------------------")
    time.sleep(3)
    print("\nThey were not there when you fell asleep.\n")
    time.sleep(3)
    print("They stand motionless. You are unable to make out any of their details.")
    print("But their eyes seem to study every inch of your body, sending a shiver\ndown your spine.\n")
    time.sleep(5)
    napChoice()
    
def napChoice():
    print("What would you like to do?")
    print("1. Ignore them.")
    print("2. Approach them.")
    print("3. Say something to them.")
    print("4. Run away.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou ignore their presence, hoping they go away.")
        chased()
    elif user_input == "2":
        print("\nYou walk towards the figure.")
        time.sleep(3)
        print("\nYou're steps away from them, when suddenly they raise their staff")
        print("and swing at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
    elif user_input == "3":
        print('\nYou shout at them, "Hey, who are you?"')
        time.sleep(3)
        print("\nThey do not reply.")
        time.sleep(3)
        print("\nYou start walking towards them.")
        time.sleep(3)
        print('\n"I don'+"'"+'t want any trouble," you shout.')
        time.sleep(3)
        print("\nThey do not reply.")
        time.sleep(3)
        print('"\nIf you think you can jump me you got another thing-"')
        print("But before you can finish, they rush towards you, rasing their staff.")
        time.sleep(4)
        print("\nThey swing at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
    elif user_input == "4":
        print("\nYou turn and run from them.")
        chased()
    else:
        print("\nThe figure stands still.")
        time.sleep(3)
        napChoice()

def chased():
    time.sleep(3)
    print("\nThey begin approaching you, gaining speed with each step.")
    pygame.mixer.music.load("suspense_strings_001wav-14805.mp3")
    pygame.mixer.music.play()
    time.sleep(3)
    print("You run for your life, running as fast as you can.")
    time.sleep(3)
    print("But they're gaining on you.")
    time.sleep(2)
    pygame.mixer.music.load("Haunted Forest Sounds  Ghostly Murmurs  1 Hour.mp3")
    pygame.mixer.music.play()
    chasedChoice()

def chasedChoice():
    print("\nWhat would you like to do?")
    print("1. Stop and allow them to reach you.")
    print("2. Kepp running!")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou stop, and within moments they are upon you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swings at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
    elif user_input == "2":
        print("\nYou run like your life depends on it. And perhaps it does.")
        time.sleep(3)
        log()
    else:
        print("Your indecisiveness has allowed them to reach you.")
        time.sleep(3)
        print("There is no running away now.")
        print("They are upon you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swings at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()

def log():
    print("\nAs you run, a large log blocks your path.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Jump over the log.")
    print("2. Run around the log.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou swiftly jump over the log, hoping to gain some distance")
        print("between you and the shadowy figure.")
        time.sleep(3)
        print("But they jump over it too.")
        time.sleep(3)
        creek()
    elif user_input == "2":
        print("\nYou try to run around the log, but the ground is wet and muddy.")
        time.sleep(3)
        print("You slip and fall. Within moments the figure stands over you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swing at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
    else:
        print("Your indecisiveness has allowed them to reach you.")
        time.sleep(3)
        print("There is no running away now.")
        print("They are upon you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swings at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()

def creek():
    print("\nYou keep running and come upon a creek, darkened by night sky.")
    time.sleep(3)
    print("\nYou cannot see the bottom.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Run straight through the creek.")
    print("2. Hop across the rocks.")
    print("3. Stop and allow the shadowy figure to reach you.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou run straight through the creek.")
        print("Fortunately, the creek is shallow and the current is weak.")
        time.sleep(3)
        print("\nYou safely make it to the other side.")
        print("You turn back, and the figure has stopped as the edge of the creek.\n")
        time.sleep(3)
        print("           --  ")
        print("          /oo\\ ")
        print("      |  /    \\")
        print("      ---|    |")
        print("      |  |    |")
        print("      |  ......")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" ~~         ^^    ~~     ")
        print("      ^^  ~~  ^^    ~~   ")
        print("     ~~     ^^ ~~      ~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        time.sleep(3)
        print("\nYou lose sight of them.")
        print("And you suddenly realize you are lost among the trees.")
        woods()
    elif user_input == "2":
        print("\nYou try to hop across the rocks scattered across the creek.")
        print("But they are wet and slippery, and you fall straight in.")
        time.sleep(3)
        print("\nYou hit your head on a rock, and you lay facedown in the water.")
        print("Unconscious, you drown lost in the woods.")
        print("Never to be found.")
        time.sleep(5)
        gameOver(1)
    elif user_input == "3":
        print("\nYou stop at the creek, unsure of its misty waters.")
        print("And the figure is soon upon you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swing at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
    else:
        print("Your indecisiveness has allowed them to reach you.")
        time.sleep(3)
        print("There is no running away now.")
        print("They are upon you.")
        time.sleep(3)
        print("\nSuddenly, they raise their staff")
        print("and swings at your head, making contact.")
        time.sleep(3)
        print("\nYou fall unconscious.")
        pygame.mixer.music.fadeout(3000)
        time.sleep(5)
        shadowConvo()
        

def shadowConvo():
    time.sleep(6)
    pygame.mixer.music.load("Creepy Night in Abandoned Forest House with spooky sounds ASMR Ambience.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    print("\nYou wake up in an old shack, sitting at a table.")
    time.sleep(3)
    print("\nThe shack is dimly lit, creaking and moaning with every light breeze.")
    hiddenInventory.append("cabin")
    time.sleep(3)
    print("\nThe figure sits across from you.\n")
    time.sleep(3)
    print("             |              ")
    print("             |              ")
    print("             |              ")
    print("          ___|___            ")
    print("          \\_____/             ")
    print("            / \\           ")
    print("\n\n")
    print("            --  ")
    print("           /oo\\ ")
    print("          /    \\")
    print("     ____|______|____")
    print("    |                |")
    print("    |                |")
    print("    |________________|")
    print("        | |    | |    ")
    print("        | ...... |    ")
    print("\n")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Wait and see what they want.")
    print("2. Try to run away.")
    user_input = input("I would like to... ")
    if user_input == "1":
        pass
    elif user_input == "2":
        print("\nYou jump up and run for the door.")
        print("You reach the door and try to turn the knob.")
        time.sleep(4)
        print("\nIt's locked.")
        time.sleep(3)
        print("\nYou turn around and the figure is standing right in front of you.")
        time.sleep(4)
        print("\nHe strikes you with his staff, and you again fall unconscious.")
        print("You are never found.")
        time.sleep(3)
        gameOver(2)
    else:
        print("\nIt is not kindly of a guest to not respond appropriately...")
        print("You must now see what they want from you.")
        time.sleep(3)
    print("\nThey give you a bowl of slop.")
    print("It seems they want you to eat it.\n")
    time.sleep(3)
    print("      / ")
    print("  ___/_")
    print("  \\___/")
    time.sleep(3)
    print("\nIt does not look tasty.")
    slop()

def slop():
    print("\nWhat would you like to do?")
    print("1. Eat the suspicious slop.")
    print("2. Refuse the meal.")
    user_input = input("I would like to... ")
    if user_input == "1":
        pass
    elif user_input == "2":
        print("\nYou refuse to eat the generous meal.")
        time.sleep(1)
        print("\nThe figure slams down its feet, kicking their chair back, and stares down at you.")
        time.sleep(3)
        print("\nThey take their staff and swing at you in one swift motion, striking you")
        print("across the head.")
        time.sleep(3)
        print("\nYou again fall unconscious. You are never found.")
        time.sleep(3)
        gameOver(2)
    else:
        print("\nYou refuse to eat the generous meal.")
        time.sleep(1)
        print("\nThe figure slams down its feet, kicking their chair back, and stares down at you.")
        time.sleep(3)
        print("\nThey take their staff and swing at you in one swift motion, striking you")
        print("across the head.")
        time.sleep(3)
        print("\nYou again fall unconscious. You are never found.")
        time.sleep(3)
        gameOver(2)
    print("\nYou pick up a spoonful of the slop. It's sticky, oozing from all sides of the spoon.")
    print("It is a dark purple color, with black chunks floating in it.")
    time.sleep(5)
    print("\nA bubble bursts from the slop, and some lands on your hand.")
    print("It stings and irritates your skin.")
    time.sleep(5)
    print("\nDo you still eat the slop?")
    print("1. Eat the slop.")
    print("2. Put the spoon down and politely decline.")
    user_input2 = input("I would like to... ")
    if user_input2 == "1":
        pass
    elif user_input2 == "2":
        print("\nYou refuse to eat the generous meal.")
        time.sleep(1)
        print("\nThe figure slams down its feet, kicking their chair back, and stares down at you.")
        time.sleep(3)
        print("\nThey take their staff and swing at you in one swift motion, striking you")
        print("across the head.")
        time.sleep(3)
        print("\nYou again fall unconscious. You are never found.")
        time.sleep(3)
        gameOver(2)
    else:
        print("\nYou refuse as nicely as you can.")
        time.sleep(3)
        print("\nThe figure slams down its feet, kicking their chair back, and stares down at you.")
        time.sleep(3)
        print("\nThey take their staff and swing at you in one swift motion, striking you")
        print("across the head.")
        time.sleep(3)
        print("\nYou again fall unconscious. You are never found.")
        time.sleep(3)
        gameOver(2)
    print("\nYou bring the spoon to your mouth and take in a hearty serving of slop.")
    time.sleep(5)
    print("\nIt tastes like syrupy gasoline. You feel like you're about to throw up.")
    print("But you manage to gulp it down.")
    time.sleep(5)
    print("\nWhat would you like to do?")
    print('1. Say, "Thank you for the meal."')
    print("2. Eat another spoonful.")
    print("3. Do nothing.")
    user_input3 = input("I would like to... ")
    if user_input3 == "1":
        pass
    elif user_input3 == "2":
        print("\nYou scoop another spoonful of the slop, and eat it.")
        time.sleep(3)
        print("\nIt is worse than before. You cannot help but throw up all over the table.")
        time.sleep(3)
        print("\nThe figure slams down its feet, kicking their chair back, and stares down at you.")
        time.sleep(3)
        print("\nThey take their staff and swing at you in one swift motion, striking you")
        print("across the head.")
        time.sleep(3)
        print("\nYou again fall unconscious. You are never found.")
        time.sleep(3)
        gameOver(3)
    elif user_input3 == "3":
        pass
    print("\nThe figure says nothing.")
    time.sleep(3)
    print("\nThey get up and go into the connecting room. You are now alone.\n")
    time.sleep(3)
    print("             |              ")
    print("             |              ")
    print("             |              ")
    print("          ___|___            ")
    print("          \\_____/             ")
    print("            / \\           ")
    print("\n\n")
    print("              ")
    print("            ")
    print("          ")
    print("     ________________")
    print("    |                |")
    print("    |                |")
    print("    |________________|")
    print("        |        |    ")
    print("        |        |    ")
    print("\n")
    time.sleep(3)
    print("\nThe room is fairly empty. There is a table in the middle, and a light overhead.")
    print("There is a window on the left wall.")
    print("The door leading outside is behind you, and the door leading to the other room is")
    print("right in front of you, behind the table.")
    print("Additionally, there is some equitment in the corner to your right.")
    time.sleep(8)
    aloneInTheCabin()

def aloneInTheCabin():
    print("\nWhat would you like to do?")
    print("1. Try to escape through the door.")
    print("2. Try to escape through the window.")
    print("3. Wait for them to return.")
    print("4. Try the door to the other room.")
    print("5. Investigate the equipment.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou try to open the door, but it's locked.")
        time.sleep(3)
        aloneInTheCabin()
    elif user_input == "2":
        print("\nYou go over to the window. It is old and rusted.")
        print("You try to get it open, but it's stuck.")
        time.sleep(3)
        print("\nWhat would you like to do?")
        print("1. Try to force it open.")
        print("2. Give up and figure something else out.")
        user_input2 = input("I would like to... ")
        if user_input2 == "1":
            print("\nYou manage to force the window open, slamming up with a thud.")
            time.sleep(3)
            print("\nYou can hear the mysterious figure heading for the room.")
            time.sleep(3)
            print("You quickly launch yourself out of the cabin, running as fast as you can.")
            print("You look back and see the figure standing in the doorway of the cabin,")
            print("But they're not chasing you")
            time.sleep(3)
            print("\nAfter a few minutes you feel safe, and finally take a breath.")
            print("But you soon realize you're lost in the woods.")
            woods()
        else:
            print("\nYou step back and rethink your move.")
            aloneInTheCabin()
    elif user_input == "3":
        print("\nYou sit still, waiting for the figure to return.")
        time.sleep(10)
        print("\nIt doesn't seem they're coming back.")
        time.sleep(3)
        print("\nWhat would you like to do?")
        print("1. Give up and figure something else out.")
        print("2. Wait some more.")
        user_input3 = input("I would like to... ")
        if user_input3 == "1":
            print("\nYou step back and rethink your move.")
            aloneInTheCabin()
        elif user_input3 == "2":
            print("\nYou continue to wait for the figure to return for a bit longer.")
            time.sleep(10)
            print("\nThe door swings back open, and the figure walks back into the room.")
            print("They sit back down in front of you.")
            figurePartTwo()
        else:
            print("\nYou mull over your options, but before you can think for too long,")
            print("The figure steps back into the room, and sits down in front of you.")
    elif user_input == "4":
        print("\nYou approach the door leading to the other room and try the knob.")
        time.sleep(3)
        print("\nThe door easily swings open.")
        time.sleep(3)
        if "hook" in inventory:
            otherRoomNoHook()
        else:
            otherRoom()
    elif user_input == "5":
        print("\nYou walk over to the pile of equipment to see if you can find anything.")
        time.sleep(3)
        print("\nAfter rummaging about for a bit, you find three items of note.")
        equipment()
    else:
        print("\nYou consider your options carefully...")
        aloneInTheCabin()

def equipment():
    print("\nFirst, there is an axe. It is quite rusty, and has a strange smell.")
    print("Second, there is some rope. Despite the enviornment, it feels quite sturdy.")
    print("Third, there is a small whistle.")
    time.sleep(6)
    print("Do you pick any of the items, 1, 2 or 3 up?")
    user_input = input("I would like to pick up... ")
    if user_input == "1":
        inventory.append("axe")
        print("\nYou pick up the axe. It feels heavy.")
        print("And the weight of what you might do with it feels heavy too.")
    elif user_input == "2":
        inventory.append("rope")
        print("\nYou pick up the rope. You hang it on your shoulder, ready to use it at any time.")
    elif user_input == "3":
        inventory.append("whistle")
        print("\nYou pick up the whistle, unsure of its purpose.")
    else:
        print("\nYou decide to not pick up any of the items and reconsider your options.")
        aloneInTheCabin()
    time.sleep(3)
    print("\nBefore you can pick anything else up, the figure comes back into the room.")
    print("You quickly back up, and sit back down, sensing that is what they want.")
    print("The figure sits down in front of you.")
    figurePartTwo()
    

def otherRoom():
    print("\nThe figure stands over a sink, filled to the brim with black slop.")
    print("Rabbits, raccoons, ferrets and other critters hang from the ceiling on hooks,")
    print("dripping blood onto the wooden floor.")
    print("Additional hooks hang empty, ready for flesh to hang from them.")
    print("Moonlight pours in from the window over the sink, the only light source allowing you to")
    print("see the grotesque scene.")
    time.sleep(15)
    print("\nThe figure doesn't seem to notice you.")
    print("They have a large coat and a furry hat on, not allowing you to see the details of their body.")
    time.sleep(5)
    print("\nWhat would you like to do?")
    print("1. Back into the previous room and close the door.")
    print("2. Stand still.")
    print("3. Approach the figure.")
    print("4. Try to steal one of the hooks.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou step back slowly, trying to not make any sudden moves.")
        print("You gingerly close the door.")
        time.sleep(3)
        print("You let out a breath, now back in the front room.")
        aloneInTheCabin()
    elif user_input == "2":
        print("\nYou stand still, waiting for the figure to do something.")
        time.sleep(3)
        print("The figure turns towards you.")
        print("The figure picks up a hatchet from the sink. It is coated in black slop.")
        print("The figure reaches out, seemingly offering the hatchet to you.")
        print("You stare at the hatchet, and you sense that this is an offer for a new life.")
        time.sleep(10)
        print("\nWhat would you like to do?")
        print("1. Stand still.")
        print("2. Take the hatchet.")
        user_input2 = input("I would like to... ")
        if user_input2 == "1":
            print("\nYou stand still and, in effect, refuse the hatchet.")
            time.sleep(3)
            print("\nThe figure screams at you, furious that you refused the offer.")
            print("You have never heard such an unnatural scream before.")
            time.sleep(3)
            print("\nThe figure raises the hatchet and strikes you, instantly killing you.")
            time.sleep(3)
            gameOver(2)
        elif user_input2 == "2":
            print("\nYou take the hatchet. Despite the slop, you feel your grip strengthen around it.")
            print("The figure motions you to follow them, and you follow.")
            time.sleep(5)
            pygame.mixer.music.load("Deer Hunter's Anthem.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
            print("\nYou hunt with the figure for the rest of your days,")
            print("living off slop cooked from the animals you kill.")
            time.sleep(6)
            print("\nYou never do get a good look at the figure, as the night never seems to end")
            print("even after countless hours of hunting with them.")
            time.sleep(6)
            hunterEnding()
        else:
            print("\nYou stand still and, in effect, refuse the hatchet.")
            time.sleep(3)
            print("\nThe figure screams at you, furious that you refused the offer.")
            print("You have never heard such an unnatural scream before.")
            time.sleep(3)
            print("\nThe figure raises the hatchet and strikes you, instantly killing you.")
            time.sleep(3)
            gameOver(2)
    elif user_input == "3":
        print("\nYou step towards the figure.")
        print("The figure does not seem to notice you approach them.")
        time.sleep(3)
        print("\nWhat would you like to do?")
        print("1. Continue to approach.")
        print("2. Step back and reconsider your options.")
        user_input3 = input("I would like to... ")
        if user_input3 == "1":
            print("\nYou continue to approach, when suddenly the figure turns towards you.")
            time.sleep(3)
            print("\nThey are weilding a hatchet, and swing it at your head.")
            print("It slams into your skull, instantly killing you.")
            time.sleep(3)
        elif user_input3 == "2":
            print("\nYou step back, unsure if it is the right choice to approach them.")
            print("You decide to take in your surroundings again.")
            time.sleep(3)
            otherRoom()
        else:
            print("\nYou shiver with fear.")
            time.sleep(3)
            print("\nYou step back, unsure if it is the right choice to approach them.")
            print("You decide to take in your surroundings again.")
            time.sleep(3)
            otherRoom()
    elif user_input == "4":
        print("\nHooks hang from the ceiling, rusty, cold, and dripping with fresh blood.")
        print("You reach out, attempting to take one of the hooks off its chain.")
        time.sleep(3)
        print("\nHow do you remove the hook?")
        print("1. Slowly, making as little noise as possible.")
        print("2. Quickly, getting it over with.")
        user_input4 = input("I would like to... ")
        if user_input4 == "1":
            print("\nYou slowly and silently lift free the hook from the hanging chain.")
            time.sleep(3)
            print("\nMiraculously, you get it free without alerting the figure.")
            inventory.append("hook")
            time.sleep(3)
            print("\nYou slowly back into the previous room, relieved you managed to take the hook.")
            time.sleep(3)
            aloneInTheCabin()
        elif user_input4 == "2":
            print("\nYou rapidly take the hook off the chain, making it clang in the process.")
            print("You turn to back out of the room.")
            time.sleep(3)
            print("\nBut the figure noticed you take it.")
            time.sleep(3)
            print("The figure rushes at you and reveals a hatchet.")
            print("Weilding the hatchet, they swing at your head.")
            print("It slams into your skull, instantly killing you.")
            time.sleep(3)
            gameOver(2)
        else:
            print("\nYou don't know how to best approach your thievery, and step back to take")
            print("in your surroundings again.")
            otherRoom()
    else:
        print("\nYou mull over your options, and take in the scene again.")
        time.sleep(3)
        otherRoom()
        
def otherRoomNoHook():
    print("\nThe figure stands over a sink, filled to the brim with black slop.")
    print("Rabbits, raccoons, ferrets and other critters hang from the ceiling on hooks,")
    print("dripping blood onto the wooden floor.")
    print("Additional hooks hang empty, ready for flesh to hang from them.")
    print("Moonlight pours in from the window over the sink, the only light source allowing you to")
    print("see the grotesque scene.")
    time.sleep(15)
    print("\nThe figure doesn't seem to notice you.")
    print("They have a large coat and a furry hat on, not allowing you to see the details of their body.")
    time.sleep(5)
    print("\nWhat would you like to do?")
    print("1. Back into the previous room and close the door.")
    print("2. Stand still.")
    print("3. Approach the figure.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou step back slowly, trying to not make any sudden moves.")
        print("You gingerly close the door.")
        time.sleep(3)
        print("You let out a breath, now back in the front room.")
        aloneInTheCabin()
    elif user_input == "2":
        print("\nYou stand still, waiting for the figure to do something.")
        time.sleep(3)
        print("The figure turns toward you.")
        print("The figure picks up a hatchet from the sink. It is coated in black slop.")
        print("The figure reaches out, seemingly offering the hatchet to you.")
        print("You stare at the hatchet, and you sense that this is an offer for a new life.")
        time.sleep(10)
        print("\nWhat would you like to do?")
        print("1. Stand still.")
        print("2. Take the hatchet.")
        user_input2 = input("I would like to... ")
        if user_input2 == "1":
            print("\nYou stand still and, in effect, refuse the hatchet.")
            time.sleep(3)
            print("\nThe figure screams at you, furious that you refused the offer.")
            print("You have never heard such an unnatural scream before.")
            time.sleep(3)
            print("\nThe figure raises the hatchet and strikes you, instantly killing you.")
            time.sleep(3)
            gameOver(2)
        elif user_input2 == "2":
            print("\nYou take the hatchet. Despite the slop, you feel your grip strengthen around it.")
            print("The figure motions you to follow them, and you follow.")
            time.sleep(5)
            pygame.mixer.music.load("Deer Hunter's Anthem.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
            print("\nYou hunt with the figure for the rest of your days,")
            print("living off slop cooked from the animals you kill.")
            time.sleep(6)
            print("\nYou never do get a good look at the figure, as the night never seems to end")
            print("even after countless hours of hunting with them.")
            time.sleep(6)
            hunterEnding()
        else:
            print("\nYou stand still and, in effect, refuse the hatchet.")
            time.sleep(3)
            print("\nThe figure screams at you, furious that you refused the offer.")
            print("You have never heard such an unnatural scream before.")
            time.sleep(3)
            print("\nThe figure raises the hatchet and strikes you, instantly killing you.")
            time.sleep(3)
            gameOver(2)
    elif user_input == "3":
        print("\nYou step towards the figure.")
        print("The figure does not seem to notice you approach them.")
        time.sleep(3)
        print("\nWhat would you like to do?")
        print("1. Continue to approach.")
        print("2. Step back and reconsider your options.")
        user_input3 = input("I would like to... ")
        if user_input3 == "1":
            print("\nYou continue to approach, when suddenly the figure turns towards you.")
            time.sleep(3)
            print("\nThey are weilding a hatchet, and swing it at your head.")
            print("It slams into your skull, instantly killing you.")
            time.sleep(3)
        elif user_input3 == "2":
            print("\nYou step back, unsure if it is the right choice to approach them.")
            print("You decide to take in your surroundings again.")
            time.sleep(3)
            otherRoomNoHook()
        else:
            print("\nYou shiver with fear.")
            time.sleep(3)
            print("\nYou step back, unsure if it is the right choice to approach them.")
            print("You decide to take in your surroundings again.")
            time.sleep(3)
            otherRoomNoNook()
    else:
        print("\nYou mull over your options, and take in the scene again.")
        time.sleep(3)
        otherRoomNoHook()


def figurePartTwo():
    print("\nThe figure stares at you.")
    time.sleep(3)
    print('\nThey finally speak. "I will now prepare you for harvest."')
    time.sleep(5)
    print("\nIt seems they plan to eat you...")
    print("Surely killing you in the process.")
    time.sleep(3)
    print("They get up and return to the other room.")
    print("You can hear them searching for something.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Try to escape through the door.")
    print("2. Try to escape through the window.")
    print("3. Wait to be prepared for harvest.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou jump up and run for the door.")
        print("You reach the door and try to turn the knob.")
        time.sleep(4)
        print("\nIt's locked.")
        time.sleep(3)
        print("\nYou turn around and the figure is standing right in front of you.")
        time.sleep(4)
        print("\nHe strikes you with his staff, and you again fall unconscious.")
        print("You are never found.")
        time.sleep(3)
        gameOver(2)
    elif user_input == "2":
        print("\nYou rush over to the window. It is old and rusted.")
        print("You try to get it open, but it's stuck.")
        time.sleep(3)
        print("\nWhat would you like to do?")
        print("1. Try to force it open.")
        print("2. Give up and figure something else out.")
        user_input2 = input("I would like to... ")
        if user_input2 == "1":
            print("\nYou manage to force the window open, slamming up with a thud.")
            time.sleep(3)
            print("\nYou can hear the mysterious figure heading for the room.")
            time.sleep(3)
            print("You quickly launch yourself out of the cabin, running as fast as you can.")
            print("You look back and see the figure standing in the doorway of the cabin,")
            print("But they're not chasing you")
            time.sleep(3)
            print("\nAfter a few minutes you feel safe, and finally take a breath.")
            print("But you soon realize you're lost in the woods.")
            woods()
        else:
            print("\nYou don't have time to reconsider your move.")
            print("They're back.")
    elif user_input == "3":
        print("\nYou patiently wait for harvest.")
        print("And soon, they return to the room.")
    else:
        print("\nYou take too long considering your options.")
        print("They return to the room.")
    time.sleep(5)
    print("\nThey grab you by your shirt and drag you into the backroom.")
    print("Kicking and squirming, you fail to break free of their grasp.")
    time.sleep(3)
    print("\nThey lift you up, and slap your upper back into one of the empty hooks.")
    time.sleep(3)
    print("\nThe pain is like nothing you have ever felt. You feel your blood")
    print("flow down your back as everything becomes blurry.")
    time.sleep(3)
    print("\nThe last thing you see is the figure moan in excitement as your last ember")
    print("of life fades from you.")
    time.sleep(3)
    gameOver(5)

#Option 2: You sleep on the bench
########################################################


########################################################
#Option 3: Road to the east

def lonelyBeaver():
    time.sleep(2)
    print("\nYou begin to walk down the road heading east.")
    print("You recall that the abandoned gift shop is a bit down this way.")
    time.sleep(5)
    print("\nThe lumber factory used to put on a Paul Bunyan festival every year.")
    print("It was popular, but that tradition ended years ago because of the disappearances.")
    time.sleep(5)
    print("\nBefore long, the old gift shop comes into view.\n")
    hiddenInventory.append("shop")
    time.sleep(2)
    print("                         _________         ")
    print("    _______________     |  The    |        ")
    print("   /               \\    | Lonely  |        ")
    print("  /_________________\\   | Beaver  |        ")
    print("   |               |    |_________|        ")
    print("   |    _     _    |        ||             ")
    print("   |   | |   |_|   |        ||             ")
    print("   |___|_|_________|        ||             ")
    print("-------------------------------------------")
    print("\n")
    print(" --  --  --  --  --  --  --  --  --  --  --")
    print("\n")
    print("-------------------------------------------")
    time.sleep(2)
    print('\n"The Lonely Beaver"\n')
    time.sleep(2)
    print("You always thought that was a strange name for a gift shop.")
    print("But that was the name.")
    time.sleep(3)
    lonelyChoice()

def lonelyChoice():
    print("\nWhat would you like to do?")
    print("1. Look around the area.")
    print("2. Try to head inside.")
    print("3. Head back to the bus stop.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou take in your surroundings.")
        time.sleep(3)
        print("The Lonely Beaver has long been abandoned. The paint is worn and chipped,")
        print("and vines and moss have run up the sides of the building.")
        print("The window is somehow still intact, but the roof seems ready to cave at any moment.")
        if "electricity" in inventory:
            print("The letters 'L' and 'v' glow due to the factory's power, but the rest of the letters")
            print("seem to have stopped working long ago.")
        else:
            print("The sign looms over without any neon glow.")
        print("The road is empty.")
        time.sleep(10)
        print("\nYou feel you have properly surveyed the area.")
        lonelyChoice()
    elif user_input == "2":
        print("\nYou approach the door.")
        time.sleep(3)
        print("\nYou try the door, but it's locked.")
        time.sleep(3)
        if "electricity" in inventory:
            print("There is a keycard panel on the door, standard for all factory associated buildings.")
            time.sleep(3)
            print("\nWhat would you like to do?")
            print("1. Swipe your keycard.")
            print("2. Step back and reconsider.")
            user_input2 = input("I would like to... ")
            if user_input2 == "1":
                print("\nYou swipe your keycard and you hear a click.")
                print("You try the door, and it swings open. You head inside.")
                time.sleep(3)
                insideLonelyBeaver()
            else:
                print("\nYou step back and reconsider your options.")
                lonelyChoice()
        else:
            print("There is a keycard panel on the door, but without power it's useless.")
            time.sleep(3)
            print("You set back, unable to get inside.")
            lonelyChoice()
    elif user_input == "3":
        print("\nYou decide that you don't have time to shop. The bus might come soon after all.")
        print("You head back to the bus stop.")
        time.sleep(4)
        print("After a short walk, you return to the bus stop.")
        time.sleep(3)
        startingChoice()
    else:
        print("\nThe surrounding trees russle with menace.")
        time.sleep(2)
        lonelyChoice()

def insideLonelyBeaver():
    pygame.mixer.music.load("factory-fluorescent-light-buzz-6871.mp3")
    pygame.mixer.music.play(-1)
    print("\nYou step inside The Lonely Beaver.")
    time.sleep(3)
    print("\nA few of the overhead lights still work, illuminating the store with a soft light.")
    print("Most of the decorations are in a state of disorder, and the shelves are mostly empty.")
    time.sleep(5)
    insideLonelyBeaverChoice()

def insideLonelyBeaverChoice():
    print("\nWhat would you like to do?")
    print("1. Check the cash register.")
    print("2. Check the shelves.")
    print("3. Check the backroom.")
    print("4. Leave The Lonely Beaver.")
    user_input = input("I would like to... ")
    if user_input == "1":
        if "nickel" not in inventory:
            print("\nYou walk over to the cash register.")
            print("You open it, and a stream of spiders scatter out.")
            time.sleep(3)
            print("You manage not to get bitten.")
            time.sleep(3)
            print("\nInside it is empty, but next it is a strange black notebook.\n")
            print("It gives you an ominous feeling.")
            time.sleep(3)
            print("Do you take the notebook?")
            print("1. Take it.")
            print("2. Leave it.")
            user_input2 = input("I decide to... ")
            if user_input2 == "1":
                inventory.append("notebook")
                print("\nYou take the notebook. It appears to be empty.")
                time.sleep(5)
                insideLonelyBeaverChoice()
            else:
                print("\nYou decide to leave it.")
                time.sleep(3)
                insideLonelyBeaverChoice()
        else:
            print("You walk back over to the cash register.")
            time.sleep(3)
            print("\nInside it is empty.")
            time.sleep(3)
            insideLonelyBeaverChoice()
    elif user_input == "2":
        shelf()
    elif user_input == "3":
        print("\nYou head towards the backroom.\n")
        hiddenInventory.append("backdoor")
        time.sleep(2)
        print("  ______  ")
        print(" |      | ")
        print(" | -#-----")
        print(" |      | ")
        print(" |    0 | ")
        print(" |      | ")
        print(" | -#-----")
        print(" |      | ")
        print(" |______| ")
        time.sleep(2)
        print("\nThe door seems to be bolted shut with some pretty serious locks.")
        print("You definitely can't force it open.")
        if "backroomSecret" in inventory:
            pass
        time.sleep(3)
        print("\nYou head back to the main room.")
        insideLonelyBeaverChoice()
        
    else:
        print("\nYou are unnerved by the eerie atmosphere and decide to get some fresh air.")
        print("You step back outside.")
        lonelyChoice()

def shelf():
    if "plushie" not in inventory and "camera" not in inventory:
        print("\nThe shelves are nearly empty. Perhaps looters have already taken every valuable.")
        time.sleep(3)
        print("\nAll you manage to find is a Babe the Blue Ox plushie and an old disposable camera.\n")
        time.sleep(2)
        print("         _              ")
        print("   _____| |     ________  ")
        print("  |       |    |      |_| ")
        print("  |  ___  |    |   ()   |  ")
        print(" _|_|___|_|____|________|__")
        print("|__________________________|")
        time.sleep(2)
        print("\nDo you take either of the items?")
        print("1. Take the plushie.")
        print("2. Take the camera.")
        print("3. Don't take either.")
        user_input = input("I would like to take... ")
        if user_input == "1":
            print("\nYou take the plushie.")
            inventory.append("plushie")
            time.sleep(3)
            print("You spend a moment admiring your newfound treasure.")
            time.sleep(3)
            insideLonelyBeaverChoice()
        elif user_input == "2":
            print("\nYou take the camera.")
            time.sleep(3)
            print("It doesn't have any film.")
            inventory.append("camera")
            time.sleep(3)
            insideLonelyBeaverChoice()
        else:
            print("\nYou decide these dusty old items aren't worth collecting.")
            print("You step back and consider your next move.")
            time.sleep(3)
            insideLonelyBeaverChoice()
    elif "plushie" not in inventory and "camera" in inventory:
        print("\nThe shelves are nearly empty. Perhaps looters have already taken every valuable.")
        time.sleep(3)
        print("\nAll you manage to find is a Babe the Blue Ox plushie.\n")
        time.sleep(2)
        print("         _              ")
        print("   _____| |       ")
        print("  |       |     ")
        print("  |  ___  |      ")
        print(" _|_|___|_|________________")
        print("|__________________________|")
        time.sleep(2)
        print("\nDo you take it?")
        print("1. Take the plushie.")
        print("2. Don't take it.")
        user_input2 = input("I would like to take... ")
        if user_input2 == "1":
            print("\nYou take the plushie.")
            inventory.append("plushie")
            time.sleep(3)
            print("You spend a moment admiring your newfound treasure.")
            time.sleep(3)
            insideLonelyBeaverChoice()
        else:
            print("\nYou decide this dusty old item isn't worth collecting.")
            print("You step back and consider your next move.")
            time.sleep(3)
            insideLonelyBeaverChoice()
    elif "camera" not in inventory and "plushie" in inventory:
        print("\nThe shelves are nearly empty. Perhaps looters have already taken every valuable.")
        time.sleep(3)
        print("\nAll you manage to find is an old disposable camera.\n")
        time.sleep(2)
        print("                          ")
        print("                ________  ")
        print("               |      |_| ")
        print("               |   ()   |  ")
        print(" ______________|________|__")
        print("|__________________________|")
        time.sleep(2)
        print("\nDo you take it?")
        print("1. Take the camera.")
        print("2. Don't take it.")
        user_input3 = input("I would like to take... ")
        if user_input3 == "1":
            print("\nYou take the camera.")
            inventory.append("camera")
            time.sleep(3)
            print("It doesn't have any film.")
            time.sleep(3)
            insideLonelyBeaverChoice()
        else:
            print("\nYou decide this dusty old item isn't worth collecting.")
            print("You step back and consider your next move.")
            time.sleep(3)
            insideLonelyBeaverChoice()
    else:
        print("\nYou have picked the shelves clean.")
        time.sleep(3)
        insideLonelyBeaverChoice()


#Option 3: Road to the east
########################################################


########################################################
#Option 4: Road to the west

def rockslide():
    time.sleep(2)
    print("\nYou walk down the road to the west. The bus should have come from this dicection.")
    print("Maybe someone closed the tunnel?")
    time.sleep(4)
    print("\nThe entrance to the tunnel appears on the horizon.")
    time.sleep(3)
    print("\nAs you draw closer, you realize that a rockslide has completely blocked off the")
    print("entrance to the tunnel. You cannot squeeze through.\n")
    hiddenInventory.append("rockslide")
    time.sleep(3)
    print("-----------------------------------------------------------------}")
    print("       _--------_                           _---__---__          }")
    print("-------         -----_       __--_        _-           -----__---}")
    print("   _____              ---__--     --------                       }")
    print("  /     \\                      _____             __             }")
    print(" /       \\       _____        /     \\           /  \\           }")
    print(" \\       /      /     \\      /       \\          \\__/          }")
    print("  \\_____/      /       \\     \\       /                        }")                
    print("               \\       /      \\_____/___                       }")
    print("                \\_____/            /     \\                     }")
    print("       _____                      /       \\   _____             }")
    print("      /     \\                     \\       /  /     \\           }")
    print("     /       \\           __        \\_____/  /       \\          }")
    print("     \\       /          /  \\                \\       /           }")
    print("      \\_____/           \\__/                 \\_____/           }")
    print("                _____________                                  }")
    print("               /  _________  \\                                }")
    print("              /  /         \\  \\                                }")
    print("             /  /     |     \\  \\      _____                     }")
    print("            /  /   ___|_     \\  \\    /     \\       __           }")
    print("           /  /|  /     \\  __|\\_ \\  /       \\     /  \\         }")
    print("          /  / | /       \\/     \\ \\ \\       /     \\__/          }")
    print("         /  / _|_\\_      /       \\ \\ \\_____/                    }")
    print("        /__/_/     \\____/\\       /__\\         _____              }")
    print("------------/       \\ |   \\_____/------------/     \\-------------}")
    print("            \\       / |      |              /       \\          ")
    print("     __      \\_____/         |              \\       /          ")
    print("    /  \\       |      |      |               \\_____/           ")
    print("    \\__/       |      |      |                                  ")
    print("               |             |                                   ")
    time.sleep(3)
    print("\nAt least you now know why there's been no busses. But how did this happen?")
    time.sleep(3)
    rockslideChoice()

def rockslideChoice():
    print("\nWhat would you like to do?")
    print("1. Try to climb the rocks.")
    print("2. Go back to the bus station.")
    user_input = input("I would like to... ")
    if user_input == "1":
        if "hook" in inventory and "rope" in inventory:
            print("\nBefore attempting to climb the rocks manually, you realize you have")
            print("some rope and a hook you managed to take from the cabin.")
            time.sleep(3)
            pygame.mixer.music.load("success_bell-6776.mp3")
            pygame.mixer.music.play()
            print("\nAfter a little bit of work, you have managed to make a grappling hook!")
            inventory.append("grappling hook")
            inventory.remove("rope")
            inventory.remove("hook")
            time.sleep(3)
            pygame.mixer.music.load("Haunted Forest Sounds  Ghostly Murmurs  1 Hour.mp3")
            pygame.mixer.music.play(-1)
            print("\nYou swing your grappling hook and release, send the hook high into the air.")
            print("It catches onto a rock at the very top and you start to make you ascent.")
            time.sleep(3)
            print("\nSoon, you reach the top.")
            time.sleep()
            clifftop()
        else:
            print("\nYou grip the firt boulder, climbing up on it.")
            print("You set your eyes on the overhang of the entrance of the tunnel.")
            print("And you jump for it...")
            time.sleep(5)
            print("\nYou make it!")
            time.sleep(2)
            print("You catch your breath and jump up to the next rock.")
            time.sleep(3)
            print("\nYou grip onto it and hoist yourself up.")
            print("You again wind up for a big jump to the boulder to your right.")
            time.sleep(5)
            print("\nYou jump for it!")
            time.sleep(2)
            print("And slip.")
            time.sleep(2)
            print("\nYou fall down the rocks, breaking numerous bones and twisting your body.")
            time.sleep(2)
            print("You slam headfirst onto the road and instantly die.")
            time.sleep(2)
            gameOver(6)
    else:
        print("\nThe rock wall is far too daunting. You head back to the bus stop.")
        time.sleep(3)
        print("You soon make it back.")
        time.sleep(3)
        startingChoice()

def clifftop():
    pass

#Option 4: Road to the west
########################################################


########################################################
#Option 5: The factory

def factoryOutside():
    time.sleep(2)
    print("\nYou walk down the dirt road leading to the factory you work at.")
    print("An old lumber mill, it's isolated from civilization deep in the woods.")
    print("The area gets heavy snowfall during the winter, so for a few months out of the year")
    print("the factory shuts down.")
    time.sleep(8)
    print("The factory comes into view.\n")
    hiddenInventory.append("factory")
    time.sleep(2)
    print("                     _    _    _    _             ")
    print("     /\\             / |  / |  / |  / |          /\\")
    print("    /  \\           /  | /  | /  | /  |         /  \\")
    print("   --  --         /___|/___|/___|/___|        --  --")
    print("   /    \\        |                   |        /    \\")
    print("  /      \\       |         _         |       /      \\")
    print("  --    --       |        | |        |       --    --")
    print("^^/      \\^^^^^^^|________|_|________|^^^^^^^/      \\^^")
    print(" /        \\              /    /             /        \\")
    print(" ----------             /    /              ----------")
    print("    |  |               /    /                  |  |")
    print("    |  |              /    /                   |  |")
    print("    |  |             /    /                    |  |")
    print("    |  |            /    /                     |  |")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    time.sleep(2)
    if "electricity" not in inventory:
        print("\nThe factory is dark inside.")
    else:
        print("\nThe factory shines a faint glow.")
        print("You can hear machines humming from inside.")
    time.sleep(3)
    factoryOutsideChoice()

def factoryOutsideChoice():
    pygame.mixer.music.load("Haunted Forest Sounds  Ghostly Murmurs  1 Hour.mp3")
    pygame.mixer.music.play(-1)
    print("\nWhat would you like to do?")
    print("1. Look around the area.")
    print("2. Try to head inside.")
    print("3. Head back to the bus stop.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nThe factory is surrounded by woods.")
        if "electricity" not in inventory:
            print("It is quiet.")
            print("The power was shut off, so it is completely dark inside.")
        else:
            print("A faint glow and hum emanates from the factory.")
        time.sleep(3)
        print("\nYou feel you have properly surveyed the area.")
        time.sleep(3)
        factoryOutsideChoice()
    elif user_input == "2":
        print("\nYou approach to the door.")
        time.sleep(3)
        if "electricity" not in inventory:
            print("Usually you would use your keycard to enter, but since the power is off")
            print("the keycard scanner isn't on.")
            print("Fortunately, you closed up the factory, and have the key to get in.")
            time.sleep(5)
        else:
            print("You swipe your keycard.")
            time.sleep(3)
        print("\nYou unlock the door and head in.")
        time.sleep(5)
        factoryMain()
    elif user_input == "3":
        print("\nYou head back to the bus stop.")
        time.sleep(3)
        print("You soon make it back.")
        time.sleep(3)
        startingChoice()
    else:
        print("\nYou consider your options.")
        factoryOutsideChoice()

def factoryMain():
    print("\nThe factory's main floor spreads out in front of you.")
    print("Towering woodworking machines line up in rows.")
    print("Logs, planks, and other forms of wood fill up the rest of the room.")
    time.sleep(3)
    print("\nYou feel like you're being watched.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Go to the manager's office.")
    print("2. Go to the storage room.")
    print("3. Go to the power room.")
    print("4. Return to the outside.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nYou head to the manager's office.")
        time.sleep(3)
        managerOffice()
    elif user_input == "2":
        print("\nYou head to the storage room.")
        time.sleep(3)
        storageRoom()
    elif user_input == "3":
        print("\nYou head to the power room.")
        time.sleep(3)
        powerRoom()
    elif user_input == "4":
        print("\nYou head back outside.")
        time.sleep(3)
        factoryOutsideChoice()
    else:
        print("\nYou consider your options.")
        factoryMain()

def managerOffice():
    print("\nYou approach the manager's office.")
    print("The manager has always been a mysterious individual. In fact, you don't")
    print("know if you've ever met them. Let alone been inside their office.")
    print("The only boss you've ever known is your shift lead.")
    time.sleep(8)
    print("\nYou reach the door.")
    print("There is a keypad next to it.")
    hiddenInventory.append("keypad")
    if "electricity" not in inventory:
        print("But without power you cannot use it.")
        time.sleep(3)
        print("\nYou head back to the main area of the factory.")
        factoryMain()
    else:
        time.sleep(3)
        keypad()

def keypad():
    print("\nWhat would you like to do?")
    print("1. Input the code.")
    print("2. Return to the main area.")
    user_input = input("I would like to... ")
    if user_input == "1":
        print("\nThe keypad lights up.")
        password = input("PLEASE ENTER PASSWORD: ").lower()
        if password == "bestlumber":
            print("\nYou hear a click.")
            time.sleep(3)
            print("\nYou try the door, and it swings open.")
            time.sleep(3)
            insideManagerOffice()
        elif password != "bestlumber":
            print("\nINCORRECT PASSWORD. PLEASE TRY AGAIN.")
            keypad()
    else:
        print("\nYou return to the main area.")
        time.sleep(3)
        factoryMain()

def insideManagerOffice():
    print("\nYOU HAVE REACHED THE MANAGER'S OFFICE! I HAVE NOT GOTTEN THIS FAR YET...")
    gameOver(100)
    
def storageRoom():
    print("\nYou look around the storage room.")
    if "gloves" not in inventory:
        print("There are two items that intrest you.")
        print("Leaning on the wall is an old broom and in the corner is a pair of rubber gloves.")
    else:
        print("Leaning against the wall is an old broom.")
    time.sleep(3)
    print("\nWhat would you like to do?")
    print("1. Clean up for a little bit using the broom.")
    if "gloves" not in inventory:
        print("2. Put on the rubber gloves.")
        print("3. Head back to the main area of the factory.")
        user_input = input("I would like to... ")
        if user_input == "1":
            print("\nYou pick up the broom and sweep for a bit.")
            time.sleep(3)
            print("The area is much cleaner now!")
            time.sleep(3)
            storageRoom()
        elif user_input == "2":
            print("\nYou put on the rubber gloves.")
            inventory.append("gloves")
            time.sleep(3)
            storageRoom()
        elif user_input == "3":
            print("\nYou return to the main area.")
            time.sleep(3)
            factoryMain()
        else:
            print("You consider your options.")
            time.sleep(3)
            storageRoom()
    else:
        print("2. Head back to the main area of the factory.")
        user_input = input("I would like to... ")
        if user_input == "1":
            print("\nYou pick up the broom and sweep for a bit.")
            time.sleep(3)
            print("The area is much cleaner now!")
            time.sleep(3)
            storageRoom()
        elif user_input == "2":
            print("\nYou return to the main area.")
            time.sleep(3)
            factoryMain()
        else:
            print("You consider your options.")
            time.sleep(3)
            storageRoom()
    
def powerRoom():
    print("\nYou enter the power room.")
    print("The power room is filled with electrical equipment you don't understand.")
    print("But you do know where the switchboard is.")
    print("A leak has caused the floor to be wet, and many of the electronics are soaked.")
    print("You're not sure if the power is going to work.")
    time.sleep(3)
    powerChoice()

def powerChoice():
    print("\nWhat would you like to do?")
    if "electricity" not in hiddenInventory:
        print('1. Turn on "MAIN POWER".')
        print("2. Head back to the main area of the factory.")
        user_input = input("I would like to... ")
        if user_input == "1":
            print("\nYou grip the switch and swing it up.")
            if "gloves" in inventory:
                time.sleep(3)
                pygame.mixer.music.load("War Machines Factory  Robot Sci-Fi Ambience  1 Hour.mp3")
                pygame.mixer.music.play(-1)
                hiddenInventory.append("electricity")
                print("The lights immediately turn on, and you can hear machinery humming.")
                time.sleep(3)
                powerChoice()
            else:
                print("Suddenly you feel a large surge of electricity shoot through you.")
                pygame.mixer.music.load("electrocute-6247.mp3")
                pygame.mixer.music.play()
                time.sleep(3)
                print("The electrocution stops your heart, and you collapse.")
                time.sleep(3)
                gameOver(8)
        elif user_input == "2":
            print("\nYou return to the main area.")
            time.sleep(3)
            factoryMain()
        else:
            print("You consider your options.")
            time.sleep(3)
            powerChoice()
    else:
        print('1. Turn off "MAIN POWER".')
        print("2. Head back to the main area of the factory.")
        user_input = input("I would like to... ")
        if user_input == "1":
            print("\nYou grip the switch and swing it down.")
            time.sleep(3)
            pygame.mixer.music.load("Haunted Forest Sounds  Ghostly Murmurs  1 Hour.mp3")
            pygame.mixer.music.play(-1)
            hiddenInventory.remove("electricity")
            print("The power is now off.")
            time.sleep(3)
            powerChoice()
        elif user_input == "2":
            print("\nYou return to the main area.")
            time.sleep(3)
            factoryMain()
        else:
            print("You consider your options.")
            time.sleep(3)
            powerChoice()


#Option 5: The factory
########################################################


########################################################
#Option 6: The Woods

def woods():
    print("\nYOU HAVE REACHED THE WOODS! I HAVE NOT GOTTEN THIS FAR YET...")
    gameOver(100)

#Option 6: The Woods
########################################################


########################################################
#Endings, Game Over and Hints

def hunterEnding():
    time.sleep(8)
    print("\n\nYOU HAVE BECOME A HUNTER.\n")
    time.sleep(2)
    print("      __                        _   ")
    print("     |  |_                     /_|  ")
    print("     (oo) _____         /-----//    ")
    print("     |  ||_/           /|_____/     ")
    print("     |__|               |    |      ")
    print("   __/__/               |    |      ")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    time.sleep(3)
    print("\nYou have reached ending #4.")
    print('"The Hunter"')
    endings.append(4)
    print("\nThere are X endings to reach in this game.")
    print("Can you reach them all?")
    time.sleep(6)
    deathInventory()

def voidEnding():
    pygame.mixer.music.load("goodbye-then-69407.mp3")
    pygame.mixer.music.play(-1)
    print("\nYOU ARE LOST IN THE VOID.\n")
    time.sleep(2)
    print("\n\n\n\n")
    print("               o    ")
    print("             -/-    ")
    print("             |\\   ")
    print("\n\n\n\n\n\n\n")
    time.sleep(3)
    print("\nYou have reached ending #9.")
    print('"The Void"')
    print("\nThere are X endings to reach in this game.")
    print("Can you reach them all?")
    time.sleep(6)
    deathInventory()
    

def gameOver(ending):
    pygame.mixer.music.load("goodbye-then-69407.mp3")
    pygame.mixer.music.play(-1)
    print("\n\nYOU HAVE DIED.")
    time.sleep(2)
    print("  ______   _____   _________   _____        _____    __        __  ______  ______")
    print(" / _____| |  _  | |  _   _  | |  ___|      /     \\   \\ \\      / / |  ___| |   _  \\")
    print("| |  ____ | |_| | | | | | | | |  ___      /   _   \\   \\ \\    / /  |  ___  |  |_| /")
    print("| | |__ | |  _  | | | | | | | |  ___|     |  |_|  |    \\ \\__/ /   |  ___| |   _  \\")
    print("| |___  | | | | | | | | | | | |  ___      \\       /     \\    /    |  ___  |  | \\  \\")
    print(" \\_____/  |_| |_| |_| |_| |_| |_____|      \\_____/       \\__/     |_____| |__|  \\__\\")
    time.sleep(5)
    if ending == 1:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"A Watery Grave"')
        endings.append(1)
    elif ending == 2:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"An Ungrateful Guest"')
        endings.append(2)
    elif ending == 3:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"Too Much of a Good Thing"')
        endings.append(3)
    elif ending == 5:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"Harvested"')
        endings.append(5)
    elif ending == 6:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"Slip and Fall"')
        endings.append(6)
    elif ending == 7:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"One Day My Bus Will Come"')
        endings.append(7)
    elif ending == 8:
        print("\nYou have reached ending #"+str(ending)+".")
        print('"A Sudden Shock"')
        endings.append(8)
    else:
        pass
    print("\nThere are X endings to reach in this game.")
    print("Can you reach them all?")
    time.sleep(5)
    deathInventory()

def deathInventory():
    if "recall" not in hiddenInventory:
        for i in inventory:
            inventory.remove(i)
        for i in hiddenInventory:
            hiddenInventory.remove(i)
    else:
        hintoffer()

def hintOffer():
    print("\nYou may get a hint for one of the endings in this game, if you wish.")
    print("If not, type anything but a number.")
    user_input = input("\nThe ending I want a hint on is number... ")
    if user_input == "1":
        hint(1)
    elif user_input == "2":
        hint(2)
    elif user_input == "3":
        hint(3)
    elif user_input == "4":
        hint(4)
    elif user_input == "5":
        hint(5)
    elif user_input == "6":
        hint(6)
    elif user_input == "7":
        hint(7)
    elif user_input == "8":
        hint(8)
    elif user_input == "9":
        hint(9)
    else:
        print("\nThe trees yearn for your next visit...")
        time.sleep(6)
        main()

def hint(ending):
    if ending == 1:
        print("\nHere is your hint:")
        print("A poor choice is made under the stress of a chase.")
        time.sleep(3)
    elif ending == 2:
        print("\nHere is your hint:")
        print("A rude gesture towards the host leads to your demise.")
    elif ending == 3:
        print("\nHere is your hint:")
        print("Don't scoop up more than you can swallow.")
    elif ending == 4:
        print("\nHere is your hint:")
        print("A stranger may offer you a new life, if you seek it.")
    elif ending == 5:
        print("\nHere is your hint:")
        print("You cannot survive in the cabin for too long.")
    elif ending == 6:
        print("\nHere is your hint:")
        print("Leave rock climbing to the professionals.")
    elif ending == 7:
        print("\nHere is your hint:")
        print("I will wait, I will wait, for you.")
    elif ending == 8:
        print("\nHere is your hint:")
        print("Safety should be a top priority when handling electronics.")
    elif ending == 9:
        print("\nHere is your hint:")
        print("Members only.")
    print("\nGood luck...")
    time.sleep(3)
    main()

#Endings, Game Over and Hints
########################################################

########################################################
################# MAIN METHOD ##########################
########################################################
################# BE CAREFUL ###########################
########################################################
    
def main():
    setupGameMusic()
    printTitle()
    startGame()
    startingArea()

main()

########################################################
################# MAIN METHOD ##########################
########################################################
################# BE CAREFUL ###########################
########################################################
