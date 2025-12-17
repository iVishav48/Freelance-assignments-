import turtle
import math

def modify_segment(drawer, dist, level):
    if level == 0:
        drawer.forward(dist)
    else:
        piece = dist / 3
        modify_segment(drawer, piece, level - 1)
        drawer.left(60)
        modify_segment(drawer, piece, level - 1)
        drawer.right(120)
        modify_segment(drawer, piece, level - 1)
        drawer.left(60)
        modify_segment(drawer, piece, level - 1)

def create_pattern(artist, edges, length, iterations):
    turn = 360 / edges
    for _ in range(edges):
        modify_segment(artist, length, iterations)
        artist.right(turn)

canvas = turtle.Screen()
canvas.bgcolor("white")
canvas.title("Geometric Pattern")
canvas.tracer(0, 0)

marker = turtle.Turtle()
marker.speed(0)
marker.color("black")

polygon_sides = int(canvas.textinput("Input", "Enter number of sides (3-12):"))
if polygon_sides < 3:
    print("Sides too low, setting to minimum of 3")
elif polygon_sides > 12:
    print("Sides too high, please keep it under 12")

base_length = int(canvas.textinput("Input", "Enter side length (50-400):"))
if base_length < 50:
    print("Length too short, please keep it above 50")
elif base_length > 400:
    print("Length too long, please keep it under 400")

depth_level = int(canvas.textinput("Input", "Enter recursion depth (0-4):"))
if depth_level < 0:
    print("Depth too low, please keep it above 0")
elif depth_level > 4:
    print("Depth too high, please keep it under 4")

radius_calc = base_length / (2 * math.sin(math.pi / polygon_sides))
marker.penup()
marker.goto(0, -radius_calc)
marker.pendown()
marker.setheading(0)

create_pattern(marker, polygon_sides, base_length, depth_level)

canvas.update()
marker.hideturtle()
canvas.mainloop()