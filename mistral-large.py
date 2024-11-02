#mistral-large
import turtle

def draw_tree(t, branch_len):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(t, branch_len - 15)
        t.left(40)
        draw_tree(t, branch_len - 15)
        t.right(20)
        t.backward(branch_len)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.color("brown")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    draw_tree(t, 75)
    screen.mainloop()

if __name__ == "__main__":
    main()
