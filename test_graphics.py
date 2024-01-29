from graphics import *

# Instantiate Graphics Window
win = GraphWin('my window', 1000, 1000)

# Start your nested loops here

for x in range(100):

    for y in range(100):
        # Calculate Top-Left and Bottom-Right Coordinates: Use rectangles instead of circles
        top_left_x = 30 + 100 * x / 2 - 12.5
        top_left_y = y * 50 - 25

        bottom_right_x = top_left_x + 25
        bottom_right_y = top_left_y + 50

        # Create Rectangle Object:
        rect = Rectangle(Point(top_left_x, top_left_y), Point(bottom_right_x, bottom_right_y))

        # Set Outline and Fill Colors: Experiment with making custom colors
        rect.setOutline(color_rgb(100, 100, 250))
        rect.setFill(color_rgb(100, 200, 100))

        # Draw the Rectangle:
        rect.draw(win)

        # Make a diagonal line of shapes
        if x == y:
            # Update colors for the diagonal line
            rect.setOutline(color_rgb(250, 100, 100))
            rect.setFill(color_rgb(200, 100, 100))

# end your loop here

# Wait for a mouse click to close the Graphics window
win.getMouse()
