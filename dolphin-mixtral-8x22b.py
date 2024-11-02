import turtle
import random

def draw_tree(t, branch_length, turtle):
    # t is turtle, branch_length is the length of the branch
    angle = random.randint(1, 30)
    my_turtle = turtle
    
    if branch_length < 3:
        return
    else:
        my_turtle.forward(branch_length)
        my_turtle.left(angle)
        draw_tree(t, branch_length - random.uniform(5, 30), my_turtle)
        my_turtle.right(angle * 2)
        draw_tree(t, branch_length - random.uniform(5, 30), my_turtle)
        my_turtle.left(angle)
        my_turtle.backward(branch_length)
        
my_turtle = turtle.Turtle()
my_window = turtle.Screen()
my_turtle.left(90)

draw_tree(my_turtle, 150, my_turtle)
my_window.mainloop()
