#anthropic/claude-3.5-sonnet
import turtle
import random

def draw_tree(t, branch_len, angle, min_length=5):
    """
    Recursively draws a tree using turtle graphics
    
    Args:
        t: turtle object
        branch_len: length of the current branch
        angle: base angle for branching
        min_length: minimum branch length to stop recursion
    """
    # Save the current state
    t.width(max(1, branch_len/10))  # Branch thickness proportional to length
    
    # Draw the branch
    t.forward(branch_len)
    
    # Only create sub-branches if branch is long enough
    if branch_len > min_length:
        # Right sub-branch
        t.right(angle + random.randint(-15, 15))
        # Save position and heading
        pos = t.position()
        heading = t.heading()
        
        # Recursively draw right sub-branch
        draw_tree(t, branch_len * random.uniform(0.6, 0.8), angle * 0.9)
        
        # Return to saved position and heading
        t.penup()
        t.setposition(pos)
        t.setheading(heading)
        t.pendown()
        
        # Left sub-branch
        t.left(angle + random.randint(-15, 15))
        draw_tree(t, branch_len * random.uniform(0.6, 0.8), angle * 0.9)
        
        # Return to start of current branch
        t.penup()
        t.setposition(pos)
        t.setheading(heading)
        t.pendown()

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Recursive Tree")
    
    # Create and configure the turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.color("brown")
    t.left(90)  # Point turtle upward
    t.penup()
    t.setposition(0, -200)  # Start at bottom of screen
    t.pendown()
    
    # Draw the tree
    draw_tree(t, 100, 30)
    
    # Hide the turtle and display the result
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
