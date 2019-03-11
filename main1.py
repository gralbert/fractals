"""
Draw fractals.
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import turtle as trt


def flower(d, n):
    """ Draw a flower. """
    # TODO
    if n == 0:
        return
    trt.forward(100)
    trt.right(45)
    trt.forward(50)
    trt.right(180)
    trt.forward(50)
    trt.right(90)
    trt.forward(50)
    trt.left(180)
    trt.forward(50)
    trt.right(45)
    trt.forward(100)
    trt.left(180)
    trt.left(45)
    tree(d, n-1)


def tree(d, n):
    """ Draw a binary tree. """
    # TODO
    if n == 0:
        return
    trt.forward(100)
    trt.right(45)
    trt.forward(50)
    trt.right(180)
    trt.forward(50)
    trt.right(90)
    trt.forward(50)
    trt.left(180)
    trt.forward(50)
    trt.right(45)
    trt.forward(100)
    trt.left(180)
    trt.left(45)
    tree(d, n-1)


def sq(d, n):
    """ Draw the squares. """
    if n == 0:
        return
    trt.up()
    trt.right(20)
    trt.forward(d//4)
    trt.down()
    for _ in range(4):
        trt.forward(d)
        trt.right(90)
    return sq(d*0.9, n-1)


def branch(n, size):
    """ Draw a fir branch. """
    if n == 0:
        trt.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        trt.forward(x)
        trt.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        trt.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        trt.right(135)

    trt.forward(x)
    trt.left(180)
    trt.forward(size)


def koch(order, size):
    """ The algorithm of Koch. """
    if order == 0:
        trt.forward(size)
    else:
        koch(order-1, size/3)
        trt.left(60)
        koch(order-1, size/3)
        trt.right(120)
        koch(order-1, size/3)
        trt.left(60)
        koch(order-1, size/3)


def snowflake(order, size):
    """ Draw snowflake by the algorithm of Koch. """
    if order == 0:
        koch(order,size)

        trt.right(120)
        koch(order, size)

        trt.right(120)
        koch(order, size)
    else:
        koch(order, size)

        trt.right(120)
        koch(order, size)

        trt.right(120)
        koch(order, size)


def main():
    trt.speed(0)

    screen = trt.getscreen()
    answer = screen.textinput("Welcome!", "Choose fractal (1, 2 ... or 5).")

    if answer is None or answer.lower().startswith('1'):
        sq(100, 20)
        trt.done()
    elif answer.lower().startswith('2'):
        trt.up()
        trt.goto(-300, 0)
        trt.down()
        koch(5, 5000)
        trt.done()
    elif answer.lower().startswith('3'):
        trt.up()
        trt.goto(-100, 0)
        trt.down()
        snowflake(3, 100)
        trt.done()
    elif answer.lower().startswith('3'):
        trt.up()
        trt.goto(0, -100)
        trt.left(90)
        trt.down()
        branch(2, 400)
        trt.done()
    elif answer.lower().startswith('4'):
        trt.up()
        trt.goto(0, -100)
        trt.down()
        trt.left(90)
        tree(10, 8)
        trt.done()
    elif answer.lower().startswith('5'):
        trt.up()
        trt.goto(0, -100)
        trt.down()
        trt.left(90)
        flower(10, 8)
        trt.done()


if __name__ == '__main__':
    main()

