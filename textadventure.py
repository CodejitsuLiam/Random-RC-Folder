import time
import random
import sys
inventory=[]
cave={"location": "north of the village", "description": "an ominous cave that looks like a gaping mouth", "itemsneeded": "a torch"}
village={"description": "the only place you have ever known"}
man={"clothesdescription": "ragged, torn, and speckled with dirt and blood", "description": "covered in cuts and scrapes from head to toe, and when he moves, he does so with great effort and pain", "words": "I have not long on this fair earth, but it is possible you can avenge me. There is a cave north of the village, where I met my untimely fate. Go there and defeat that which has defeated me."}
def endignore():
    print("You decide to forget about everything that has happened today. Despite the death of the man you met at the edge of the woods, there is nothing in it for you to risk what happened to him. ")
    time.sleep(5)
    print("\033[31mThe end.\033[0m")
    sys.exit()
def dialogue():
    print(f"You live in a small village, which is {village["description"]}.")
    time.sleep(4)
    print(f'One day, you see a man stumble out of woods.')
    time.sleep(2)
    print(f'His clothes are {man["clothesdescription"]}. He himself is in a more pitiful state- he is {man["description"]}.')
    time.sleep(7)
    print(f'You realize, with some surprise, that you do not recognize him. You know that there are other villages and towns besides yours, but without much outside contact, sometimes it feels as if your village is the only one in the world.')
    time.sleep(7)
    print(f'He sees you and says, "{man["words"]}" With these words, he gives a groan of despair, then falls at your feet, dead.')
    time.sleep(9)
def preparation():
    togoornottogo=input("Back inside, you think about what happened. Waiting in front of you is a tantalizing adventure, but is it worth risking the fate of that poor soul? ")
    if togoornottogo in ("yes", "y"):
        print("It is worth the risk. Your whole life, you have wanted a greater purpose, and you have finally found one.")
        time.sleep(5)
    elif togoornottogo in ("no", "n"):
        endignore()
    while True:
        weapongrab=input("Having decided to go to the cave, you realize you may need a weapon. You see a kitchen knife on the cutting board. Do you wish to grab it to defend yourself? ").strip().lower()
        if weapongrab in ("yes", "y"):
            inventory.append("Knife")
            print("You decide to grab the knife, knowing it may come in handy. ")
            break
        if weapongrab in ("no", "n"):
            print("Are you sure you don't want to grab the knife? ")
            time.sleep(2)
#deletedialogueherewhileplaytesting
preparation()      
def entercave():
    print("You enter the cave...")
    import time
    time.sleep(3)
def maybeattacked():
    global killorescape
    global attackcave
    import random
    attackcaveevents=["Nothing happens","A monstrous spider",]
    attackcaveweights=[50, 50]
    attackcave=random.choices(attackcaveevents, weights=attackcaveweights, k=1)[0]
    if attackcave=="Nothing happens":
        pass
    if attackcave=="A monstrous spider":
        while True:
            firstattack=input("\033[31mA monstrous spider leaps out of the shadows! What will you do? \033[0m(Run or Fight)").strip().lower()
            if firstattack== "run":
                print("You run from the spider, and you manage to lose it in the tunnels.")#maybe add turtle graphics game? That's way l8r tho, like final week shite
                killorescape="escaping"
                time.sleep(3)
                break
            elif firstattack=="fight":
                hitmissevents=["hit", "miss"]
                hitmissweight=[80, 20]
                hitmiss=random.choices(hitmissevents, weights=hitmissweight, k=1)[0]
                if hitmiss=="hit":
                    print(f"You stab at the spider with the knife, and you hit it! You step back, watching as it collapses to the ground.")
                if hitmiss=="miss":
                    print("You miss the spider! It stabs its fangs into you, but you stab at it again, and this time, you hit it!")#healthgodownaddthatl8r
                killorescape="killing"
                break
            else:
                killorescape="notyet"
                print("That is not an option")
def outnoise():
    while True:
        outnoise=input("As you walk away from the cave, you here an anguished scream come from the mouth of the cave. You spin around, but see nothing. The scream sounded human, but if someone is screaming like that, something must have caused it. Is it worth the risk to go into the cave and save the poor soul within? ").strip().lower()
        if outnoise in ("y","yes"):
            entercave()
            maybeattacked()
            if attackcave=="A monstrous spider":
                print(f"After {killorescape} the spider, you continue deeper into the cave, searching for the source of the scream. ")
                time.sleep(4)
            if attackcave=="Nothing happens":
                print("You continue deeper into the cave, searching for the source of the scream. ")
                time.sleep(2)
            print("You see droplets of blood, and you follow them until they suddenly curve into a tunnel at your right. You peek down the tunnel, but it curves along the way, so you cannot see the end. ")
            time.sleep(8)
            break
        elif outnoise in ("n","no"):
            wheregonow=input("It's not worth the risk. Do you wish to return to your village or keep exploring? (Enter Return or Explore) ").strip().lower()
            if wheregonow=="return":
                endignore()
            elif wheregonow=="explore":
                #explorefunction
                break#work on this l8r
            else:
                print("That is not an option")
        else:
            print("That is not an option")


def innoise():
    if attackcave=="A monstrous spider":
        print(f"After {killorescape} the spider, you continue deeper into the cave. ")
        time.sleep(2)
    if attackcave=="Nothing happens":
        print("You continue deeper into the cave.")
        time.sleep(1)
    print("Suddenly, you hear a loud and anguished scream from a tunnel at your right. You peek down the tunnel, but it curves along the way, so you cannot see the end. ")
    time.sleep(6)
def dontexplore():
    print("You back away from the tunnel, and descend into the depths of the cave. Down here, everything is pitch black, and fear of the unknown is just as scary as whatever lies within that tunnel.")
    time.sleep(5)
    depths=input("Do you turn back or continue on? (Back or Continue)").strip().lower()
    if depths=="back":
        print("You turn away from the darkness, and start to leave the cave.")#work more on l8r
    elif depths=="continue":
        print("You continue into the dark, only to see that the cave ends. You turn away from the darkness, and start to leave the cave.")
    else:
        print("That is not an option.")
def cavesequence():
    while True:
        caveenter = input(f"You see {cave["description"]}. Do you go in? ").strip().lower()
        if caveenter in ("yes", "y"):
            entercave()
            maybeattacked()
            innoise()
            break
        elif caveenter in ("n", "no"):
            print("You decide not to enter the cave right now. ")
            outnoise()
            break
        else:
            print("Please type either yes or no")
def encounter():
    while True:
        enterorwalk=input("Do you enter the tunnel to see what lurks inside, do you continue exploring the caves, or do you leave the cave entirely? (Enter, Explore or Leave) ").strip().lower()
        if enterorwalk=="explore":
            print("You decide to leave for now and come back later, when you are feeling more confident.")
            dontexplore()
            
        elif enterorwalk=="enter":
            print("You creep along the tunnel, walking stealthily as to not alert anything of your presence. Turning the corner, you are confused, as at the end of the tunnel is the man you met before! He faces away from you, but you recognize the tattered clothing and posture. ")
            time.sleep(10)

            break
        elif enterorwalk=="leave":
            break#sync w/ explorefunction line 72
        else:
            print("You cannot do that!")
            time.sleep(2)
cavesequence()
encounter()