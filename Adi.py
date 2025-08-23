import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral")

# Create the turtle
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
turtle.colormode(255)

# Function to draw a colorful spiral
def draw_spiral():
    num_colors = 36
    hue = 0
    for i in range(360):
        color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
        t.pencolor(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
        t.forward(i * 2)
        t.right(59)
        hue += 1 / num_colors

# Call the function
draw_spiral()

# Keep the window open
turtle.done()
