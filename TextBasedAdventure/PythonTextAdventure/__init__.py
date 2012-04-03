map= ["prison- behind bars","prison- jailhouse","prison- jailblock","prison- wardens office","prison- hallway",
      "prison- outside","prison- courtyard","prison- gate","prison- outside","parking lot","parking lot-car",
      "road -highway""road- crossroads","road- west road","road- east road","suburban estate- outside- Ma's House",
      "suburban estate- outside- Girlfriend's House","Ma's House- inside","Girlfriend's House- inside","Coffin"]
current= map[0]
inventory=["empty"]
deltenBook=0
def prison():
    lookTake="look"
    helpValue="help me"
    
    inputTake=""
    afterLookingInputTake=""
    
    print(str(current) + "\n You're lying in a jail behind bars, confused as to how you got there\n")
    print("You know that theres no possible way that you did whatever they're trying to convict you of\n")
    print("You must escape, but the question now is, how?\n")
    print("What do you wish to do?\n")
    inputTake=input()
    while current==map[0]:
        
    
        
        
        if inputTake!= helpValue and inputTake!= lookTake:
            print("I'm sorry but I've no idea what you're on about\n")
            print("Maybe you might wish to ask for help by typing in 'help me'\n")
            print("What do you wish to do?\n")
            inputTake=input()    

        if inputTake == lookTake:
            print(str(current) +"\n")
            print("The cell you sit in is plain and grey like any normal cell, theres a bed in the corner,\n")
            print("and a sink near, with a cup and toothbrush in it, both of which are covered in mould.\n")
            print("There's also a ventilation shaft, which seems to be hanging loose.\n")
            print("At the same time you can feel something digging into your pocket\n")
            print("Outside the cell is a guard, dressed unlike a regular guard you're used to, he's struggling \n")
            print("to stay awake in his seat as he watches TV\n\n")
            print("What do you wish to do\n")
            afterLookingInputTake= input()
            inputTake=afterLookingInputTake
            if afterLookingInputTake== "check pocket" or  afterLookingInputTake== "shout at guard" or afterLookingInputTake== "escape" or afterLookingInputTake=="look at vent" or afterLookingInputTake=="look at sink" or afterLookingInputTake=="help me":
                checkBehindBarsLookAround(afterLookingInputTake)
            

        if inputTake=="help me":
            print("you may wish to 'look' around and get a grasp of what you could do\n")
            print("What do you wish to do\n")
            inputTake= input()
            
            
        

