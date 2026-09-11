print("Welcome to the Enchanted Forest!")
print("You stand before two paths leading deeper into the woods.")
print("A: A path glowing with a faint, welcoming blue light.")
print("B: A dark, narrow path overgrown with thick, menacing thorns.")

# Choice 1
user_choice1 = input("Which path do you choose? (A/B): ").lower()

if user_choice1 == "a":
    print("\nYou follow the blue light and discover a glowing fairy trapped in a giant spider web.")
    print("A: Try to carefully cut the web and free the fairy.")
    print("B: Ignore the fairy and keep walking; you don't want to meet the spider.")

    # Choice 2 (Branch A)
    user_choice2 = input("What do you do? (A/B): ").lower()

    if user_choice2 == "a":
        print("\nThe fairy is grateful and offers you a magical reward.")
        print("A: Ask for a sword that never dulls.")
        print("B: Ask for a bottomless pouch of gold coins.")

        # Choice 3 (Branch A-A)
        user_choice3 = input("What is your choice? (A/B): ").lower()

        if user_choice3 == "a":
            print(
                "\nENDING 1: You take the sword, slay a dragon, and become a legendary knight renowned across the realm.")
        elif user_choice3 == "b":
            print("\nENDING 2: You take the gold, buy a massive castle, and live a life of luxury and peace.")
        else:
            print("\nInvalid input. The fairy gets impatient and vanishes. Game Over.")

    elif user_choice2 == "b":
        print("\nYou walk past the fairy, but soon stumble upon a sleeping forest troll guarding a bridge.")
        print("A: Try to sneak past the sleeping troll.")
        print("B: Shout to wake the troll and challenge it to a riddle contest.")

        # Choice 4 (Branch A-B)
        user_choice4 = input("What is your plan? (A/B): ").lower()

        if user_choice4 == "a":
            print("\nENDING 3: You successfully sneak past and find the exit to the forest, safely escaping!")
        elif user_choice4 == "b":
            print(
                "\nENDING 4: The troll wakes up grumpy, ignores your riddles, and throws you into the river. You wash up back where you started.")
        else:
            print("\nInvalid input. The troll wakes up and chases you away. Game Over.")

    else:
        print("\nInvalid input. The spider returns. Game Over.")

elif user_choice1 == "b":
    print("\nYou hack your way through the thorns and discover an old, abandoned, creepy cabin.")
    print("A: Go inside the cabin to investigate.")
    print("B: Walk around the back of the cabin to see what else is there.")

    # Choice 5 (Branch B)
    user_choice5 = input("What do you do? (A/B): ").lower()

    if user_choice5 == "a":
        print("\nInside, you find an old witch brewing a bubbling, purple potion.")
        print("A: Ask her if you can have a sip.")
        print("B: Apologize for intruding and run out the door.")

        # Choice 6 (Branch B-A)
        user_choice6 = input("What is your move? (A/B): ").lower()

        if user_choice6 == "a":
            print("\nENDING 5: The potion turns you into a frog! You now live a happy life catching flies by the pond.")
        elif user_choice6 == "b":
            print(
                "\nENDING 6: You run away so fast you trip over a root, fall down a hidden tunnel, and discover a secret underground kingdom!")
        else:
            print("\nInvalid input. The witch curses you with bad luck. Game Over.")

    elif user_choice5 == "b":
        print("\nBehind the cabin, you find a mysterious portal swirling with galactic energy.")
        print("A: Close your eyes and jump into the portal.")
        print("B: Throw a rock into the portal to see what happens.")

        # Choice 7 (Branch B-B)
        user_choice7 = input("What do you do? (A/B): ").lower()

        if user_choice7 == "a":
            print(
                "\nENDING 7: You are transported to an alien world where the locals mistake you for their prophesied ruler.")
        elif user_choice7 == "b":
            print(
                "\nENDING 8: The portal acts as a mirror; the rock bounces back, hits you in the head, and knocks you out. You wake up safely in your own bed.")
        else:
            print("\nInvalid input. The portal closes forever. Game Over.")

    else:
        print("\nInvalid input. The cabin collapses. Game Over.")

else:
    print("\nInvalid input. You wander aimlessly until it gets dark. Game Over.")