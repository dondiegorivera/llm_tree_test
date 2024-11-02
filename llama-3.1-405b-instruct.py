#llama-3.1-405b-instruct
import turtle

def draw_branch(turt, branch_length, angle, depth):
    if depth == 0:
        return
    turt.forward(branch_length)
    turt.left(angle)
    draw_branch(turt, branch_length * 0.7, angle, depth - 1)
    turt.right(angle * 2)
    draw_branch(turt, branch_length * 0.7, angle, depth - 1)
    turt.left(angle)
    turt.backward(branch_length)

def main():
    window = turtle.Screen()
    window.setup(800, 600)
    turt = turtle.Turtle()
    turt.speed(0)
    turt.left(90)
    draw_branch(turt, 100, 30, 10)
    window.exitonclick()

if __name__ == "__main__":
    main()