def checkBehindBarsLookAround(inputString):
    innerChoice=""
    innerInnerChoice=""
    if inputString=="help me":
        print("As seen in the description, you've got a wide array of options to check out\n" +
              " such as 'look at vent' to get a closer look at the broken vent, 'check pocket' to see the contents \n" +
              "of your pocket and whether they're of any use, 'look at sink' to check out the sink area in greater detail\n" +
              ", 'shout at guard' to interrupt the guards show and wake him up a bit(not advisable), 'escape' "+ 
              "to try to escape\n")
        print("so what do you wanna do?\n")
        inputString=input()
    
    if inputString=="check pocket":
        print("in your pocket you've found a piece of paper. It reads as follows:\n")
        print("WELCOME TO REBEL: A TEXT BASED ADVENTURE WHERE YOU FIGHT A DICTATORSHIP\n")
        print("AND REUNITE SOME FALLEN BRETHREN IN AIMS OF BRINGING ABOUT A NEW DAWN")
        print("AND HAVING STORIES AND FIGHTS AND OTHER SUCH THINGS. AS THE CREATOR OF\n THIS WORLD I HOPE YOU ENJOY")
        print("WHAT IT HAS TO OFFER AND MAKE THE MOST OF THE EXPERIENCE")
        print("so what do you wanna do?\n")
        inputString=input()
        
    if inputString=="shout at guard":
        print("You shout loudly at the guard: 'HEY LEMME OUTTA HERE' \n")
        print("He groggily rises from his chair and throws a book at you\n")
        print("You look at the book: 'The Tale of Delten: Our Leader'")
        print("The Book is added to your inventory\n may come in useful later\n")
        deltenBook=1
        print("so what do you wanna do?\n")
        inputString=input()
        
    if inputString== "escape":
        if inventory[0]=="big ass sword":
            print("Thinking about what you're gonna do to escape, you remember the sword\n")
            print("And then you start to escape using it:\n")
            escapeUsingSword()
            
        elif inventory[0]=="screw":
            print("Thinking about what you're gonna do to escape, you remember the screw")
            print("And then you start to escape using it:\n")
            escapeUsingScrew()
            
        elif inventory[0]=="key":
            print("Thinking about what you're gonna do to escape, you remember the key")
            print("And then you start to escape using it:\n")
            print("The Key opened the door, you then quietly sneak to the guard")
            escapeUsingKey()
        
        else:
            print("You think about trying to escape but, its clear that you are not ready to do so\n")
            print("you think you should probably try more things to see if theres some thing to help")
            print("so what do you wanna do?\n")
            inputString=input()   
        
        
    if inputString=="look at vent":
        while innerChoice!="stop looking at vent":
            if innerChoice=="":
                print("you walk over to the vent, get into a crouched position as you look at the vent with its dangling vent cover\n"+
                    "and see if there's anything that is there to benefit you\n you notice that the screws holding the cover are\n"+
                    " long and loose and you may be able to 'pull out screw'. As you look into the actual vent you know that\n"+
                    " there's absolutely no way of fitting yourself through it, so thats ruled out, however you can see\n" +
                    " something in the vent, you know you could 'open up vent and take item' but there may be other ways to\n" +
                    " escape without these, and you could just 'stop looking at vent'\n")
                print("What do you wish to do?\n")
                innerChoice=input()
            elif innerChoice=="pull out screw":
                inventory[0]="screw"
                print("screw has been added to your inventory\n")
                print("What do you wish to do?\n")
                innerChoice=input()

            elif innerChoice=="open up vent and take item":
                  
                print("you have taken out a giant ass sword,but it is too big to keep on your person without\n"+
                      " arousing suspicion, so you hide it under your bed\n")
                print("You go back to the vent\n")
                inventory[0]="big ass sword"
                print("What do you wish to do?\n")
                innerChoice=input()

            

            elif innerChoice=="help me":
                print(str(current) + "\n")
                print("you walk over to the vent, get into a crouched position as you look at the vent with its dangling vent cover\n"+
                    "and see if theres anything that is there to benefit you\n you notice that the screws holding the cover are\n"+
                    " long and loose and you may be able to 'pull out screw'. As you look into the actual vent you know that\n"+
                    " theres absolutely no way of fitting yourself through it, so thats ruled out, however you can see\n" +
                    " something in the vent, you know you could 'open up vent and take item' but there may be other ways to\n" +
                    " escape without these, and you could just 'stop looking at vent'\n")
                print("What do you wish to do?\n")
                innerChoice=input()
                
            else:
                print("This doesn't make sense, 'help me if you're stuck")
                print("What do you wish to do?\n")
                innerChoice=input()

    if inputString=="look at sink":
        print("Beneath the mould of the sink drain and the rancid toothbrush, you see a shiny thing in the drain,\n"+
                " you could reach it with some leverage if you really wanted to, maybe by using something you have\n" +
                " or could have gotten and put in your inventory. You could 'use X to get shiny thing' or just 'stop\n"+
                " looking at sink'\n")
        print("What do you wish to do?\n")
        innerInnerChoice=input()
        while innerInnerChoice!= "stop looking at sink":
            if innerInnerChoice=="use screw to get shiny thing":
                for stuff in inventory:
                    if stuff=="screw":
                        print ("The screw came in handy after all, with it you've fished out a key to something")
                        inventory[0]="key"
                    else:
                        print("just checking, but it seems like you don't have a screw\n")
                        print("What do you wish to do?\n")
                        innerInnerChoice=input()
                          
                  
                      
            if innerInnerChoice== "use big ass sword to get shiny thing":
                for stuff in inventory:
                    if stuff== "big ass sword" or stuff=="key":
                        print("in a totally inconspicuous way you have managed to smash the hell out of the" +
                                " sink and get the shiny thing with any trouble thanks to the big ass sword"+
                                " you have gotten a key for your work.\n")
                        inventory[0]="key"
                        print("What do you wish to do?\n")
                        innerInnerChoice=input()
                    else:
                        print("just checking, but it seems like you don't have a big ass sword\n")
                        print("What do you wish to do?\n")
                        innerInnerChoice=input()
        

            if innerInnerChoice=="help me":
                print ("depending your inventory you may be able to 'use X to get shiny thing' or"+
                          " 'stop looking at sink'\n")
                print("What do you wish to do?\n")
                innerInnerChoice=input()

            if innerInnerChoice!="help me" and innerInnerChoice!="use screw to get shiny thing" and innerInnerChoice!="use big ass sword to get shiny thing":
                print("i've no idea what you're saying, try to use 'help me' if you're stuck")
                print("What do you wish to do?\n")
                innerInnerChoice=input()
                   
