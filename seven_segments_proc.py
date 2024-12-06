import turtle


class number:
    def __init__(self, my_turtle, color):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        my_turtle.color(color)
        my_turtle.penup()
        my_turtle.setheading(0)
        my_turtle.goto(0, 0)
        my_turtle.pensize(10)

        self.color = color

    def draw(self, my_turtle, digit):
        if digit == 0:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 1:
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 2:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 3:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 4:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.penup()

        if digit == 5:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 6:
            draw(my_turtle, 5)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

        if digit == 7:
            my_turtle.goto(-50, 100)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.forward(-100)
            draw(my_turtle, 1)

        if digit == 8:
            draw(my_turtle, 0)
            my_turtle.goto(-50, 0)
            my_turtle.pendown()
            my_turtle.forward(100)
            my_turtle.penup()

        if digit == 9:
            draw(my_turtle, 5)
            my_turtle.goto(50, 100)
            my_turtle.pendown()
            my_turtle.right(90)
            my_turtle.forward(100)
            my_turtle.left(90)
            my_turtle.penup()

    def clear(my_turtle):
        my_turtle.clear()

    def my_delay(dt):
        import time
        start = time.time()
        while time.time() - start < dt:
            pass


class i_give_up(number):
    Tom = turtle.Turtle()
    tom_color = (255, 0, 0)

    def __init__(self, Tom, tom_color):
        pass

turtle.done()