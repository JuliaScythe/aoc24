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

    def rotate(self, amount):
        variants = [d for d in Direction]
        idx = variants.index(self)
        return variants[(idx + (amount // 45)) % len(variants)] 

class Grid:
    def __init__(self, backer, default=' '):
        self.backer = list(map(lambda x: x.strip(), backer))
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
        self.push()
        self.move(*dir.value)
        val = self.get()
        self.pop()
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
        self.push()
        words = {}
        for dir in Direction:
            self.pop()
            self.push()
            word = [self.at()]
            for i in range(length-1):
                self.move(*dir.value)
                word.append(self.at())
            words[dir] = word
        self.pop()
        return words
    
    def for_each(self, f):
        self.push()
        for iY, row in enumerate(self.backer):
            for iX, col in enumerate(row):
                self.x = iX
                self.y = iY
                f(self)
        self.pop()
    
    def find(self, target):
        for y, row in enumerate(self.backer):
            for x, cell in enumerate(row):
                if cell == target:
                    return x,y
        return None, None
    
    def find_all(self, target):
        for y, row in enumerate(self.backer):
            for x, cell in enumerate(row):
                if cell == target:
                    yield x,y
        return

    def inbounds(self, x=None, y=None):
        if x is None:
            x = self.x
        if y is None:
            y = self.y
        return 0 <= x < len(self.backer[0]) and (0 <= y < len(self.backer))
    
    def __repr__(self):
        repr_str = f"Grid: {len(self.backer[0])} x {len(self.backer)}, Default: '{self.default}'\n"
        for row in self.backer:
            repr_str += str(row) + "\n"
        repr_str += f"Tags: {self.tags}"

        return repr_str
