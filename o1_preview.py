#openai/o1-preview
import turtle
import random

def draw_tree(branch_length, t):
    if branch_length > 5:
        # Adjust pen size based on branch length
        t.pensize(branch_length / 10)
        # Random angle and length reduction for natural appearance
        angle = random.uniform(15, 45)
        length_reduction = random.uniform(0.6, 0.8)
        
        # Draw the forward branch
        t.forward(branch_length)
        # Right branch
        t.right(angle)
        draw_tree(branch_length * length_reduction, t)
        # Left branch
        t.left(2 * angle)
        draw_tree(branch_length * length_reduction, t)
        # Restore the heading and position
        t.right(angle)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("saddle brown")
    draw_tree(100, t)
    screen.exitonclick()

if __name__ == "__main__":
    main()
