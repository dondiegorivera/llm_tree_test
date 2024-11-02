#qwen/qwen-2-72b-instruct
import turtle
import random

def draw_tree(branch_length, t):
    if branch_length > 5:
        if branch_length < 30:
            t.color('brown')
        else:
            t.color('green')

        t.pensize(branch_length / 10)
        t.forward(branch_length)
        t.right(20 + random.randint(-10, 10))
        draw_tree(branch_length - 15, t)
        t.left(40 + random.randint(-10, 10))
        draw_tree(branch_length - 15, t)
        t.right(20 + random.randint(-10, 10))
        t.backward(branch_length)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.screensize(800, 800)  # Increase screensize to accommodate larger tree
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pensize(5)
    draw_tree(100, t)
    myWin.exitonclick()

main()
