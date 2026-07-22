import turtle
import time
import sys

screen = turtle.Screen()
screen.title("Spider Escape!")
screen.bgcolor("dimgray")
screen.setup(width=600, height=600)
screen.tracer(0) 

human_shape = turtle.Shape("compound")
human_shape.addcomponent(((0,12), (3,15), (0,18), (-3,15)), "royalblue")
human_shape.addcomponent(((0,12), (0,0), (-8,-12), (-5,-12), (0,-2)), "royalblue")
human_shape.addcomponent(((0,-2), (5,-12), (8,-12), (0,0)), "royalblue")
human_shape.addcomponent(((0,8), (-10,4), (-8,2), (0,6)), "royalblue")
human_shape.addcomponent(((0,6), (8,2), (10,4), (0,8)), "royalblue")
screen.register_shape("human", human_shape)
spider_shape = turtle.Shape("compound")
spider_shape.addcomponent(((0,-6), (6,0), (0,8), (-6,0)), "black")
spider_shape.addcomponent(((0,-6), (4,-10), (0,-14), (-4,-10)), "black")
spider_shape.addcomponent(((0,4), (14,10), (16,8), (0,2)), "black")
spider_shape.addcomponent(((0,4), (-14,10), (-16,8), (0,2)), "black")
spider_shape.addcomponent(((0,2), (16,3), (16,1), (0,0)), "black")
spider_shape.addcomponent(((0,2), (-16,3), (-16,1), (0,0)), "black")
spider_shape.addcomponent(((0,0), (15,-5), (14,-7), (0,-2)), "black")
spider_shape.addcomponent(((0,0), (-15,-5), (-14,-7), (0,-2)), "black")
spider_shape.addcomponent(((0,-4), (12,-14), (10,-15), (0,-6)), "black")
spider_shape.addcomponent(((0,-4), (-12,-14), (-10,-15), (0,-6)), "black")
screen.register_shape("spider", spider_shape)

GRID_SIZE = 40
MOVE_DIST = 40
BOUNDS = 240 
player_moves_left = 2
player_health = 100
exit_portal = turtle.Turtle()
exit_portal.shape("square")
exit_portal.color("gold")
exit_portal.shapesize(2, 2) 
exit_portal.penup()
exit_portal.goto(0, 200) 

player = turtle.Turtle()
player.shape("human")
player.setheading(90)
player.penup()
player.goto(0, -200)

enemy = turtle.Turtle()
enemy.shape("spider")
enemy.setheading(0)
enemy.penup()
enemy.goto(0, 0)

def trigger_catch_event():
    """Triggered when the spider touches the human player."""
    global player_moves_left, player_health
    screen.bgcolor("darkred")
    screen.update()
    time.sleep(0.4) 

    player_health -= 20
    player_moves_left = 2
    print(f"Health: {player_health}")
    screen.bgcolor("dimgray")

def trigger_victory_event():
    """Triggered when the human player safely reaches the portal."""
    global player_moves_left
    screen.bgcolor("limegreen")
    screen.update()
    time.sleep(0.5)
    
    player_moves_left = 2
    screen.bye()
    sys.exit()

def check_collisions():
    if player.distance(enemy) < 20:
        trigger_catch_event()
        return True
    if player.distance(exit_portal) < 20:
        trigger_victory_event()
        return True
    return False

def enemy_turn():
    """Spider AI: Moves one step closer to the player."""
    global player_moves_left
    if check_collisions():
        return

    dx = player.xcor() - enemy.xcor()
    dy = player.ycor() - enemy.ycor()

    if abs(dx) > abs(dy):
        step = MOVE_DIST if dx > 0 else -MOVE_DIST
        enemy.setx(enemy.xcor() + step)
        if dx > 0:
            enemy.setheading(0)
        else:
            enemy.setheading(180)
    else:
        step = MOVE_DIST if dy > 0 else -MOVE_DIST
        enemy.sety(enemy.ycor() + step)
        if dy > 0:
            enemy.setheading(90)
        else:
            enemy.setheading(270)

    check_collisions()
    player_moves_left = 2

def handle_player_move(new_x, new_y):
    global player_moves_left
    
    if abs(new_x) <= BOUNDS and abs(new_y) <= BOUNDS:
        player.goto(new_x, new_y)
        player_moves_left -= 1
        
        if not check_collisions():
            if player_moves_left == 0:
                screen.update()
                time.sleep(0.15) 
                enemy_turn()

def go_up():
    handle_player_move(player.xcor(), player.ycor() + MOVE_DIST)

def go_down():
    handle_player_move(player.xcor(), player.ycor() - MOVE_DIST)

def go_left():
    handle_player_move(player.xcor() - MOVE_DIST, player.ycor())

def go_right():
    handle_player_move(player.xcor() + MOVE_DIST, player.ycor())

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

while True:
    screen.update()