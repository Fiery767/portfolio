from __future__ import print_function
import sys 
import random

#function for game over
def gameOver(ending, GO_Desc):
    '''
    Exits the program and sends a game over message to the user, indicating which ending they got.
    '''
    print()
    print('Possible ending ' + ending + '/19.')
    print('Ending:', GO_Desc)
    print('GAME OVER')
    sys.exit() #ends the program

CarGetAway = random.randint(1,15) #sets number randomizer for later on

'''INTRODUCTION/GAME START'''
print('Welcome to ESCAPE!')
print('Game Designed and Coded By: Celine Lafosse and Melody Wang')
print('Instructions: Please type everything exactly as specified in the prompt.')

print()
print('---------------------------------------------------------------------------------------------------------------------------')
print()



'''---------------------------------------------------------------------------------------------------------------------------'''

'''ACT 1''' 

'''---------------------------------------------------------------------------------------------------------------------------'''

#Prints the initial description of the situation
print('You and your friends are sitting around a campfire on a cold winter night.',\
'Suddenly the fire goes out and you hear screams. Panicking in the dark you grab your') 

'''Friend or Flashlight choice'''

choice1 = raw_input('friend/flashlight: ') #User choice for which direction to proceed in
print() #prints an empty line
    
'''Grab Friend'''
if choice1 == 'friend': 
    print ('You reach for your friend but there is nothing there. Suddenly something grabs you and drags you away!',\
    'You have been taken.') #If the user makes the incorrect answer 'friend' they automaticlly go to the maze/act 2


    
'''Grab a Flashlight'''
    
if choice1 == 'flashlight':
    print ('You reach for a flashlight, stumbling around you manage to turn it on. Everyone is...gone?',\
    'Not a single person in sight.') 
    print ('Suddenly something grabs you! You try to fight it off with your flashlight as a weapon!',\
    'As you try to hit them with your flashlight you aim....')
    #if the user makes the correct answer it prints the prompt of the attack
    
    choice2 = raw_input ('high/low: ')#user makes next choice of whether to aim high or low
    print()
    
    if choice2 != 'high' and choice2 != 'low': #4th wall break if they type anything else and goes to the maze
        print ('Are you serious? Trying to break the game? Really?? We worked so hard on this game and you think you can break it',\
        'that easily. We thought this through you know?')
        print ('This isn\'t funny, thinking we would slack off and not put a fourth wall break here is sad. We\'ve worked so hard',\
        'on this, and you\'re really trying to break it?')
        print ('You swing everywhere and don\'t hit anything as you try to break the game and the mysterious thing takes you away.')
        
    if choice2 == 'high': #user makes the incorrect choice and is taken to the maze.
        print ('You missed! How did you miss it was literally inches away from you',\
          'and you missed! The mysterious thing drags you away! You have been taken.') 
          
    elif choice2 == 'low': #user makes the correct choice and get the chance to get the car ending
        print ('You hit...something? You dont know what but the mysterious thing',\
            'lets go. You make a break for the car, look for your keys and get in.') 
        print ('Choose a number from 1 to 15, if it is the same as the computer you get away')
        carGuess = int(raw_input('Choose a number to determine your fate: ')) #user inputs number
        
        #The car ending is rare and hard to get because the user needs to guess the same number as the
        #randomizer at the beginning of the program.
        if carGuess == CarGetAway: 
                    print ('Its a miracle!!! Your car starts in time unlike every horror movie',\
                                'cliche and you get away!!') #the user gets away
                    ending = '1' #game end prompt
                    GO_Desc = 'Car Escape'
                    gameOver(ending, GO_Desc)
        
        #user does not get away and goes to act 2            
        if carGuess != CarGetAway: 
                print ('And just as the horror movie cliche goes, your car is having trouble',\
                    'starting. Something opens the car door because for some reason you forgot to lock it and takes you.')
