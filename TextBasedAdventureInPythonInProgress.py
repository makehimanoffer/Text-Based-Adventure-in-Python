map= ["prison- behind bars","prison- jailhouse","prison- jailblock","prison- wardens office","prison- hallway",
      "prison- outside","prison- courtyard","prison- gate","prison- outside","parking lot","parking lot-car",
      "road -highway""road- crossroads","road- west road","road- east road","suburban estate- outside- Ma's House",
      "suburban estate- outside- Girlfriend's House","Ma's House- inside","Girlfriend's House- inside","Coffin"]
current= map[0]
inventory=["empty"]
def prison():
    lookTake="look"
    helpValue="help me"
    inventoryTake="inventory"
    inputTake=""
    afterLookingInputTake=""
    
    print(str(current) + "\n You're lying in a jail behind bars, confused as to how you got there\n")
    print("You know that theres no possible way that you did whatever they're trying to convict you of\n")
    print("You must escape, but the question now is, how?\n")
    print("What do you wish to do?\n")
    inputTake=input()
    while current=="prison- behind bars":
        
    
        
        
            

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
            if afterLookingInputTake=="look at vent" or afterLookingInputTake=="look at sink":
                checkBehindBarsLookAround(afterLookingInputTake)
            else:
                inputTake=""
            

         
            
        else:
            print("I'm sorry but I've no idea what you're on about\n")
            print("Maybe you might wish to ask for help by typing in help\n")
            print("What do you wish to do?\n")
            inputTake=input()

def checkBehindBarsLookAround(inputString):
    innerChoice=""
    innerInnerChoice=""
    if inputString=="help me":
        print("As seen in the description, you've got a wide array of options to check out" +
              " such as 'look at vent' to get a closer look at the broken vent, 'check pocket' to see the contents " +
              "of your pocket and whether they're of any use, 'look at sink' to check out the sink area in greater detail" +
              ", 'shout at guard' to interrupt the guards show and wake him up a bit(not advisable), 'escape' "+ 
              "to try to escape\n")
        print("so what do you wanna do?\n")
        inputString=input()

    if inputString=="look at vent":
        while innerChoice!="stop looking at vent":
            if innerChoice=="":
                print("you walk over to the vent, get into a crouched position as you look at the vent with its dangling vent cover"+
                    "and see if theres anything that is there to benefit you\n you notice that the screws holding the cover are"+
                    " long and loose and you may be able to 'pull out screw'. As you look into the actual vent you know that"+
                    " theres absolutely no way of fitting yourself through it, so thats ruled out, however you can see" +
                    " something in the vent, you know you could 'open up vent and take item' but there may be other ways to" +
                    " escape without these, and you could just 'stop looking at vent'\n")
                print("What do you wish to do?\n")
                innerChoice=input()
            if innerChoice=="pull out screw":
                  inventory[0]="screw"
                  print("screw has been added to your inventory\n")
                  print("What do you wish to do?\n")
                  innerChoice=input()

            if innerChoice=="open up vent and take item":
                  
                print("you have taken out a giant ass sword,but it is too big to keep on your person without"+
                      " arousing suspicion, so you hide it under your bed\n")
                print("You go back to the vent\n")
                inventory[0]="big ass sword"
                print("What do you wish to do?\n")
                innerChoice=input()

            

            if innerChoice=="help me":
                  print(str(current) + "\n")
                  print("you walk over to the vent, get into a crouched position as you look at the vent with its dangling vent cover"+
                    "and see if theres anything that is there to benefit you\n you notice that the screws holding the cover are"+
                    " long and loose and you may be able to 'pull out screw'. As you look into the actual vent you know that"+
                    " theres absolutely no way of fitting yourself through it, so thats ruled out, however you can see" +
                    " something in the vent, you know you could 'open up vent and take item' but there may be other ways to" +
                    " escape without these, and you could just 'stop looking at vent'\n")
                  print("What do you wish to do?\n")
                  innerChoice=input()

    if inputString=="look at sink":
        print("Beneath the mould of the sink drain and the rancid toothbrush, you see a shiny thing in the drain,"+
                " you could reach it with some leverage if you really wanted to, maybe by using something you have" +
                " or could have gotten and put in your inventory. You could 'use X to get shiny thing' or just 'stop"+
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
                          
                  
                      
              elif innerInnerChoice== "use big ass sword to get shiny thing":
                  for stuff in inventory:
                      if stuff== "big ass sword" or stuff=="key":
                          print("in a totally inconspicuous way you have managed to smash the hello out of the" +
                                " sink and get the shiny thing with any trouble thanks to the big ass sword"+
                                " you have gotten a key for your work.\n")
                          inventory[0]="key"
                          print("What do you wish to do?\n")
                          innerInnerChoice=input()
                      else:
                           print("just checking, but it seems like you don't have a big ass sword\n")
                           print("What do you wish to do?\n")
                           innerInnerChoice=input()
        

              elif innerInnerChoice=="help me":
                   print ("depending your inventory you may be able to 'use X to get shiny thing' or"+
                          " 'stop looking at sink'\n")
                   print("What do you wish to do?\n")
                   innerInnerChoice=input()

              else:
                   print("i've no idea what you're saying, try to use 'help me' if you're stuck")
                   print("What do you wish to do?\n")
                   innerInnerChoice=input()
                   
                    

             
                                
                  
                
                
            


prison()
