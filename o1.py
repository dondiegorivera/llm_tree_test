import turtle
import random

def draw_tree(branch_length, pen, thickness):
    """
    Recursively draw a fractal tree.
    
    :param branch_length: The length of the current branch segment.
    :param pen: The turtle (pen) used for drawing.
    :param thickness: The current thickness of the branches.
    """
    # If the branch is too short, draw a leaf (small green dot) and stop.
    if branch_length < 10:
        pen.color("green")
        pen.dot(6)  # Draw a small circle to represent leaves
        pen.color("brown")
        return

    # Set the current pen thickness for realistic trunk/branches
    pen.pensize(thickness)

    # Move forward by branch_length
    pen.forward(branch_length)

    # Choose a random angle and random reduction in length for sub-branches
    angle = random.randrange(15, 40)          # Random angle between 15 and 40 degrees
    length_reduction = random.randrange(10, 20)  # Randomly shorten sub-branches

    # Turn right for the first branch
    pen.right(angle)
    draw_tree(branch_length - length_reduction, pen, thickness - 1)

    # Turn left twice the angle for the second branch (to swing from the right side to the left side)
    pen.left(angle * 2)
    draw_tree(branch_length - length_reduction, pen, thickness - 1)

    # Re-center the heading
    pen.right(angle)

    # Move back to the original position
    pen.backward(branch_length)


def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("skyblue")
    screen.title("Realistic Fractal Tree")

    # Create our drawing turtle (pen)
    pen = turtle.Turtle()
    pen.speed("fastest")  # Speed up the drawing
    pen.color("brown")
    pen.left(90)          # Face upwards

    # Move the turtle down so there's space for the tree to grow
    pen.up()
    pen.goto(0, -250)
    pen.down()

    # Draw the tree, starting with a fairly tall trunk and a thicker base
    draw_tree(branch_length=80, pen=pen, thickness=8)

    pen.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
