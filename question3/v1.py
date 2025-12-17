import turtle
import math

def draw_koch_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        segment_length = length / 3
        draw_koch_edge(t, segment_length, depth - 1)
        t.left(60)
        draw_koch_edge(t, segment_length, depth - 1)
        t.right(120)
        draw_koch_edge(t, segment_length, depth - 1)
        t.left(60)
        draw_koch_edge(t, segment_length, depth - 1)

def draw_polygon(t, sides, side_length, depth):
    angle = 360 / sides
    for i in range(sides):
        draw_koch_edge(t, side_length, depth)
        t.right(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Recursive Geometric Pattern")
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    t.color("black")
    
    sides_input = screen.textinput("Input", "Enter the number of sides:")
    sides = int(sides_input)
    
    length_input = screen.textinput("Input", "Enter the side length:")
    side_length = int(length_input)
    
    depth_input = screen.textinput("Input", "Enter the recursion depth:")
    depth = int(depth_input)
    
    radius = side_length / (2 * math.sin(math.pi / sides))
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.setheading(0)
    
    draw_polygon(t, sides, side_length, depth)
    
    t.hideturtle()
    screen.mainloop()

main()