if choice1 != 'friend' and choice1 != 'flashlight':#4th wall break for choice1 if the user chooses something else.
    print ('Are you trying to break our story this early? Or are you looking for some sort of special ending?')
    print ('You\'re in the middle of the forest with your friends, theres no unicorns here. You \'re not going',\
    'to get a special "Unicorn Stabbing" ending.')
    print ('Because you have bad survival insticts and didn\'t do anything, something took you away!')

'''Car Ending''' 



'''---------------------------------------------------------------------------------------------------------------------------'''

'''ACT 2''' 

'''---------------------------------------------------------------------------------------------------------------------------'''


def fourth_wall_break():
    '''
    Function that prints a message to the user if they attempt to pick an option other than those specified to them.
    '''
    #Death, game over
    print('How dare you try to beat the system by entering an option other than the options specified? Who do you think you are?')
    print('You have DIED a HORRIBLE and PAINFUL death. Next time, follow the rules.')

#print some empty lines before the start of act 2
print()
print()

print('You see a huge maze before you. You walk inside and follow the pathway',\
'until you hit your first choice of where to go next.') #Prints the initial description of the maze
move = raw_input('left/right: ') #User choice for which direction to proceed in
print() #prints an empty line

#If the user chooses to move left the following block of code will run
if move == 'left':
    print('You turn left and keep walking, following the path laid out before',\
    'you by the walls of the maze. Eventually, you hit a dead end.') #User hits a dead end
    print('You turn around to head back to where you came from. Before you can',\
    'leave, a wall slides out of seemingly nowhere, blocking you in. On the wall reads:') #User is blocked in to answer the question
    
    print('What is the name of the Dublin High School mascot?') #Prints the puzzle question
    print() #prints an empty line
    
    q1_ans = 'Grady' #Sets the correct answer for question 1 to the variable q1_ans
    #Takes a user input and sets it to q1_guess, the user's guess for the first puzzle
    q1_guess = raw_input('Guess (capitilization counts): ') 
    print() #prints an empty line
    #the user speaks their answer
    print('You speak into the silence, and say "' + q1_guess + '". The words on the wall glow for a moment.')
    
    print() #prints an empty line
    
    #If they get the answer right
    if q1_guess == q1_ans:
        print('The wall stops glowing, and for a moment you fear that you have',\
        'answered incorrectly. However, your doubts quickly fade as the wall slides',\
        'away, and you\'re able to return to where you came from.')
    
    #Else, if they get it wrong
    else:
        #Death, game over
        print('The wall stops glowing. It seems to have rejected your answer, and,'\
        'now the entire wall glows red. It is angry at your ignorance and foolishness.',\
        'There\'s a loud ringing in your ears before everything goes black.')
        print('You have died.')
        ending = '2'
        GO_Desc = 'Puzzle Question 1/4 Incorrect Answer'
        gameOver(ending, GO_Desc)

#Else if the user chooses neither right or left, runs this block of code
elif move != 'right' and move != 'left':
    fourth_wall_break()
    ending = '3'
    GO_Desc = 'Maze Turn 1 Invalid Choice'
    gameOver(ending, GO_Desc)
    
#This will run after they get the question right (if they chose to go left), or directly after they chose to go right
print('You proceed to the right and take several more twisting turns before reaching another branching pathway.')
move = raw_input('left/forward/right: ') #User chooses where to move next

print() #prints an empty line

