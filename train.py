from math import *
from random import randrange


def rand():
    real_stop_time = randrange(20, 120, 10)
    stop_time = real_stop_time / 30
    stop_time *= 100
    return int(stop_time)


class Train():
    def __init__(self, train, root, canvas, stop=0):
        self.root = root
        self.stop = stop
        self.c = canvas
        self.coord_list = [(400, 151), (546, 198), (636, 323), (647, 426), (630, 493), (501, 627), (451, 643),
                           (298, 627), (184, 524), (152, 426), (184, 275), (253, 198)]
        self.du = 10
        self.number = train[0]
        self.start = str(train[1])
        self.direction = train[2]
        self.avspeed = train[3]
        self.carrige = train[4]
        self.ball = self.c.create_oval(0, 0, 4, 4, outline="black", fill='black')
        if int(self.carrige) == 2:
            self.ball2 = self.c.create_oval(0, 0, 4, 4, outline="black", fill='black')

        self.r11 = 245
        self.r2 = 252
        self.x = 400
        self.y = 159
        self.dictionary = {'Проспект Мира': 0,
                           'Комсомольская': 3,
                           'Курская': 6,
                           'Таганская': 8,
                           'Павелецкая': 11,
                           'Добрынинская': 13,
                           'Октябрьская': 14,
                           'Парк культуры': 17,
                           'Киевская': 20,
                           'Краснопресненская': 22,
                           'Белорусская': 25,
                           'Новослободская': 27}
        self.list_values = [0, 36, 72, 96, 112, 156, 168, 204, 240, 264, 300, 324]

        self.ugol = int(int(self.dictionary[self.start]) * 12)

    def __str__(self):

        s = str(self.ugol)

        return s

    def move(self):
        if self.stop == 0:

            if self.direction == '1':
                self.ugol_rad = -radians(self.ugol)
                self.y = 400 - (self.r11 * cos(self.ugol_rad))
                self.x = 400 - self.r11 * sin(self.ugol_rad)
                if int(self.carrige) == 1:
                    self.c.coords(self.ball, self.x + 2, self.y + 2, self.x - 2, self.y - 2)
                if int(self.carrige) == 2:
                    self.c.coords(self.ball2, self.x + 2, self.y + 2, self.x - 2, self.y - 2)
                    self.ball2, self.ball = self.ball, self.ball2

                self.root.update()
                for i in self.list_values:
                    if int(self.ugol) == i:
                        self.stop = int(rand())
                        self.ugol = self.ugol + 1
                        self.root.update()

                self.ugol += (int(self.avspeed) * 0.03)

            if self.direction == '0':

                self.ugol_rad = radians(self.ugol)
                self.y = 400 - (self.r2 * cos(self.ugol_rad))
                self.x = 400 - self.r2 * sin(self.ugol_rad)
                self.c.coords(self.ball, self.x + 2, self.y + 2, self.x - 2, self.y - 2)
                self.root.update()
                for i in self.list_values:
                    if int(self.ugol) == i:
                        self.stop = int(rand())
                        self.ugol += 1
                        self.root.update()
                self.ugol += (int(self.avspeed) * 0.03)



        else:
            self.stop = self.stop - 1
