# List2d
# author: Ondrej Sika, http://ondrejsika.com

def list2d(x, y, default=None):
    return [[default for xxx in range(x)] for xxx in range(y)]

def reverse(data):
    rev = list2d(len(data), len(data[0]))
    for y in range(len(data)):
        for x in range(len(data[0])):
            rev[x][y] = data[y][x]
    return rev

class List2d:
    def __init__(self, *args):
        if len(args) == 1:
            self.load(*args)
        else:
            self.create(*args)

    def load(self, data):
        self.data = data

    def create(self, x, y, default=None):
        self.data = list2d(x, y, default)
    
    def list(self):
        return self.data

    def row(self, n):
        return self.data[n]

    def rows(self):
        return self.data

    def col(self, n):
        return [x[n] for x in self.data]

    def cols(self):
        return reverse(self.data)

    def get(self, x, y):
        return self.data[x][y]

    def set(self, x, y, val):
        self.data[x][y] = val

    def reverse(self):
        self.data = reverse(data)

    def duplicate(self):
        return List2d(self.data)

    def __unicode__(self):
        return u"<List2d %s>"%list(self.data)

    def __repr__(self):
        return self.__unicode__()

    def __str__(self):
        return self.__unicode__()