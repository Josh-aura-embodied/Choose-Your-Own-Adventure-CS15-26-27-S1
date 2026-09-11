print("Welcome to Kings Court!")
print("You stand before two 1v1 opponents each on a different court, waiting for your pick.")
print("A: A 6'5 200 pound beast who cant dribble but can shoot and hit layups and dunks with ease.")
print("B: A 5'9 130 pound player who can blow right by you and get to the rim, and can also shoot, but gets scared when you step up to play defense.")

# Choice 1
user_choice1 = input("Which opponent do you choose? (A/B): ").lower()

if user_choice1 == "a":
    print("You follow the player onto the court and shoot for ball. He makes his with ease...Your turn to shoot.")
    print("A: Show off and shoot with your off hand.")
    print("B: Shoot off of one leg with your eyes closed.")

    # Choice 2 (Branch A)
    user_choice2 = input("What do you do? (A/B): ").lower()

    if user_choice2 == "a":
        print("You let loose a fundamentally ugly jumpshot that sends a univeral wince to both your opponent and the bystanders")
        print("A: Ignore the crowd and get the game going.")
        print("B: Laugh it off and make it seem like that was all a part of the plan.")

        # Choice 3 (Branch A-A)
        user_choice3 = input("What is your choice? (A/B): ").lower()

        if user_choice3 == "a":
            print(
                "ENDING 1: You play to 3 points. Play 1, the giant grabs the ball after tou check up, makes the mistake of dribbling and you take that opportunity to steal the ball, and get to the basketb for an easy layup. Leaving the crowd silenced. Play 2, the giant steps up on defense, obviously trying to overwhelm you, but you are used to this... you hit a pound dribble into a tween and step back, making him fall flat on his bum, and let loose a three point shot that you already know is going in. Ending the game with style.")
        elif user_choice3 == "b":
            print("ENDING 2: First play of the game, the player lets off a crowd silencing three, that shakes both the crowd into a loud riot of cheering, and you right off the court. Better luck next time. Maybe try practicing basketball before challenging such an advanced player.")
        else:
            print("Invalid input. Your opponent lets loose all the tricks up his sleeve and wins the game in a mere instant. Game Over.")

    elif user_choice2 == "b":
        print("You brick the one-legged shot horribly off the top of the backboard. The big man gets ball first and checks it up at the top of the key.")
        print("A: Play tight physical defense and force him to dribble.")
        print("B: Sag way back into the paint and give him the open jumper.")

        # Choice 4 (Branch A-B)
        user_choice4 = input("What is your plan? (A/B): ").lower()

        if user_choice4 == "a":
            print("ENDING 3: You press up close. Uncomfortable with handling the ball, he tries to dribble around you, loses control, and turns it over! You take over, knock down back-to-back shots, and win the game!")
        elif user_choice4 == "b":
            print(
                "ENDING 4: Since you sagged off, the giant catches the ball and smoothly drains jumper after jumper right over your head. You lose without even getting a possession.")
        else:
            print("Invalid input. You freeze on defense, and the giant walks right in for a thunderous slam. Game Over.")

    else:
        print("Invalid input. The giant gets tired of waiting and steps off the court. Game Over.")

elif user_choice1 == "b":
    print("You walk over to Court B to face the speedy 5'9 speedster. He checks the ball up to start the game.")
    print("A: Immediately press up on him full-court and yell 'NO EASY BUCKETS!'")
    print("B: Lay back in the paint and let him drive into your shot-blocking zone.")

    # Choice 5 (Branch B)
    user_choice5 = input("What do you do? (A/B): ").lower()

    if user_choice5 == "a":
        print("Seeing your aggressive defensive stance, he visibly flinches, gets nervous, and picks up his dribble early.")
        print("A: Reach in aggressively for an easy steal.")
        print("B: Stay disciplined in your stance and let him make a mistake.")

        # Choice 6 (Branch B-A)
        user_choice6 = input("What is your move? (A/B): ").lower()

        if user_choice6 == "a":
            print("ENDING 5: You reach in too aggressively! You poke the ball free, snag it, drive in for an easy game-winning layup, leaving him rattled!")
        elif user_choice6 == "b":
            print(
                "ENDING 6: You hold your ground. He tries a panicked pass to no one, coughing up the ball. You grab it, hit a cold step-back jumper, and lock up the win!")
        else:
            print("Invalid input. You stumble on defense, giving him just enough room to regain confidence and score. Game Over.")

    elif user_choice5 == "b":
        print("You give him space. With room to operate, he uses his lighting-fast first step to gain full speed toward the basket.")
        print("A: Slide your feet and meet him at the rim for a contest.")
        print("B: Try to take a charge near the key.")

        # Choice 7 (Branch B-B)
        user_choice7 = input("What do you do? (A/B): ").lower()

        if user_choice7 == "a":
            print(
                "ENDING 7: He uses his incredible speed to blow right past your contest, pulling off a smooth double-clutch reverse layup for the game winner!")
        elif user_choice7 == "b":
            print(
                "ENDING 8: You set your feet just in time! He panics at the wall of defense, charges right into you, and commits an offensive foul! You take over possession and seal the game with a smooth jumper.")
        else:
            print("Invalid input. He pulls up for an uncontested jump shot and swishes it. Game Over.")

    else:
        print("Invalid input. He gets bored waiting and walks off to find another challenger. Game Over.")

else:
    print("Invalid input. You wander off the court aimlessly. Game Over.")