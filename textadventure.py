import time
import random
import sys
import threading
inventory=[]
health=100
health_stop = threading.Event()
caveorno=None
wheregonow=None
enterorwalk=None
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
            inventory.append("a knife")
            print("You decide to grab the knife, knowing it may come in handy. ")
            time.sleep(2)
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
            print("\033[95mAchievent Unlocked\033[0m")
            time.sleep(1)
            print("\033[95mSOUS\033[0m")
            time.sleep(1)
            global firstattack
            firstattack=input("\033[31mA spider of unusual size leaps out of the shadows! What will you do? \033[0m(Run or Fight)").strip().lower()
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
                time.sleep(4)
                print("One of the spider's eyes pops out from its socket. You're disgusted, but you figure you should take anything you get. ")
                time.sleep(4)
                inventory.append("the spider's eye")
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
                global enterredcave
                enterredcave="didnt"
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
            time.sleep(2)
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
        global enterorwalk
        enterorwalk=input("Do you enter the tunnel to see what lurks inside, do you continue exploring the caves, or do you leave the cave entirely? (Enter, Explore or Leave) ").strip().lower()
        if enterorwalk=="explore":
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
            global enterredcave
            enterredcave="left"
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
            time.sleep(11)
            print("The troll's massive bulk means it can't chase you! As you turn the corner, you see the troll slowly warp into the man you saw, but you aren't about to turn around after that near-death experience.")
            time.sleep(6)
            returnorexplore=input("Now, you stand in front of a crossroads. You can still return to the village and forget about it all, or continue exploring. ").strip().lower()
            if returnorexplore in ("return", "forget", "village",):
                endignore()
            elif returnorexplore in ("continue", "explore"):
                global enterredcave
                caveorno="Despite your wounds, y"
                enterredcave="sawtroll"
                explorefunction()
                break
            else:
                print("You can't do that.")
        elif fightorflight=="fight":
            print("\033[95mAchievement Unlocked\033[0m")
            time.sleep(1)
            print("You grab the knife, and wait for an opportunity to stab the troll somewhere vital. As it swipes at you again, you lunge forward and stab the knife straight into its eye! It lets out a deep, ear-shattering roar of agony! You feel elated... until you realize the troll's claw is hurtling through the air towards you. Oh well, shouldn't have fought the deadly, scary troll.")
            time.sleep(9)
            print("\033[95mNoob vs. Thanos\033[0m")
            health-=100
            break
        else:
            print("You can't do that!")
def sagenpc():
    print("npc")
def sageintro():
    print("As you walk into the central plaza, a small circular area paved with cobblestones, you immediately see what the stand owner meant. One building stands out from the others, radiating a sense of knowledge and wisdom.")
    time.sleep(5)
    print("You enter the building, and go up a set of stairs with a sign that says \"Ascend these stairs to seek advice from the sage.\" As you emerge onto the second floor, you see the sage with her back to you.")
    time.sleep(7)
    print("Feeling slightly intimidated, you cautiously approach, but before you get near her, she says in a raspy voice, \"Well? Will you introduce yourself to me, or will I have to call you Mysterious Adventurer for the rest of this hopefully short conversation?\"")
    time.sleep(8)
    print("Shakily, you say, \"How... did you know I was there?\"")
    time.sleep(3)
    print("She replies sarcastically, \"As a sage I am all-knowing... of course not, I heard you on the stairs. Now, sit, and introduce yourself.\"")
    time.sleep(6)
    print("You take a seat on the floor across from her, and say, \"I come from a village not far away. Just this morning, an adventurer stumbled out of the woods, and before death, he told me to avenge him by going to a cave, where he met his untimely fate.\"")
    time.sleep(8)
    print("\"Well?\" The sage interrupts. \"Did you go to cave?\"")
    time.sleep(3)
    if enterredcave=="sawtroll":
        print("\"Well, \" you say with some annoyance, \"I entered the cave, where I saw that very same adventurer turn into a troll and try to kill me.\"")
        time.sleep(6)
        print("After a few seconds, she says, \"Ah, that's quite bad. What you encountered was not a troll or the adventurer, but a malevolent shapeshifter. Harken to my words as I tell you a tale... of magic gone wrong.\"")
        time.sleep(8)
    if enterredcave=="didnt":
        print("\"Not quite...\" you say, cringing internally. The least you could have done for the poor soul was honor his dying wish.")
        time.sleep(5)
        print("She gives you a hard stare. \"You wimped out, didn't you?\"")
        time.sleep(3)
        print("\"Yeah.\" You say with a wince. \"But now that I'm here, I realize that may not have been the smartest move.\"")
        time.sleep(5)
        print("\"Too late for realizations. Where was the cave, anyway?\" You tell her, and she thinks for a minute or two. Finally, she says, \"I know of a terrible beast, a malevolent shapeshifter, that prowls that area, searching for victims. It's quite likely that was what killed the adventurer.\"")
        time.sleep(9)
        print("\"Harken to my words, \" she says, \"as I tell you a tale... of magic gone wrong.")
        time.sleep(4)
    if enterredcave=="left":
        print("\"Not quite... I entered the cave, but I... left.\" you say, cringing internally. The least you could have done for the poor soul was honor his dying wish.")
        time.sleep(5)
        print("She gives you a hard stare. \"You wimped out, didn't you?\"")
        time.sleep(3)
        print("\"Yeah.\" You say with a wince. \"But now that I'm here, I realize that may not have been the smartest move.\"")
        time.sleep(5)
        print("\"Too late for realizations. Where was the cave, anyway?\" You tell her, and she thinks for a minute or two. Finally, she says, \"I know of a terrible beast, a malevolent shapeshifter, that prowls that area, searching for victims. It's quite likely that was what killed the adventurer.\"")
        time.sleep(9)
        print("\"Harken to my words, \" she says, \"as I tell you a tale... of magic gone wrong.")
        time.sleep(4)
    sagenpc()