def escapeUsingSword():                    
    health=5
    commands="'pull back' 'swing sword' 'lunge sword' 'slam sword'  "
    takeInput=""
    lungeHealth=2
    slamHealth=2
    current=map[0]
    previousInput=""
    print("Warning: this requires specific keyboard input to escape using the sword\n")
    print(" One command must be immediately followed by a command that makes sense with\n")
    print("the sword. Therefore they must make sense. You have life here and if you fail you will die\n")
    while health>0 and current==map[0]:
        print("Commands:"+ str(commands))
        takeInput=input()
        
        if takeInput=="pull back" and previousInput=="":
            previousInput=takeInput
            print("You have pulled back with the sword ready to lunge at the lock")
            takeInput=input()
        if takeInput=="lunge sword" and previousInput=="pull back"and lungeHealth>1:
            print("You have lunged forward with all your strength at the lock\n")
            print(" and caused considerable damage to it, one more lunge should do it")
            lungeHealth=lungeHealth-1
            previousInput=""
        if takeInput=="lunge sword" and previousInput=="pull back"and lungeHealth==1:
            print("You have lunged forward with all your strength at the lock\n")
            print(" and broken the lock")
            lungeHealth=lungeHealth-1
            current=map[1]
            knockOutGuard()
            
        if takeInput=="swing sword" and previousInput=="":
            previousInput=takeInput
            print("You have swung the sword round and round and round, ready to slam \n it down on the lock ")
        if takeInput=="slam sword" and previousInput=="swing sword" and slamHealth>1:
            print("You slam the sword harshly down upon the lock, it smashes and you know\n one more swing oughta do it")
            previousInput=""
            slamHealth=slamHealth-1
           
        if takeInput=="slam sword" and previousInput=="swing sword" and slamHealth==1:
            print("You slam the sword harshly down upon the lock, it smashes and\nbreaks the lock")
            previousInput=""
            slamHealth=slamHealth-1
            current=map[1]
            knockOutGuard()
            
        if takeInput!="slam sword" and takeInput!="swing sword" and takeInput!="lunge sword" and takeInput!="pull back":
            print("I'm sorry but your command makes no sense at this time, did you try to eat the lock \nor something?")
            print("In your silly effort you've lost a health point\n")
            health=health-1
            print("Health: " + str(health))
            
            
    
             
def escapeUsingScrew():
    print("I bet you regret this")
    knockOutGuard()

def escapeUsingKey():
    print("You open the lock without much ado")
    knockOutGuard()
                                
def knockOutGuard():                 
    print("You then run over and knock out the guard")
    current=map[1]
    prisonJailhouse()

def prisonJailhouse():
    print("This is as far as I got")      
                
            


prison()
