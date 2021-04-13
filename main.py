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


#Кривая Коха 
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

