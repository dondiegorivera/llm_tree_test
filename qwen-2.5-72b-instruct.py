#qwen/qwen-2.5-72b-instruct
import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")
    draw_tree(75, my_turtle)
    my_win.exitonclick()

if __name__ == "__main__":
    main()
