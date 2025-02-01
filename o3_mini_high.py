import turtle
import random

def draw_tree(t, branch_length, thickness):
    """
    Recursively draws a tree.
    
    Parameters:
      t            -- turtle object used for drawing
      branch_length-- the current branch length
      thickness    -- the current pen thickness for the branch
    """
    # Base case: stop when the branch is too small to draw further
    if branch_length > 5:
        # Set the thickness and color: thinner branches are drawn in green
        t.pensize(thickness)
        if branch_length < 20:
            t.color("green")
        else:
            t.color("sienna")
        
        # Draw the current branch
        t.forward(branch_length)
        
        # Save the current position and heading
        current_pos = t.position()
        current_heading = t.heading()
        
        # Draw the right branch
        right_angle = random.uniform(15, 45)
        length_reduction = random.uniform(0.7, 0.9)
        t.right(right_angle)
        draw_tree(t, branch_length * length_reduction, thickness * length_reduction)
        
        # Restore the state after drawing the right branch
        t.penup()
        t.setposition(current_pos)
        t.setheading(current_heading)
        t.pendown()
        
        # Draw the left branch
        left_angle = random.uniform(15, 45)
        length_reduction = random.uniform(0.7, 0.9)
        t.left(left_angle)
        draw_tree(t, branch_length * length_reduction, thickness * length_reduction)
        
        # Restore state again before backtracking
        t.penup()
        t.setposition(current_pos)
        t.setheading(current_heading)
        t.pendown()
        
        # Backtrack to the previous branch's base
        t.backward(branch_length)

def main():
    # Set up the drawing window
    screen = turtle.Screen()
    screen.bgcolor("skyblue")  # A light sky blue background for contrast
    
    # Create and configure the turtle
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)               # Point the turtle upward
    t.penup()
    t.setposition(0, -250)   # Start near the bottom of the screen
    t.pendown()
    
    # Draw the tree: starting with a branch length of 100 and thickness 10
    draw_tree(t, branch_length=100, thickness=10)
    
    # Wait for a click on the window to exit
    screen.exitonclick()

if __name__ == '__main__':
    main()