#If the user chooses left or forward, the following block of code will run
if move == 'left' or move == 'forward':
    print('You go', move, 'and eventually come across a dead end. You turn around to head back and bump into an invisible barrier.')
    print('A voice echoes from out of nowhere. It asks:')
    
    print('What year did the Golden Gael Palace open?') #Prints puzzle question
    q2_ans = '2017' #Sets the answer to question 2 to the variable q2_ans
    print() #prints an empty line
    q2_guess = raw_input('Guess: ') #Takes a user input and sets it to the variable q2_guess
    print() #prints an empty line
    print('You speak into the silence, and say "' + q2_guess + '". For a moment, nothing happens.') #The user speaks their answer
    
    #If they get the answer right
    if q2_guess == q2_ans:
        print('You reach forward to check if the barrier has disappeared. To your relief, your hand passes through where the',\
        'barrier was before.')
        print('You go back to where you made your last turn.')
        
        #defines the q3 function
        def q3():
            '''
            prints the dead end and puzzle question 3. Asks for the user's answer, and either let's them go back to where they came
            from (if it's correct), or kills them and ends the game (if it's wrong).
            Uses two variables, q3_ans (the answer to puzzle question 3) and q3_guess (the user's input). Checks if q3_guess is 
            equal to q3_ans to determine which branching pathway will be carried out.
            '''
            #dead end description
            print('You hit another dead end, and to your annoyance, there\'s another barrier when you try to turn back.')
            print('This time, the voice asks:')
            
            #puzzle question 3
            print('What\'s Mr. Brown\'s room number?')
            q3_ans = 'J204' #sets a variable, q3_ans, to the answer to question 3
            
            print() #prints an empty line
            q3_guess = raw_input('Guess (format: A123): ') #gets user input (their guess) and sets it to a variable, q3_guess
            print() #prints an empty line
            
            print('Once again, you speak into the silence. "' + q3_guess + '". You wait a few moments.')
            print('This time, you say screw it. You back up a couple steps, then try charging through where the barrier was.')
            
            #if the user is correct
            if q3_guess == q3_ans:
                print('Where you expect an impact, there is none. You return to where you came from.')
            
            #else, if the user is incorrect: death, game over
            else:
                print('Exactly where you expected it, you slam your shoulder into an invisible force. It stings, ',\
                'but you keep trying.') 
                print('Though you\'re doing your best, try as you might, you can\'t break through.')
                print('You hear the same voice from before, and it seems to be... laughing?')
                print('Everything goes black.')
                print('You have died.')
                ending = '4'
                GO_Desc = 'Puzzle Question 2/4 Incorrect Answer'
                gameOver(ending, GO_Desc)
        
        #If their last choice was left, gives them the option to go forward or right
        if move == 'left':
            move = raw_input('forward/right: ')
            print() #prints an empty line
            print('This time you go', move, 'instead of left.')
            
            if move == 'forward': #If the user chooses to go forward
                q3() #calls the q3 function
            
            #else if the user tries to go left again
            elif move == 'left':
                print('Why... why would you go back there?')
                ending = '7'
                GO_Desc = 'Maze Turn 2B Duplicate Choice'
                gameOver(ending, GO_Desc)
                
            #else if the user tries to specify another option
            elif move != 'forward' and move != 'right':
                fourth_wall_break() #calls the fourth_wall_break function
                ending = '8'
                GO_Desc = 'Maze Turn 2B Invalid'
                gameOver(ending, GO_Desc)
                
        #Else (if their last choice was forward), gives them the option to go left or right    
        else:
            move = raw_input('left/right: ')
            print() #prints an empty line
            print('This time you go', move, 'instead of forward.')
            
            #if the user goes left
            if move == 'left':
                q3() #calls the q3 function
                
            #else if the user tries to go forward again
            elif move == 'forward':
                print('Why... why would you go back there?')
                ending = '5'
                GO_Desc = 'Maze Turn 2A Duplicate Choice'
                gameOver(ending, GO_Desc)
            
            #else if the user tries to specify another option
            elif move != 'left' and move != 'right':
                fourth_wall_break() #calls the fourth_wall_break function
                ending = '6'
                GO_Desc = 'Maze Turn 2A Invalid Choice'
                gameOver(ending, GO_Desc)
    
    #Else, if they get the answer wrong        
    else:
        #Death, game over.
        print('You reach forward to check if the barrier has disappeared. Your hand smacks right into it, just like before.')
        print('Before you know what\'s happening, a pit opens beneath your feet and you fall down.')
        print('You have died.')
        ending = '9'
        GO_Desc = 'Puzzle Question 3/4 Incorrect Answer'
        gameOver(ending, GO_Desc)

