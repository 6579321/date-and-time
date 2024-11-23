import turtle

# Set up the turtle
t = turtle.Turtle()

# Define the side length for the triangle
side_length = 100

# Draw the right-angled triangle
t.forward(side_length)  # Draw the base of the triangle
t.left(90)              # Turn 90 degrees to draw the height
t.forward(side_length)  # Draw the height of the triangle
t.left(135)             # Turn to draw the hypotenuse
t.forward(side_length * (2 ** 0.5))  # Draw the hypotenuse (Pythagorean theorem)

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open
turtle.done()

