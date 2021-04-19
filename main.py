"""Case-study
Developers:   Ignatovich D. (60%),
              Miller A. (45%),
              Poylova E. (50%)
"""
import turtle as t

t.speed(1000)
t.up()
t.goto(0, -100)
t.down()

# Square picture 1
def square(a):
    if a < 10:
        return
    t.down()
    for _ in range(4):
        t.forward(a)
        t.right(90)
    t.up()
    t.right(12)
    t.forward(a / 7.5)

    return (square(a * 0.89))


def square_main():
    side = float(input('Enter the length of the side of the square: '))
    square(side)

    
# Binary tree picture 2

def tree(size, n):
    if n == 0:
        return
    else:
        t.forward(size)
        t.left(30)
        tree((size * 0.6), n - 1)
        t.right(60)
        tree((size * 0.6), n - 1)
        t.left(30)
        t.back(size)
        
        
def tree_main():
    t.left(90)
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    tree(size, n)


# Fractal Branch picture 3
def branch(n, size):
    if n == 0:
        t.left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)


def branch_main():
    t.left(90)
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    branch(n, size)


# Koch Curve picture 4
def koch(order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)
        t.right(120)
        koch(order - 1, size / 3)
        t.left(60)
        koch(order - 1, size / 3)


def koch_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    koch(n, size)


# Koch's Snowflake picture 5
def koch_snowflake(order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_snowflake(order - 1, size / 3)
        t.left(60)
        koch_snowflake(order - 1, size / 3)
        t.right(120)
        koch_snowflake(order - 1, size / 3)
        t.left(60)
        koch_snowflake(order - 1, size / 3)


def koch_snowflake_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    for _ in range(3):
        koch_snowflake(n, size)
        t.right(120)

# Minkowski Curve picture 6

def curve_minkowski(size, n):
    if n == 0:
        t.forward(size * 3)
    else:
        curve_minkowski(size / 3, n - 1)
        t.left(90)
        curve_minkowski(size / 3, n - 1)
        t.right(90)
        curve_minkowski(size / 3, n - 1)
        t.right(90)
        curve_minkowski(size / 3, n - 1)
        curve_minkowski(size / 3, n - 1)
        t.left(90)
        curve_minkowski(size / 3, n - 1)
        t.left(90)
        curve_minkowski(size / 3, n - 1)
        t.right(90)
        curve_minkowski(size / 3, n - 1)
        
        
def main_curve_minkowski():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    curve_minkowski(size, n)

   
# Levy Curve picture 8
def levy_curve(size, n):
    if n == 0:
        turtle.forward(size * 4)
        return
    turtle.left(45)
    levy_curve(size / 3, n - 1)
    turtle.right(90)
    levy_curve(size / 3, n - 1)
    turtle.left(45)
    
    
def main_levy_curve():
    n = int(input('Глубина рекурсии:'))
    size = int(input('Длина стороны:'))
    tree(size, n)

# The Harter-Haythaway Dragon Fractal picture 9
def dragon_left(order, size):
    if order == 0:
        t.forward(size)
    else:
        t.left(45)
        dragon_left(order - 1, size*(2**0.5)/2)
        t.right(90)
        dragon_right(order - 1, size*(2**0.5)/2)
        t.left(45)

def dragon_right(order, size):
    if order == 0:
        t.forward(size)
    else:
        t.right(45)
        dragon_left(order - 1, size*(2**0.5)/2)
        t.left(90)
        dragon_right(order - 1, size*(2**0.5)/2)
        t.right(45)


def dragon_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    dragon_left(n, size)
 
# Ice fractal picture 1
def ice(n, a):
    if n == 0:
        t.forward(a)
    else:
        ice(n - 1, a / 2)
        t.left(90)
        ice(n - 1, a / 4)
        t.right(180)
        ice(n - 1, a / 4)
        t.left(90)
        ice(n - 1, a / 2)


def ice_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    ice(n, size)

# Ice fractal picture 2
def snow(n, a):
    if n == 0:
        t.forward(a)
    else:
        snow(n - 1, a / 2)
        t.left(120)
        snow(n - 1, a / 4)
        t.right(180)
        snow(n - 1, a / 4)
        t.left(120)
        snow(n - 1, a / 4)
        t.right(180)
        snow(n - 1, a / 4)
        t.left(120)
        snow(n - 1, a / 2)


def snow_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    snow(n, size)


# Ice fractal picture 3
def ice_snowflake(n, a):
    if n == 0:
        t.forward(a)
    else:
        ice_snowflake(n - 1, a / 2)
        t.left(90)
        ice_snowflake(n - 1, a / 4)
        t.right(180)
        ice_snowflake(n - 1, a / 4)
        t.left(90)
        ice_snowflake(n - 1, a / 2)


def ice_snowflake_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    for _ in range(3):
        ice_snowflake(n, size)
        t.right(120)
    t.right(60)
    for _ in range(3):
        ice_snowflake(n, size)
        t.left(120)


# Ice fractal picture 4
def flake_of_snow(n, a):
    if n == 0:
        t.forward(a)
    else:
        flake_of_snow(n - 1, a / 2)
        t.left(120)
        flake_of_snow(n - 1, a / 4)
        t.right(180)
        flake_of_snow(n - 1, a / 4)
        t.left(120)
        flake_of_snow(n - 1, a / 4)
        t.right(180)
        flake_of_snow(n - 1, a / 4)
        t.left(120)
        flake_of_snow(n - 1, a / 2)


def flake_of_snow_main():
    n = int(input('Recursion depth: '))
    size = int(input('Side length: '))
    for _ in range(3):
        flake_of_snow(n, size)
        t.right(120)
    t.right(60)
    for _ in range(3):
        flake_of_snow(n, size)
        t.left(120)

    
#Main
print('Choose a drawing:', '1)Square', '2)Binary tree', '3)"Branch" Fractal', '4)Koch Curve', "5)Koch's Snowflake",
      '6)Minkowski Curve', '7)Ice fractals', '8)Levy Curve', "9)Harter-Haythaway's Dragon Fractal", sep='\n')
picture = int(input())
if picture == 1:
    square_main()
elif picture == 2:
    tree_main()
elif picture == 3:
    branch_main()
elif picture == 4:
    koch_main()
elif picture == 5:
    koch_snowflake_main()
elif picture == 6:
    main_curve_minkowski()
elif picture == 7:
    x = int(input('Choose an ice fractal pattern from 1 to 4: '))
    if x == 1:
        ice_main()
    elif x == 2:
        snow_main()
    elif x == 3:
        ice_snowflake_main()
    elif x == 4:
        flake_of_snow_main()
elif picture == 8:
    main_levy_curve()
elif picture == 9:
    dragon_main()


    
t.hideturtle()
t.done()
