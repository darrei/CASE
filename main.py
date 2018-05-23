'''
Case #6
Developers: Rodionova D(50%), Nazimova S(50%), Kozlovsky A(50%)
'''
from tkinter import *

from train import *

root = Tk()
root.title('Метрополитен симуляция кольцевая линия')
c = Canvas(root, width=800, height=800, bg='white')

r1 = 249
r11 = 253
r2 = 246
coord_list = []
c.create_oval(148, 148, 652, 652, outline="red")  # 1
c.create_oval(154, 154, 646, 646, outline="red")  # 2


def stations(ugol):
    ugol = -radians(ugol)
    y = int(400 - (r1 * cos(ugol)))
    x = int(400 - r1 * sin(ugol))
    c.create_oval(x - 4, y - 4, x + 4, y + 4, outline="darkblue", fill='darkblue')
    if ugol == 0:
        c.create_text((x - 69, y), text="Проспект мира: ", fill='darkblue')
    if ugol == -(36 * pi) / 180:
        c.create_text((x - 69, y), text="Комсомольская: ", fill='darkblue')
    coord_list.append((x, y))


def chp(p=False):  # нажата ли кнопка стоп
    global stop1
    stop1 = p


'''def trains():

    file = open('metro.txt', 'r')
    lst = file.readlines()
    file.close()
    trains_list = []
    for i in lst:
        train = i.split()
        if len(train) == 6:
            train[1] = train[1] + ' ' + train[2]
            train.pop(2)
        trains_list.append(Train(train, root, c))'''

'''def diction():
    dictionary = {'Проспект Мира' : 0,
                  'Комсомольская' : 3,
                  'Курская' : 6,
                  'Таганская' : 8,
                  'Павелецкая'  : 11,
                  'Добрынинская' : 13,
                  'Октябрьская' : 14,
                  'Парк культуры' : 17,
                  'Киевская' : 20,
                  'Краснопресненская' : 22,
                  'Белорусская' : 25,
                  'Новослободская' : 27}
    return dictionary'''


def rand():
    real_stop_time = randrange(20, 120, 10)
    stop_time = real_stop_time / 30
    stop_time *= 100
    return int(stop_time)


# c.bind("z", callback)
# u.pack(side=TOP)
# c.pack(side=TOP)

file = open('metro.txt', 'r')
lst = file.readlines()
file.close()
trains_list = []
for i in lst:
    train = i.split()
    if len(train) == 6:
        train[1] = train[1] + ' ' + train[2]
        train.pop(2)
    trains_list.append(Train(train, root, c))


def stations(ugol):
    ugol = -radians(ugol)
    y = int(400 - (r1 * cos(ugol)))
    x = int(400 - r1 * sin(ugol))
    c.create_oval(x - 4, y - 4, x + 4, y + 4, outline="darkblue", fill='darkblue')
    if ugol == 0:
        c.create_text((x - 69, y), text="Проспект мира: ", fill='darkblue')
    if ugol == -(36 * pi) / 180:
        c.create_text((x - 69, y), text="Комсомольская: ", fill='darkblue')
    coord_list.append((x, y))


def start():
    while 1:
        for i in trains_list:
            i.move()


def stopp():
    c.delete("all")


stations(0)
stations(36)
stations(72)
stations(96)
stations(112)
stations(156)
stations(168)
stations(204)
stations(240)
stations(264)
stations(300)
stations(324)

u = Frame(root)

u.pack(side=TOP)

c.grid()
c.focus_set()
c.pack(side=TOP)
b_pusk = Button(u, text='ПУСК', width=10, command=lambda: start())
b_pusk.grid(row=1, column=1)

b_stop = Button(u, text='СТОП', width=10, command=lambda: stopp())  # кнопка стоп

b_stop.grid(row=1, column=2)

c.bind('z', start)

root.mainloop()
