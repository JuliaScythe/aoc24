from enum import Enum

class Direction(Enum):
    NORTH = (0, -1)
    NORTHEAST = (1, -1)
    EAST = (1, 0)
    SOUTHEAST = (1, 1)
    SOUTH = (0, 1)
    SOUTHWEST = (-1, 1)
    WEST = (-1, 0)
    NORTHWEST = (-1, -1)

class Grid:
    def __init__(self, backer, default=' '):
        self.backer = backer
        self.default = default
        self.x = 0
        self.y = 0
        self.tags = {}
        self.stack = []
    
    def get(self, x, y):
        if 0 <= x < len(self.backer[0]) and (0 <= y < len(self.backer)):
            return self.backer[y][x]
        return self.default
    
    def push(self):
        self.stack.append((self.x,self.y))

    def pop(self):
        self.x, self.y = self.stack.pop()
    
    def at(self):
        return self.get(self.x, self.y)

    def adj(self, dir):
        oX = self.x
        oY = self.y
        self.move(*dir.value)
        val = self.get()
        self.x = oX
        self.y = oY
        return val
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def tag(self, obj, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        
        if (x,y) not in self.tags:
            self.tags[(x,y)] = [obj]
        else:
            self.tags[(x,y)].append(obj)
    
    def get_cardinal_words(self, length=1):
        oX = self.x
        oY = self.y
        words = {}
        for dir in Direction:
            self.x = oX
            self.y = oY
            word = [self.at()]
            for i in range(length-1):
                self.move(*dir.value)
                word.append(self.at())
            words[dir] = word
        self.x = oX
        self.y = oY
        return words
    
    def for_each(self, f):
        for iX, row in enumerate(self.backer):
            for iY, col in enumerate(row):
                self.x = iX
                self.y = iY
                f(self)