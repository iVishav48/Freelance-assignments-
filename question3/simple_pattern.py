import turtle
import math

def make_bumpy_line(pen, length, bumpiness):
    if bumpiness == 0:
        pen.forward(length)
    else:
        small_piece = length / 3
        
        make_bumpy_line(pen, small_piece, bumpiness - 1)
        pen.left(60)
        make_bumpy_line(pen, small_piece, bumpiness - 1)
        pen.right(120)
        make_bumpy_line(pen, small_piece, bumpiness - 1)
        pen.left(60)
        make_bumpy_line(pen, small_piece, bumpiness - 1)

def draw_shape(pen, sides, edge_length, bumpiness):
    corner_turn = 360 / sides
    
    for side in range(sides):
        make_bumpy_line(pen, edge_length, bumpiness)
        pen.right(corner_turn)

def get_user_input():
    sides = int(input("How many sides for your shape? (3-12): "))
    if sides < 3:
        sides = 3
        print("That's too few! Let's use 3 sides (a triangle).")
    elif sides > 12:
        sides = 12
        print("That's a lot! Let's use 12 sides to keep it manageable.")
    
    length = int(input("How long should each side be? (50-400): "))
    if length < 50:
        length = 50
        print("That's too short! Let's use 50 pixels.")
    elif length > 400:
        length = 400
        print("That's too long! Let's use 400 pixels.")
    
    bumps = int(input("How bumpy should the lines be? (0-4, 0=smooth, 4=very bumpy): "))
    if bumps < 0:
        bumps = 0
        print("Can't have negative bumps! Let's use 0 (smooth lines).")
    elif bumps > 4:
        bumps = 4
        print("That's too bumpy! Let's use 4 to keep it from getting too crazy.")
    
    return sides, length, bumps

def center_the_shape(pen, sides, length):
    circle_radius = length / (2 * math.sin(math.pi / sides))
    
    pen.penup()
    pen.goto(0, -circle_radius)
    pen.pendown()
    pen.setheading(0)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Let's Draw a Bumpy Shape!")
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.color("blue")
    
    print("Welcome to the Bumpy Shape Drawer!")
    print("Let's create a beautiful geometric pattern together.\n")
    
    sides, length, bumps = get_user_input()
    
    center_the_shape(pen, sides, length)
    
    print(f"\nDrawing your {sides}-sided shape with bumpiness level {bumps}...")
    draw_shape(pen, sides, length, bumps)
    
    pen.hideturtle()
    
    print("All done! Look at your beautiful creation!")
    print("Close the window when you're ready to quit.")
    
    window.mainloop()

if __name__ == "__main__":
    main()
