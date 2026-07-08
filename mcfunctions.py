def build_tower():
    for floor in range(3):
        print("Starting floor ", floor+1)
        for block in range(4):
            print("Placing block ", block+1)
def collect_logs():
    for i in range(64):
        print(f"choop log {i+1}")
        if i==59:
            print("Inventory nearly full!") 

def night_patrol():
    energy=100
    while energy>0:
        print("Patrolling...")
        energy=energy-12
        if 0<energy<30:
            print("Warning: Low Power!")
        if energy<=0:
            energy=0
            print("Shutting down...")
            import sys
            sys.exit()
        print(energy)
        import time
        time.sleep(1)#iknowitsasecondnotaminutebutwhowantstowaitawholeminuteifyoureallywantittoactuallybeaminutemakeit60
night_patrol()