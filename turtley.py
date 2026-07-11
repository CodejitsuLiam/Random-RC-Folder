import turtle
screen=turtle.Screen()
screen.title("Move the player")

TILE = 32
dungeon = [
"############################",
"#............D.............#",
"#............#.............#",
"#............#.............#",
"######D###########D#########",
"#..........................#",
"#..........................#",
"###########D############...#",
"#..........................#",
"#..........................#",
"############################"
]

ROWS = len(dungeon)
COLS = len(dungeon[0])

screen = turtle.Screen()
screen.setup(1000,700)
screen.bgcolor("black")
screen.title("Dungeon")
screen.tracer(0)

draw = turtle.Turtle()
draw.hideturtle()
draw.penup()
draw.shape("square")
draw.shapesize(TILE/20)

startx = -COLS*TILE/2
starty = ROWS*TILE/2

# Draw map
for y,row in enumerate(dungeon):
    for x,tile in enumerate(row):

        draw.goto(startx+x*TILE,starty-y*TILE)

        if tile=="#":
            draw.color("dimgray")
        elif tile=="D":
            draw.color("sienna")
        else:
            draw.color("lightgray")

        draw.stamp()

# Player
player=turtle.Turtle()
player.penup()
player.shape("turtle")
player.color("lime")


player_x=1
player_y=1

player.goto(startx+player_x*TILE,starty-player_y*TILE)

vx=0
vy=0

def can_move(nx,ny):
    if nx<0 or ny<0 or nx>=COLS or ny>=ROWS:
        return False

    return dungeon[ny][nx]!="#"

# Key handlers
def left():
    global vx,vy
    vx=-1
    vy=0

def right():
    global vx,vy
    vx=1
    vy=0

def up():
    global vx,vy
    vx=0
    vy=-1

def down():
    global vx,vy
    vx=0
    vy=1


# Game loop
def update():
    global player_x,player_y

    nx=player_x+vx
    ny=player_y+vy

    if can_move(nx,ny):
        player_x=nx
        player_y=ny

        # Sync the visible turtle's heading with the movement direction
        if vx == -1:
            player.setheading(180)
        elif vx == 1:
            player.setheading(0)
        elif vy == -1:
            player.setheading(90)
        elif vy == 1:
            player.setheading(270)

        player.goto(
            startx+player_x*TILE,
            starty-player_y*TILE
        )

    screen.update()
    screen.ontimer(update,120)

update()
MOVE_DISTANCE=20
def move_up():
    player.setheading(90)
    player.forward(MOVE_DISTANCE)
def move_down():
    player.setheading(270)
    player.forward(MOVE_DISTANCE)
def move_left():
    player.setheading(180)
    player.forward(MOVE_DISTANCE)
def move_right():
    player.setheading(0)
    player.forward(MOVE_DISTANCE)
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.mainloop()