#else if they try to specify another option
elif move != 'left' and move != 'forward' and move != 'right':
    fourth_wall_break() #calls the fourth_wall_break function
    ending = '10'
    GO_Desc = 'Maze Turn 2 Invalid Choice'
    gameOver(ending, GO_Desc)

#runs when the user goes right (either after q2 or q3, or if they chose it in the first place)
print('You go to the right and keep following the path the maze has set out for you.')
print('Eventually, you reach yet another branching path.')

move = raw_input('left/right: ')
print() #prints an empty line

#if the user goes left
if move == 'left':
    print('You hit a dead end. You turn back, and a little gnome stands there, a wooden club held in his hand.')
    
    #puzzle question 4
    print('He asks you, "What does PLTW stand for?"')
    q4_ans = 'Project Lead The Way' #sets the correct answer to q4 to a variable, q4_ans
    
    print() #prints an empty line
    #gets the user input (their answer to the question) and sets it to a variable, q4_guess
    q4_guess = raw_input('Guess (format: Pizza Lake Taco Win): ') 
    print() #prints an empty line
    
    print('You take a deep breath, and respond. "' + q4_guess + '". You hold your breath as you wait for the gnome\'s judgement.')
    
    #if the user gets it correct
    if q4_guess == q4_ans:
        print('The gnome seems to think for a few seconds. Before giving you a curt nod and stepping aside, allowing you to pass.')
        print('You go back to where you came from.')
    #else, if the user gets it wrong
    else:
        print('The gnome looks angry. You try stepping forward with your arms raised in surrender, but he charges at you, ',\
        'club raised in the air.')
        print('You have died.')
        ending = '11'
        GO_Desc = 'Puzzle Question 4/4 Incorrect Answer'
        gameOver(ending, GO_Desc)

#if the user inputs an option other than those specified        
elif move != 'left' and move != 'right':
    fourth_wall_break()
    ending = '12'
    GO_Desc = 'Maze Turn 3 Invalid Choice'
    gameOver(ending, GO_Desc)
    
#runs if the user picks right, or if they got q4 right
print('You turn right and keep winding through more twists and turns until finally, you reach an exit.') #exit of the maze!


'''------------------------------------------------------------------------------------------------------------------------------'''

'''ACT 3'''

'''------------------------------------------------------------------------------------------------------------------------------'''

#Defines the function standing_death()
def standing_death():
    '''
    Prints the description of a death where the user stands in place, and ends the program
    '''
    print('You stand in place, thinking about what to do. While you stand and do nothing, something grabs you from behind,',\
    'covering your mouth while pulling you down to the floor.')
    print('Whatever grabbed you wraps its arm around your throat, choking you.')
    print('You have died.')

#print some empty lines before the start of act 3
print()
print()

#description of town
print('You enter a small, abandoned town. You glance behind you, and see nothing. It seems like you\'ve escaped whatever was',\
'chasing you, at least for now.')
print('To your right is a bicycle shop. To your left is a hardware store.')

#user chooses next move
print() #prints an empty line
move = raw_input('bicycle shop/hardware store: ')
print() #prints an empty line

