start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("type 'left' to go left or 'right' to go right.")
user_input = input()
while user_input not in ('left','right'):
    print("Try Again")
    user_input = input()

if user_input == "left":
    print("You decide to go left and begin walking down a narrow hallway that leads to a spiral staircase.")
    print("type 'up' to go up or 'down' to go down")
    user_input = input()
    while user_input not in ('up','down'):
        print("Try Again")
        user_input = input()

    if user_input == "up":
        print('''You decided to go up. As you ascend the staircase, you see fragments of broken bones and begin to panic.
        When you reach the top of the staircase, you see a door. Trying to open the door, you discover that it is locked.''')

    elif user_input =="down":
        print('''You decided to go down the staircase and slip on the mossy stone and stumble down the stairs.
        When you finnally grab hold of a vine, you realise that you are hanging over the ledge of the broken stairs. You look down
        and there is the other ledge of the stairs that continues heading down.''' )
        print("type 'pull up' to pull yourself back up or 'reach' to reach for the other ledge.")
        user_input = input()
        while user_input not in ('pull up','reach'):
            print("Try Again")
            user_input = input()

        if user_input == "pull up":
            print("You decided to pull yourself up and have managed to successfully return to the staircase ledge.")

        elif user_input == "reach":
            print('''You chose to attempt to reach the other broken ledge below you. Unfortunately, you didn't make it and slipped, falling
            twenty feet to your death''')



elif user_input == "right":
    print("You choose to go right and head down a dark hallway. To your right you see a torch.")
print("Type 'pick up torch' to take torch or 'continue walking' to continue walking in the dark.")
user_input = input()
while user_input not in ('pick up torch','continue walking'):
    print("Try Again")
    user_input = input()

    if user_input == "pick up torch":
        print('''You decided to pick up the torch then continue walking down the hallway.
        You notice all the portraits on the wall and the degrading stone walls.
        All of a sudden you hear a growling, screeching noise up ahead in
        the dark. You look around and notice there is a door to your right.''')
        print("type 'try door' to go to door or 'forward' to continue heading towards the noise.")
        user_input = input()
        while user_input not in ('try door','forward'):
            print("Try Again")
            user_input = input()

        if user_input == "try door":
            print("You attempt to open the door but find it to be locked.")
            print("type 'kick door' to break the door down or'turn around' to head towards the sound.")
            user_input = input()
            while user_input not in ('kick door','turn around'):
                print("Try Again")
                user_input = input()

                if user_input == "kick door":
                    print('''You managed to successfully kick down the door and enter the room. Unfortunatley,
                    you entered the room that leads to the pit of snakes and got bitten to death, dying from the loss of blood and snake venom''')

                elif user_input == "turn around":
                    print('''You turned around to resume your original path but ended up running into the enormous, grotesque beast, ending
                    up as his late night snack.''')



        elif user_input == "forward":
            print('''You continue moving towards the noise and run into a beast. You try to run but end up falling and being dragged to his lair
            and eaten by him.''')


    elif user_input == "continue walking":
        print('''You decided to continue walking in the dark down the hallway. Eventually, your eyes begin to adjust to the dark
        and that is when you notice a dark sillhouette shifting in front of you. Following the movement, you hear a growling, screeching noise
        come from the sillhouette. You see a door to your left as you panic.''')
        print("type 'try door' to attempt to open the door or 'sneak around' to try and go around the beast.")
        user_input = input()
        while user_input not in ('try door','sneak around'):
            print("Try Again")
            user_input = input()

        if user_input == "try door":
            print('''You try the door and it is unlocked. You manage to hide from the beast and hear it moving past the door.''')
            print("type 'hallway' to return to the hallway or 'room' to stay in the room.")
            user_input = input()
            while user_input not in ('hallway','room'):
                print("Try Again")
                user_input = input()

                if user_input == "hallway":
                    print('''You leave the room and enter the hallway, but this beast was a mother and had little beasties.
                    Unfortunatley, they all attack you and eat you.''')

                elif user_input == "room":
                    print('''You stay in the room and suddenly hear a buzzing noise. Looking around, you see a dark shadow buzzing in front of you.
                    Wasps! They swarm towards you and sting you to death.''')



        elif user_input == "sneak around":
         print('''You continue towards the beast quietly. While almost past the beast, you Unfortunatley trip over the rug, and he charges at you.
         You begin to run but end up tripping again, and he kills you by eating you alive.''')
