"""Case-study
Developers:   Ignatovich D. (60%),
              Miller A. (45%),
              Poylova E. (40%)
"""
import turtle as t

t.speed(1000)
t.up()
t.goto(0, -100)
t.down()

# Рисунок_1 Параметры подогнать
def square(a):
    if a < 10:
        return
    t.down()
    for _ in range(4):
        t.forward(a)
        t.right(90)
    t.up()
    t.right(15)
    t.forward(a / 8)

    return (square(a * 0.9))


def square_main():
    side = float(input('Введите длину стороны квадрата: '))
    square(side)


# Фрактал Ветка Рисунок 3
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
    n = int(input('Введите глубиину рекурсии: '))
    size = int(input('Введите длину строны: '))
    branch(n, size)


# Кривая Коха Рисунок 4
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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)


# Снежинка Коха Рисунок 5
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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    for _ in range(3):
        koch_snowflake(n, a)
        t.right(120)
 
# Двоичное дерево
t.penup()
t.setposition(0, -300)
t.left(90)
t.pendown()
def tree(n, size):
    if size == 0:
        return
    else:
        t.forward(n)
        t.left(30)
        tree((n * 0.6), size - 1)
        t.right(60)
        tree((n * 0.6), size - 1)
        t.left(30)
        t.back(n)
tree(200, 5) #пример вывода
t.done()

#Фрактал Дракон Хартера-Хейтуэя Рисунок 9
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
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    dragon_left(n, a)
    
    
#Main
print('Выбирете рисунок:', '1)Квадрат', '2)Двоичное дерево', '3)Фрактал "Ветка"', '4)Кривая Коха', '5)Снежинка Коха', '6)Кривая Минковского', '7)"Ледяные" фракталы', '8)Кривая Леви', '9)Фрактал Дракон Хартера-Хейтуэя', sep='\n')
picture = int(input())
if picture == 1:
    square_main()
elif picture == 2:
    square_main()
elif picture == 3:
    branch_main()
elif picture == 4:
    koch_main()
elif picture == 5:
    koch_snowflake_main()
elif picture == 6:
    square_main()
elif picture == 7:
    square_main()
elif picture == 8:
    square_main()
elif picture == 9:
    square_main()
