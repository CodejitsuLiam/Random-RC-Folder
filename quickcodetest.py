import time
health=100
def main():
    global health
    while health > 0:
        time.sleep(1.0)
        if health <= 0:
            print("You died")
if True:
    main()