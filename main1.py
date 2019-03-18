"""
Draw fractals.
Grigorev A., Batenev P., Zhambaeva D.
"""

import rulocal as ru
import turtle as trt


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


def tree(size, n):
    """ Turn turtle for drawing tree. """
    trt.left(90)
    help_tree(n, size)


def help_tree(n, size):
    """ Drawing binary tree. """
    if n == 0:
        trt.forward(size)
    else:
        trt.forward(size)
        trt.right(30)
        help_tree(n - 1, size/2)
        trt.right(180)
        help_tree(n - 1, size/2)
        trt.right(120)
        help_tree(n - 1, size/2)
        trt.right(180)
        help_tree(n - 1, size/2)
        trt.right(30)
        trt.forward(size)


def branch(n, size):
    """ Draw a fir branch. """
    if n == 0:
        trt.left(180)
        return

    x = size/(n+1)
    for i in range(int(n)):
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


def mink(order, size):
    """ Minkowski curve. """
    if order == 0:
        trt.forward(size)
    else:
        mink(order-1, size/3)
        trt.left(90)
        mink(order-1, size/3)
        trt.right(90)
        mink(order-1, size/3)
        trt.right(90)
        mink(order-1, size/3)
        mink(order - 1, size / 3)
        trt.left(90)
        mink(order - 1, size / 3)
        trt.left(90)
        mink(order - 1, size / 3)
        trt.right(90)
        mink(order - 1, size / 3)


def ice_fractal(d, n):
    """ Drawing ice fractal №1. """
    if n == 0:
        trt.forward(d)
    else:
        ice_fractal(d/2, n-1)
        trt.left(90)
        ice_fractal(d/4, n-1)
        trt.right(180)
        ice_fractal(d/4, n-1)
        trt.left(90)
        ice_fractal(d/2, n-1)


def ice_2fractal(d, n):
    """ Drawing ice fractal №2. """
    if n == 0:
        trt.forward(d)
    else:
        ice_2fractal(d/2, n-1)
        trt.left(120)
        ice_2fractal(d/4, n-1)
        trt.left(180)
        ice_2fractal(d/4, n-1)
        trt.left(120)
        ice_2fractal(d/4, n-1)
        trt.left(180)
        ice_2fractal(d/4, n-1)
        trt.left(120)
        ice_2fractal(d/2, n-1)


def ice_snowflake(d, n):
    """ Drawing ice snowflake. """
    ice_fractal(d, n-1)
    trt.right(120)
    ice_fractal(d, n-1)
    trt.right(120)
    ice_fractal(d, n-1)
    trt.left(180)
    ice_fractal(d, n-1)
    trt.left(120)
    ice_fractal(d, n-1)
    trt.left(120)
    ice_fractal(d, n-1)


def lev(n, size):
    """ Drawing Levi curve. """
    if n == 0:
        trt.forward(size)
    else:
        trt.left(45)
        lev(n-1, size)
        trt.right(90)
        lev(n-1, size)
        trt.left(45)


def dragon(n, size,k):
    """ Draw dragon. """
    if n == 0:
        trt.forward(size)
    else:
        if k == 1:
            trt.left(45)
        else:
            trt.right(45)
        dragon(n - 1, size / 2 ** 0.5,1)
        if k == 1:
            trt.right(90)
        else:
            trt.left(90)
        dragon(n - 1, size / 2 ** 0.5,-1)
        if k == 1:
            trt.left(45)
        else:
            trt.right(45)


def place(num):
    """ Put the turtle in the right place. """
    if num in {'3', '1'}:
        trt.up()
        trt.goto(0, -100)
        trt.down()
        trt.left(90)
    elif num == '2':
        trt.right(0)
    elif num == '4':
        trt.up()
        trt.goto(-300, 0)
        trt.down()
    elif num == '5':
        trt.up()
        trt.goto(-100, 0)
        trt.down()
    elif num == '6':
        trt.up()
        trt.backward(200)
        trt.down()
    elif num in {'7','8', '9'}:
        trt.up()
        trt.goto(-200, 0)
        trt.down()


def get_data(_size, _depth):
    """ Get data for drawing. """
    screen2 = trt.getscreen()
    size = screen2.numinput(ru.DATA, ru.SIZE, _size, minval=10, maxval=10000)
    depth = screen2.numinput(ru.DATA, ru.DEPTH, _depth, minval=0, maxval=1000)

    return {'size': size, 'depth': depth}


def main():
    """ Main function. """
    trt.hideturtle()
    trt.tracer(0)

    screen = trt.getscreen()
    answer = screen.textinput('Welcome!', ru.WELCOME)

    if answer == '1':
        data = get_data(100, 20)
        place('1')
        sq(data['size'], data['depth'])

    elif answer == '2':
        data = get_data(100, 4)
        place('2')
        tree(data['size'], data['depth'])

    elif answer == '3':
        data = get_data(400, 3)
        place('3')
        branch(data['depth'], data['size'])

    elif answer == '4':
        data = get_data(500, 3)
        place('4')
        koch(data['depth'], data['size'])

    elif answer == '5':
        data = get_data(100, 3)
        place('5')
        snowflake(data['depth'], data['size'])

    elif answer == '6':
        data = get_data(200, 3)
        place('6')
        mink(data['depth'], data['size'])

    elif answer == '7':
        data = get_data(50, 3)
        place('7')
        ice_fractal(data['size']*10, data['depth'])

    elif answer == '8':
        data = get_data(50, 3)
        place('7')
        ice_2fractal(data['size']*10, data['depth'])

    elif answer == '9':
        data = get_data(150, 3)
        place('7')
        ice_snowflake(data['size'], data['depth'])

    elif answer == '10':
        data = get_data(20, 7)
        place('6')
        lev(data['depth'], data['size'])

    elif answer == '11':
        data = get_data(200, 12)
        place('6')
        dragon(data['depth'], data['size'],1)

    trt.update()
    trt.mainloop()

if __name__ == '__main__':
    main()

