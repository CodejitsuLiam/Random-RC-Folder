import time
import random
import sys
import threading
inventory=[]
health=100
health_stop = threading.Event()
caveorno=None


def health_loop():
    global health
    while health > 0 and not health_stop.is_set():
        time.sleep(1.0)
        if health <= 0:
            print("You died.")
            time.sleep(0.5)
            print("\033[31mThe end.\033[0m")
            health_stop.set()
            break

health_thread = threading.Thread(target=health_loop, daemon=True)
health_thread.start()

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
#deletedialogueherewhileplaytesting In final version, put dialogue() here
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
            global firstattack
            firstattack=input("\033[31mA monstrous spider leaps out of the shadows! What will you do? \033[0m(Run or Fight)").strip().lower()
            if firstattack== "run":
                print("You run from the spider, and you manage to lose it in the tunnels.")
                killorescape="escaping"
                time.sleep(3)
                break
            elif firstattack=="fight":
                global health
                hitmissevents=["hit", "miss"]
                hitmissweight=[80, 20]
                global hitmiss
                hitmiss=random.choices(hitmissevents, weights=hitmissweight, k=1)[0]
                if hitmiss=="hit":
                    print(f"You stab at the spider with the knife, and you hit it! You step back, watching as it collapses to the ground.")
                if hitmiss=="miss":
                    health-=20
                    print("You miss the spider! It stabs its fangs into you, but you stab at it again, and this time, you hit it!")#healthgodownaddthatl8r
                killorescape="killing"
                break
            else:
                killorescape="notyet"
                print("That is not an option")
def outnoise():
    while True:
        outnoise=input("As you walk away from the cave, you hear an anguished scream come from the mouth of the cave. You spin around, but see nothing. The scream sounded human, but if someone is screaming like that, something must have caused it. Is it worth the risk to go into the cave and save the poor soul within? ").strip().lower()
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
            global wheregonow
            wheregonow=input("It's not worth the risk. Do you wish to return to your village or keep exploring? (Enter Return or Explore) ").strip().lower()
            if wheregonow=="return":
                endignore()
            elif wheregonow=="explore":
                global caveorno
                caveorno="Y"
                explorefunction()
                break
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
def cavesequence():
    while True:
        global caveenter
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
def dontexplore():
    print("You back away from the tunnel, and descend into the depths of the cave. Down here, everything is pitch black, and fear of the unknown is just as scary as whatever lies within that tunnel.")
    time.sleep(5)
    while True:
        depths=input("Do you turn back or continue on? (Back or Continue) ").strip().lower()
        if depths=="back":
            print("You turn away from the darkness, and start to leave the cave.")
            time.sleep(2)
            break
        elif depths=="continue":
            print("You continue into the dark, only to see that the cave ends. You turn away from the darkness, and start to leave the cave.")
            time.sleep(4)
            break
        else:
            print("That is not an option.")
    print("As you approach the tunnel once more, you hear footsteps coming from within. You duck behind a rock, and peek out from the side.")
    time.sleep(2)
    if caveenter in ("yes", "y"):
        print("You wonder if the scream you heard was from the person whose footsteps you hear... or if it was someone else, and the person you hear was the cause of the scream.")
        time.sleep(6)
    if caveenter in ("no", "n"):
        print("You wonder if the blood you saw leading into the tunnel came from the person you hear now.")
        time.sleep(3)
    print("But as the person emerges from the tunnel, you gasp in surprise, as the person before you is the man you met before!")
    time.sleep(5)
    print("He turns sharply towards you, sees you, and freezes. You cautiously emerge from behind the rock, feeling very wary of him, as you watched him die this morning at the edge of the woods.")
    time.sleep(8)
    print("")
def encounter():
    while True:
        enterorwalk=input("Do you enter the tunnel to see what lurks inside, do you continue exploring the caves, or do you leave the cave entirely? (Enter, Explore or Leave) ").strip().lower()
        if enterorwalk=="explore":
            print("You decide to leave for now and come back later, when you are feeling more confident.")
            time.sleep(3)
            dontexplore()
            break
            
        elif enterorwalk=="enter":
            print("You creep along the tunnel, walking stealthily as to not alert anything of your presence. Turning the corner, you are confused, as at the end of the tunnel is the man you met before! He faces away from you, but you recognize the tattered clothing and posture. ")
            time.sleep(10)
            print("You back away, hoping he hasn't seen you, and hide behind a rock outside of the tunnel.")
            time.sleep(3)
            print("He emerges from the tunnel, and you let out a gasp despite yourself, for it is rather offputting to see someone who should be dead.")
            time.sleep(5)
            print("He turns sharply towards you, sees you, and freezes. You cautiously emerge from behind the rock, feeling very wary of him, as you watched him die this morning at the edge of the woods.")
            break
        elif enterorwalk=="leave":
            global caveorno
            caveorno="Despite your wounds, y" if attackcave=="A monstrous spider" and firstattack=="fight" and hitmiss=="miss" else "Y"
            explorefunction()
            break
        else:
            print("You cannot do that!")
            time.sleep(1)
def reveal():
    print("You back away from him, and say to him,\"Look, I'm not sure if I can trust you, because I watched watched you die just earlier this morning.\"")
    time.sleep(6)
    print("At these words, his face starts to change, and you scramble away from him in horror, because his face is morphing into something else! The rest of his body starts to shift and warp, and he turns into a hideous beast, ten feet tall with gray, lumpy skin, and long tusks and claws.")
    time.sleep(10)
    print("You recognize it from stories of lands far away your mother told you when you were young. It is a troll, a creature of pure brute force, and incredibly deadly.")
    time.sleep(6)
    print("The troll roars, and swipes at you with its claws. You jump back, crashing into a wall, but you've avoided the troll. Your head is bleeding slightly.")
    global health
    global caveorno
    health -= 10
    time.sleep(6)
    while True:
        fightorflight=input("You need to survive! The only options seem to be fighting the troll or running from it. Will you run or fight? ").strip().lower()
        if fightorflight=="run":
            print("You make a split-second decision to run from the troll, and you dodge around the next time it swings. As it does, you realize that the way it swings at you feels oddly mechanical, but you don't have time to think about it right now. You wait until the troll swings at you... then run past the troll and out towards the exit!")
            time.sleep(10)
            print("The troll's massive bulk means it can't chase you! As you turn the corner, you see the troll slowly warp into the man you saw, but you aren't about to turn around after that near-death experience.")
            time.sleep(6)
            returnorexplore=input("Now, you stand in front of a crossroads. You can still return to the village and forget about it all, or continue exploring. ").strip().lower()
            if returnorexplore in ("return", "forget", "village",):
                endignore()
            elif returnorexplore in ("continue", "explore"):
                caveorno="Despite your wounds, y"
                explorefunction()  
            else:
                print("You can't do that.")
        elif fightorflight=="fight":
            print("You grab the knife, and wait for an opportunity to stab the troll somewhere vital. As it swipes at you again, you lunge forward and stab the knife straight into its eye! It lets out a deep, ear-shattering roar of agony! You feel elated... until you realize the troll's claw is hurtling through the air towards you. Oh well, shouldn't have fought the deadly, scary troll.")
            health-=100
            break
        else:
            print("You can't do that!")
def explorefunction():
    print(f"You see a path in the woods, composed of dirt and gravel. {caveorno}ou follow it for an hour, until")
if wheregonow not in ("explore"):
    cavesequence()
    encounter()
    reveal()
sys.exit()