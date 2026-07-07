#yaycode
while True:
    try: 
        pet_type_ip=int(input("Choose the type of pet you want- type 1 for dog, 2 for cat, and 3 for dragon. "))
        if 1<= pet_type_ip <4:
            break
        else:
            print("Please enter 1, 2, or 3 ")
    except ValueError:
        print("Please enter 1, 2, or 3 ")
#values
hunger=80
energy=80
cleanliness=80
happiness=100-(50-(cleanliness/2))-(50-(energy/2))
health=100-(20-(happiness/5))-(40-(hunger/2.5))-(40-(energy/2.5))  
#petmodifiers
if pet_type_ip== 1:
    pet_type= "dog"
    petmoji= "🐕"
    special_bonus= "starts with more hunger"
    hunger=hunger+10
    special_weakness= "starts with less cleanliness"
    cleanliness=cleanliness-10
if pet_type_ip== 2:
    pet_type= "cat"
    petmoji= "🐈"
    special_bonus= "starts with more cleanliness"
    cleanliness=cleanliness+10
    special_weakness= "starts with less energy"
    energy=energy-10
if pet_type_ip== 3:
    pet_type= "dragon"
    petmoji= "🐉"
    special_bonus= "starts with more energy"
    energy=energy+10
    special_weakness= "starts with less hunger"
    hunger=hunger-10
pet_name=input("Choose the name you want for your pet. ")
print("Your pet is " + pet_name + " the " + pet_type + ".\n" + petmoji)
#eastereggs!
if pet_type_ip == 3 and pet_name == "Midlife Crisis":
    print("You need help.")
elif pet_type_ip == 1 and pet_name == "William":
    print("Yo same!!!")
elif pet_type_ip == 2 and pet_name == "Binka":
    print("RIP")
x_row_health= "x" * int(health/10)
x_row_hunger= "x" * int(hunger/10)
x_row_happiness= "x" * int(happiness/10)
print("Starting happiness: " + x_row_happiness)
print("Starting health: " + x_row_health)
print("Starting hunger: " + x_row_hunger)
#firstweek
day=0
while health>0 and day<8: 
    action=input("A new day begins... what do you want to do? Enter 1 to rest your pet, enter 2 to feed your pet, and enter 3 to clean your pet. You can also press 4 to do nothing. ")
    if action== "1":
        energy=energy+20
    elif action== "2":
        hunger=hunger+20
    elif action== "3":
        cleanliness=cleanliness+20
    elif action== "4":
        pass
    else:
        print("That is not an option!")
    action2=input("The day comes to an end... Choose something to do at the end of the day. The same rules as before apply. ")
    if action2== "1":
        energy=energy+10
    elif action2== "2":
        hunger=hunger+10
    elif action2== "3":
        cleanliness=cleanliness+10
    elif action2== "4":
        pass
    else:
        print("That is not an option!")
    if hunger > 100:
        print(pet_name + "'s belly is full!")
        hunger = 100
    elif hunger < 0:
        print(pet_name + " is very hungry...")
        hunger = 0
    if cleanliness > 100:
        print(pet_name + " is squeaky clean!")
        cleanliness = 100
    elif cleanliness < 0:
        print(pet_name + " is very dirty...")
        cleanliness = 0
    if energy > 100:
        print(pet_name + " is bouncing off the walls!")
        energy = 100
    elif energy < 0:
        print(pet_name + " needs some sleep...")
        energy = 0
    happiness=100-(50-(cleanliness/2))-(50-(energy/2))
    health=100-(20-(happiness/5))-(40-(hunger/2.5))-(40-(energy/2.5))
    x_row_health= "x" * int(health/10)
    x_row_hunger= "x" * int(hunger/10)
    x_row_happiness= "x" * int(happiness/10)
    print("Happiness: " + str(x_row_happiness))
    print("Health: " + str(x_row_health))
    print("Hunger: " + str(x_row_hunger))
    energy -=10
    hunger -=10
    cleanliness -=10
    day=day+1
    if health <=0:
        print("\033[31mGame Over!\033[0m")
        import sys
        sys.exit()
#everythingafter
print("\033[33mAfter a week, you have unlocked new options to use... a spa day, a big meal, and a bath. All of these will greatly increase the stat they correspond to, but you cannot choose a second option.\033[0m")
while health>0 and day>=8:
    action=input("A new day begins... what do you want to do? Enter 1 to rest your pet, 2 to give your pet a spa day, 3 to feed your pet, 4 to feed them a big meal, 5 to clean your pet, and 6 to give your pet a bath. You can also press 7 to do nothing. ")
    if action== "1":
        energy=energy+20
    elif action== "3":
        hunger=hunger+20
    elif action== "5":
        cleanliness=cleanliness+20
    elif action== "2":
        energy=energy+35
    elif action== "4":
        hunger=hunger+35
    elif action== "6":
        cleanliness=cleanliness+35
    elif action== "7":
        pass
    else:
        print("That is not an option!")
    action2=None
    if action in ['1', '3', '5', '7']:
        action2=input("The day comes to an end... Choose something to do at the end of the day. Enter 1 to rest your pet, enter 2 to feed your pet, and enter 3 to clean your pet. You can also press 4 to do nothing. ")
    if action2 is not None:
        if action2== "1":
            energy=energy+10
        elif action2== "2":
            hunger=hunger+10
        elif action2== "3":
            cleanliness=cleanliness+10
        elif action2== "4":
            pass
        else:
            print("That is not an option!")
    import random
    events = [    "Your pet played around in the mud!",
    "You forgot to feed your pet!",
    "Your pet stayed up all night!",
    "Nothing happened"    ]
    event_percentages = [10,10,10,70]
    selected_event = random.choices(events, weights=event_percentages, k=1)[0]
    if selected_event == "Nothing happened":
        pass
    elif selected_event == "Your pet played around in the mud!":
        cleanliness=cleanliness-30
        print(pet_name+"\033[33m played around in the mud!\033[0m")
    elif selected_event == "You forgot to feed your pet!":
        hunger=hunger-30
        print("\033[33mYou forgot to feed your pet!\033[0m")
    elif selected_event == "Your pet stayed up all night!":
        energy=energy-30
        print(pet_name+"\033[33m stayed up all night!\033[0m")
    if hunger > 100:
        print(pet_name + "'s belly is full'!")
        hunger = 100
    elif hunger < 0:
        print(pet_name + " is very hungry...")
        hunger = 0
    if cleanliness > 100:
        print(pet_name+" is squeaky clean!")
        cleanliness = 100
    elif cleanliness < 0:
        print(pet_name+" is very dirty...")
        cleanliness = 0
    if energy > 100:
        print(pet_name+" is bouncing off the walls!")
        energy = 100
    elif energy < 0:
        print(pet_name+" needs some sleep...")
        energy = 0
    happiness=100-(50-(cleanliness/2))-(50-(energy/2))
    health=100-(20-(happiness/5))-(40-(hunger/2.5))-(40-(energy/2.5))
    x_row_health= "x" * int(health/10)
    x_row_hunger= "x" * int(hunger/10)
    x_row_happiness= "x" * int(happiness/10)
    print("Happiness: " + str(x_row_happiness))
    print("Health: " + str(x_row_health))
    print("Hunger: " + str(x_row_hunger))
    energy -=5
    hunger -=5
    cleanliness -=5
    day=day+1
    if health <=0:
        print("\033[31mGame Over!\033[0m")
        import sys
        sys.exit()
import sys
sys.exit()