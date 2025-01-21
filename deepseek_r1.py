import turtle
import random

def draw_branch(t, branch_length, angle, width):
    if branch_length < 5:
        return
        
    # Draw current branch
    t.pensize(width)
    t.forward(branch_length)
    
    # Randomize parameters for realism
    angle_variation = random.randint(-10, 10)
    length_reduction = random.uniform(0.6, 0.8)
    
    # Right branch
    t.right(angle + angle_variation)
    draw_branch(t, branch_length * length_reduction, angle, width*0.7)
    t.left(angle + angle_variation)
    
    # Left branch
    t.left(angle - angle_variation)
    draw_branch(t, branch_length * length_reduction, angle, width*0.7)
    t.right(angle - angle_variation)
    
    # Return to original position
    t.backward(branch_length)

# Set up turtle
t = turtle.Turtle()
t.speed('fastest')
t.left(90)
t.penup()
t.setpos(0, -250)
t.pendown()
t.color("saddlebrown")

# Draw the tree
draw_branch(t, 150, 30, 12)

# Add leaves at the ends
t.color("forestgreen")
for _ in range(30):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(0, 300))
    t.pendown()
    t.dot(random.randint(5, 15))

t.hideturtle()
turtle.done()
