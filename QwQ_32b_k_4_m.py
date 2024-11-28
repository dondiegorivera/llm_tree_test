import turtle

def draw_tree(branch_length, angle, depth):
    if depth == 0:
        return
    
    # Draw the main branch
    turtle.pendown()
    turtle.forward(branch_length)
    
    # Turn left and draw left subtree
    turtle.left(angle)
    draw_tree(0.75 * branch_length, angle, depth - 1)
    
    # Turn right and draw right subtree
    turtle.right(2 * angle)
    draw_tree(0.75 * branch_length, angle, depth - 1)
    
    # Return to the previous position
    turtle.left(angle)
    turtle.penup()
    turtle.backward(branch_length)

def main():
    # Set up the screen and turtle
    turtle.speed(0)  # Set speed to fastest
    turtle.penup()
    turtle.goto(0, -200)  # Position at the bottom of the screen
    turtle.setheading(90)  # Point upwards
    
    # Draw the tree
    draw_tree(100, 30, 5)
    
    # Keep the window open
    turtle.done()

if __name__ == "__main__":
    main()