#if they choose to enter the bicycle shop
if move == 'bicycle shop':
    print('You go right, into the bicycle shop. Once inside, you see countless bicycles lined up in rows and hanging on the wall.')
    print('While wandering the store, looking for signs of life, you hear something behind you. You quickly glance around for',\
    'something to help you get away.')
    
    #user chooses next move
    print() #prints an empty line
    move = raw_input('grab a bicycle/run: ')
    print() #prints an empty line
    
    #if they choose to grab a bicycle, one possible ending
    if move == 'grab a bicycle':
        print('You grab a nearby bicycle and hop on. You quickly try to pedal away, but it seems that the bike\'s tire is flat.')
        print('Terrified of what you\'ll see, you reluctantly turn your head to where you heard the noise coming from.')
        
        print() #print an empty line
        print() #print an empty line
        print('There\'s nothing there.')
        print() #print an empty line
        print() #print an empty line
        
        print('You jolt awake in your bed, covered in a layer of sweat. You sit up and look around, but there\'s nothing around',\
        'you other than the regular ornaments of your room.')
        print('It was all just a dream.')
        ending = '13'
        GO_Desc = 'Dreamland'
        gameOver(ending, GO_Desc)
    
    #if they choose to run, one possible ending
    elif move == 'run':
        print('You think, screw the bikes. You\'ll probably get farther if you just run rather than if you get on a',\
        'bike and try to maneuver it out of the cramped store.')
        print('You take on last brief glance around the store before sprinting out as fast as you can. You don\'t know where',\
        'you\'re running, but anywhere is better than trapped in a store with whoever or whatever\'s chasing you.')
        print('You don\'t get far from the store before you feel something grab you and pull you back, stopping your movement.',\
        'You turn, ready to fight, but you see the face of your friend, who quickly lets you go and raises his hands in surrender.')
        
        print() #prints an empty line
        print('"Chill! It was just a prank, no need to get crazy."')
        print() #prints an empty line
        
        print('A prank?')
        print('You\'re confused for a moment. If this was all a prank, did your friend set up that whole elaborate maze? And',\
        'where were you? Where was everyone else?')
        print('Your friend grabs your shoulder and stares into your eyes. "IT WAS JUST A PRANK BRO."')
        ending = '14'
        GO_Desc = 'Pranked'
        gameOver(ending, GO_Desc)
    
    #if the user doesn't choose either of the given options, one possible ending
    elif move != 'grab a bicycle' and move != 'run':
        standing_death() #calls the standing_death function
        ending = '15'
        GO_Desc = 'Just Standing in a Bike Shop'
        gameOver(ending, GO_Desc)

#if the user chooses to enter the bicycle shop     
elif move == 'hardware store':
    print('You go to the left, entering the hardware store.')
    print('Inside, there are shelves lining the walls, stocked with various mechanical tools. ',\
    'Near the cashier desk, there\'s a small snack rack.')
    
    print() #prints an empty line
    #computer chooses random number
    cc = random.randint(1, 5)
    #user chooses number
    nn = int(raw_input('Pick a number between 1 and 5: '))
    print() #prints an empty line
    
    #if the user picks the same number as the computer, one possible ending
    if nn == cc:
        print('You grab a wrench from a nearby shelf. You test its weight in your hands, taking a couple practice swings.')
        print('You hear something behind you. You quickly turn around and find yourself faced with a horrible goo creature.')
        print('With the wrench you grabbed, you swing at the creature. The wrench sinks into its goo body for a moment, before',\
        'the whole creature melts into a puddle before your eyes.')
        print('You have defeated what was chasing you.')
        ending = '16'
        GO_Desc = 'Goo Monster Beaten'
        gameOver(ending, GO_Desc)
    
    #else if the user picks a different number than the computer, but still in the range; one possible ending
    elif nn != cc and nn >= 1 and nn <= 5:
        print('You grab a bag of chips from the snack rack. All this running has made you tired. Before you can open it and',\
        'enjoy the treat, you hear a noise behind you.')
        print('You quickly turn around and find yourself faced with a horrible goo creature.')
        print('You glance down at your bag of chips before making a decision and throwing the chips at the creature',\
        'as hard as you can.')
        print('To your disappointment, the goo creature simply opens its mouth and swallows the bag whole.')
        print('Then, it swallows you.')
        print('You have died.')
        ending = '17'
        GO_Desc = 'Killed by Goo Monster'
        gameOver(ending, GO_Desc)
    
    #else (if the user picks a number outside the range provided), fourth wall break ending
    else:
        fourth_wall_break()
        ending = '18'
        GO_Desc = 'Dice Roll Invalid Choice'
        gameOver(ending, GO_Desc)

else: #if the user inputs an option other than those specified
    standing_death() #calls the standing_death function
    ending = '19'
    GO_Desc = 'Standing in the Middle of Town'
    gameOver(ending, GO_Desc)