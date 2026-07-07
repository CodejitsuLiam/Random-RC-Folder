for floor in range(3):
    print("Starting Floor", floor+1)
    for block in range(4):
        print("  Placing block", block+1)
for row in range(1,5):
    for col in range(1, row+1):
        print(col, end=" ")
    print()
    