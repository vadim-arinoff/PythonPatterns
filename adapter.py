import math
class Hole(object):
    def __init__(self, r):
        # радиус дыры
        self.r = r

    def put(self, obj):
        # проверка сходимости по r
        try:
            if self.r >= obj.r:
                print('Залезло')
            else:
                print('Не лезет')
        except AttributeError:
            print('Объект не умеет вычислять радиус дырки, в которую он лезет.')

class Square(object):
    def __init__(self, x, h):
        # параметры квадрата
        self.x = x
        self.h = h

class SquareHoleAdapter(object):
    def __init__(self, sq_obj):
        self.sq_obj = sq_obj

    @property
    def r(self):
            # половина диагонали квадрата будет равна радиусу круга
        return math.sqrt(2*(self.sq_obj.x**2))/2

h1 = Hole(5)
h2 = Hole(2)
s1 = Square(5, 7)
s2 = Square(3, 3)
sa = SquareHoleAdapter(s2)

h1.put(s1)
h1.put(sa)
h2.put(sa)
