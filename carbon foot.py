#Values
Electrical=0.3
Gaseous=0.45
Induction=0.18
Bus=0.2
Light_Rail=0
Foot=0.4
By_Car=1.06
Plane=0.15
Electric=0.14
Gas=0.4
Hybrid=0.25
Lights=0.05
Computer=0.06
Showers=1.2
Air_Conditioning=1
print("Welcome to the carbon footprint calculator! ")
showers=input("How many showers do you take per day? ")
lights=input("How many hours per day are your lights on? ")
lights2=input("How many lights do you have in your house? ")
meals=input("How many meals do you cook per day? ")
stove=input("What kind of stove do you have? (Type exactly Electrical, Gaseous, or Induction) ")
if stove=="Electrical":
    stove=Electrical
if stove=="Gaseous":
    stove=Gaseous
if stove=="Induction":
    stove=Induction
computer=input("How many hours per day do you use your computer? ")
transportation=input("What kind of transportation do you use? (Type exactly Car, Bus, Light_Rail, Ferry, or Plane) ")
if transportation=="Plane":
    transportation6=input("How many miles do you fly per year? ")
    Transportation_Total=(float(transportation6)*float(Plane))/365
if transportation=="Car":
    transportation2=input("What kind of car do you drive? (Type exactly Electric, Gas, or Hybrid) ")
    transportation3=input("How many miles do you drive per day? ")
    if transportation2=="Hybrid":
        transportation2=Hybrid
    if transportation2=="Gas":
        transportation2=Gas
    if transportation2=="Electric":
        transportation2=Electric
    Transportation_Total=float(transportation2)*float(transportation3)
if transportation=="Ferry":
    transportation4=input("Do you you take the ferry on foot or by car? (Type exactly Foot or By_Car) ")
    transportation5=input("How many trips do you take on the ferry per week? ")
    if transportation4=="Foot":
        transportation4=Foot
    if transportation4=="By_Car":
        transportation4=By_Car
    Transportation_Total=(float(transportation5)*float(transportation4))/7
if transportation=="Light_Rail":
    Transportation_Total=Light_Rail
if transportation=="Bus":
    Transportation_Total=Bus
transportation7=input("Do you have another notable method of transportation? (Type exactly Yes or No) ")
if transportation7=="No":
    Transportation_Total2=0
if transportation7=="Yes":
    transportation8=input("What kind of transportation do you use? (Type exactly Car, Bus, Light_Rail, Ferry, or Plane) ")
    if transportation8=="Plane":
        transportation10=input("How many miles do you fly per year? ")
        Transportation_Total2=(float(transportation10)*float(Plane))/365
    if transportation8=="Car":
        transportation9=input("What kind of car do you drive? (Type exactly Electric, Gas, or Hybrid) ")
        transportation12=input("How many miles do you drive per day? ")
        if transportation9=="Hybrid":
            transportation9=Hybrid
        if transportation9=="Gas":
            transportation9=Gas
        if transportation9=="Electric":
            transportation9=Electric
        Transportation_Total2=float(transportation9)*float(transportation12)
    if transportation8=="Ferry":
        transportation10=input("Do you you take the ferry on foot or by car? (Type exactly Foot or By_Car) ")
        if transportation10=="Foot":
            transportation10=Foot
        if transportation10=="By_Car":
            transportation10=By_Car
        transportation11=input("How many trips do you take on the ferry per week? ")
        Transportation_Total2=(float(transportation11)*float(transportation10))/7
    if transportation8=="Light_Rail":
        Transportation_Total2=float(Light_Rail)
    if transportation8=="Bus":
        Transportation_Total2=float(Bus)
ac=input("How many hours per day is your AC on? ")
Showers_Total=float(showers)*Showers
Lights_Total=float(lights)*float(lights2)*Lights
Meals_Stove_Total=float(meals)*float(stove)
Computer_Total=float(computer)*Computer
Transportation_Final_Total=float(Transportation_Total)+float(Transportation_Total2)
Ac_Total=float(ac)*float(Air_Conditioning)
Cumulative_Total=Showers_Total+Lights_Total+Meals_Stove_Total+Computer_Total+Transportation_Final_Total+Ac_Total
print("Your total carbon footprint is", Cumulative_Total, "kg of CO2 per day.")
import sys
sys.exit()