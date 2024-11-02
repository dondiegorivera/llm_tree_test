import turtle
import random

def draw_tree(branch_len, t):
    if branch_len > 5:
        t.pensize(branch_len / 10)  # Adjust pensize based on branch length

        # Vary colors slightly for realism
        t.color(random.choice(["#228B22", "#32CD32", "#006400"]))

        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")  # Set initial trunk color
    draw_tree(75, t)
    my_win.exitonclick()

if __name__ == "__main__":
    main()