def townintro():
    print("You emerge from the woods, and your mind flashes back to this morning when you saw the adventurer do the very same.")
    time.sleep(5)
    if wheregonow=="explore":
        print("It occurs to you that you probably should have gone into the cave, but there's no point in turning back now.")
        time.sleep(5)
    if enterorwalk=="leave":
        print("It occurs to you that you shouldn't have left the cave so soon- you haven't learned that much about what killed the adventurer.")
        time.sleep(5)
    print("As you walk through the town, you here someone yelling, \"Magic Items for sale! Bring something of value, and you'll get to take an item of similar value!\"")
    time.sleep(5)
    print("Intrigued, you wander over to the stand. The owner sees you, and says to you, \"Might you have any items to trade?\"")
    while True:
        viewe=input("Do you wish to look into your inventory to see what you have to trade?").strip().lower()
        if viewe in ("yes", "y", "e", "inventory", "look", "trade"):
            for item in inventory:
                print(f"You have {item}.")
            print("The owner leans over excitedly. \"A spider's eye, huh? Well, I'll  be! You must be an adventurer!\" He says.")
            time.sleep(5)
            print("You reply without much enthusiasm, \"I guess. Really, I'm just on a quest, and then I'll probably go back to my village forever.\"")
            time.sleep(5)
            print("\"Either way, \" the owner says, \"do want to trade that for anything?\"")
            time.sleep(3)
            print("You think for a few seconds. Eventually, you reply, \"I'd like to figure out what I should do first, so I have a better idea of what to use it for.\"")
            time.sleep(5)
            print("The owner nods and says, \"If you're on quest and looking for advice, there is a wise sage at the center of the town, who used to be an adventurer herself. You'll know where she is when you see it.\" You thank him and head towards the town center.\"")
            time.sleep(8)
            break

        elif viewe in ("no", "n"):
            print("You say to the owner of the stand, \"Sorry, but I'm not really interested right now. However, I'm on a quest, so if you could point me toward someone with much knowledge of the world, that would be greatly appreciated.\"")
            time.sleep(8)
            print("The owner nods. \"There is a wise sage at the center of the town, who used to be an adventurer herself. You'll know where she is when you see it.\" You thank him and head towards the town center.")
            time.sleep(6)
            print("")
            break
        else:
            print("That is not an option!")
        sageintro()
def explorefunction():
    print(f"You see a path in the woods, composed of dirt and gravel. {caveorno}ou follow it for an hour, until you see a town in the distance through the trees.")
    time.sleep(6)
    jimothyevent=["Nothing happens", "JIMOTHY"]
    jimothymuchweight=[70,30]
    jimothy=random.choices(jimothyevent, weights=jimothymuchweight, k=1)[0]
    if jimothy=="Nothing happens":
        pass
    if jimothy=="JIMOTHY":
        raccoonname=input("As you approach the town, you see an oddly spherical raccoon. What will you name him? ")
        print(f"You named the raccoon {raccoonname}.")
        if raccoonname in ("Jimothy", "jimothy",):
            print("\033[95mAchievement Unlocked\033[0m")
            time.sleep(1)
            print("\033[95mJIMOTHY!!!\033[0m")
            time.sleep(1)
    townintro()

cavesequence()
encounter()
reveal()
sys.exit()