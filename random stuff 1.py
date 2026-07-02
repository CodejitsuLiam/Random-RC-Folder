nameOG = "Bobificus"
adjectiveOG = "amazing"
name2OG = "Maximillius Pontrificus the 2nd"
adjective2OG = "very goofy"
adjective3OG = "peaceful"
verbOG = "run"
verb2OG = "attack" 
nounOG = "book"
noun2OG = "sword"
noun3OG = "castle"
#This is the way to make things interactive. Haven't figured out a way to turn it off yet.
name=input("Type a name and press enter: ")
adjective=input("Type an adjective and press enter: ")
name2=input("Type another name and press enter: ")
adjective2=input("Type another adjective and press enter: ")
adjective3=input("Type another adjective and press enter: ")
verb=input("Type a verb and press enter: ")
verb2=input("Type another verb and press enter: ")
noun=input("Type a noun and press enter: ")
noun2=input("Type another noun and press enter: ")
noun3=input("Type another noun and press enter: ")


print("\t" + "Once upon a time, there was a person named " + name + ". " + name + " was " + adjective + ".")
print("There was also a person named " + name2 + ". " + name2 + " was " + adjective2 + ".")
print("One day, the " + noun3 + " was too " + adjective3 + " so " + name + " and " + name2 + " decided to " + verb2 + " an enemy " + noun3 + ".")
print("The " + verb2 + " failed terribly, and they were forced to " + verb + ".")
print("After returning, " + name + " found a " + noun + " that taught the secrets of the universe to whoever read it.")
sys.exit()
