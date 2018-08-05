
class dynamic(object):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.dynamic = True
        self.yVelocity = 0
        self.contact = True

class static(object):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.dynamic = False

class player(dynamic):

    def __init__(self, dimensions):
        dynamic.__init__(self, dimensions)
        self.id = 'player'
        self.shrunk = True
        self.xVelocity = 0
        self.defaultPosition = [330,300]

    def changeSize(self, size):
        self.dimensions = [self.dimensions[0], self.dimensions[1] + self.dimensions[3] - size[1]] + size

    def jump(self):
        self.yVelocity -= 1000

class enemy(dynamic):

    def __init__(self,dimensions,velocity):
        dynamic.__init__(self,dimensions)
        self.xVelocity = velocity

class goomba(enemy):

    def __init__(self, position, velocity):
        self.id = 'goomba'
        enemy.__init__(self,position + [40,40],velocity)

class koopa(enemy):

    def __init__(self, position, velocity):
        self.id = 'koopa'
        enemy.__init__(self, position + [40,60], velocity)

class border(static):

    def __init__(self, dimensions):
        static.__init__(self, dimensions)
        self.id = 'border'

class block(static):

    def __init__(self, position):
        static.__init__(self, position + [40,40])
        self.id = 'block'
