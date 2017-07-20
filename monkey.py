##defining functions before hand :3

###when you lose this shows up
def lose():
     print(" ")
     print(" ")
     print(" ")
     print("                 GAME OVER                      ")
     print(" ")
     print(" ")

###when you win this shows up
def win ():
    print(" ")
    print(" ")
    print(" ")
    print("                 YOU WIN!                       ")
    print(" ")
    print(" ")


#begining
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a jungle, scared and alone. You stand up and go .... '''
print(start)



#first path choosen
print("Type 'left' to go left or 'right' to go right.")
user_input = input()

#left
if user_input == "left":
    print("You decide to go left and there is a monkey attacking you! ") # finished the story by writing what happens
    print("Type 'fight' to fight or 'run' to run away.")
    forr = input()
    #fight
    if forr == "fight":
        print("The monkey beats you up. You see the light and die :( ")
        lose()

    #run
    elif forr == "run":
        print ("You are so tired from running away like a chicken. You die of exhaustion. :( ")
        lose()

    #not valid
    else:
        print("no bro try a valid input")


#right
elif user_input == "right":
    print("You choose to go right and there is a long road ahead of you! ") # finished the story writing what happens
    print(" ")
    print("You are hella tired man... Type 'rest' to take a break or 'continue' to keep on going ")
    rorc = input()

    #rest
    if rorc == "rest":
        print("You see a nice monkey. He seems friendly for a monkey in a jungle. What do you want to do?")
        print(" ")
        print("Type 'play' to play with monkey or type 'fight' to say fight me to the monkey that does not know English")
        porf = input()

        #play
        if porf == "play":
            print(" ")
            print("You play with the monkey and it is very friendly.")
            print("He decides to take you to the nearest city ")

            print("But you do not know where this city is. Do you call a taxi, uber, horse carriage, camel")
            ride = input()

            #uber
            if ride == "uber":
                print(" ")
                print("you don't have a phone bro")
                lose()

            #taxi
            elif ride == "taxi":
                print("You get in a taxi but it turns out he  ")
                lose()

            #horse
            elif ride == "horse carriage":
                print("You take a horse carriage back home.")
                win()

            #camel
            elif ride == "camel":
                print("You steal a camel and get home safe and sound, but you are now a criminal for theft.")
                print(" ")
                print(" ")
                print(" ")
                print("                 YOU WIN?                       ")
                print(" ")
                print(" ")

            #other
            else:
                print("Invalid input")


        #fight
        elif porf == "fight":
            print("okay you choose to fight a monkey. Do you punch or kick?")
            pork = input()

            #punch
            if pork == "punch":
                print("The monkey cries and leaves. You feel bad you feel like a monster but you now have to live with it")
                print("Type 'cry' to cry or type 'run after' to chase the monkey and say sorry")
                corr = input()

                #cry
                if corr == "cry":
                    print("the guilt overcomes you drown in your tears. ")
                    lose()

                #run
                elif corr == "run after":
                    print("You say sorry to the monkey. But then you remember the monkey does not speak English.")
                    print("it is too late now to say sorry... (yes it is too l8 m8)")
                    lose()

                #other
                else:
                    print("Invalid Imput")

            #kick
            elif pork == "kick":
                print("You kick the monkey. It kicks back. You regret your choice. It eats you. You are now bones")
                lose()

            #other
            else:
                print("Ivalid Input")

    #continue
    elif rorc == "continue":
        print("""
        I walk a lonely road
        The only one that I have ever known
        Don't know where it goes
        But it's only me, and I walk alone """)
        print(" ")
        print(" ")
        print(".. you pass out.")
        lose()

    else:
        print("no bro try a valid input")
else:
    print("no bro try a valid input")
