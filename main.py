"""Case-study 
Developers:   Ignatovich D. (60%),
              Miller A. (30%),
              Poylova E. (40%)
"""
import turtle as t
t.speed(1000)

#Рисунок_1 Параметры подогнать
def square(a):
    if a<10:
        return
    t.down()
    for _ in range(4):
        t.forward(a)
        t.right(90)
    t.up()
    t.right(15)
    t.forward(a / 8)

    return (square(a*0.9))

def square_main():
    side = float(input('Введите длину стороны квадрата: '))
    square(side)

#Фрактал Ветка Рисунок 3    
def branch(n, size):
    if n == 0:
        t.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(size)

def branch_main():
    t.up()
    t.goto(0,-100)
    t.left(90)
    t.down()
    n = int(input('Введите глубиину рекурсии: '))
    size = int(input('Введите длину строны: '))
    branch(n,size)
    
#Кривая Коха Рисунок 4
def koch(order, size):
    if order == 0:
        t.forward(size)
    else:
        koch(order-1, size/3)
        t.left(60)
        koch(order-1, size/3)
        t.right(120)
        koch(order-1, size/3)
        t.left(60)
        koch(order-1, size/3)

def koch_main():
    t.up()
    t.goto(-100,0)
    t.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)

#Снежинка Коха Рисунок 5
def koch_snowflake(order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_snowflake(order-1, size/3)
        t.left(60)
        koch_snowflake(order-1, size/3)
        t.right(120)
        koch_snowflake(order-1, size/3)
        t.left(60)
        koch_snowflake(order-1, size/3)

def koch_snowflake_main():
    t.up()
    t.goto(-100,0)
    t.down()
    t.speed(1000)
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    for _ in range(3):
        koch_snowflake(n, a)
        t.right(120)
