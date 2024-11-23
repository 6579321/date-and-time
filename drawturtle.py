import turtle

# Set up the turtle
t = turtle.Turtle()

# Loop to draw a square
for _ in range(4):
    t.forward(100)  # Move the turtle forward by 100 units
    t.left(90)      # Turn the turtle by 90 degrees

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
turtle.done()
