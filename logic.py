# Class and supporting functions for the platform game

import time
import GameObjects
import copy
import geometry
import random

class PlatformGame(object):

    def __init__(self, window_dimensions, mapBorders):
        self.start_time = time.time()
        self.score = 0
        self.fail = False
        self.wd = window_dimensions
        self.target = GameObjects.player([200,200,40,40])
        self.objects =[self.target]
        self.border_width = 20
        self.mb = mapBorders
        self.CreateScreenBorders()
        self.acceleration = 800


    def move(self,axis,distance,objectIndex):

        """
        This is the method for defining a movement of the player:
        It creates a copy of the object, moves it according to instruction
        If this copy now lies inside another object the move is invalid
        axis - 0 for x axis and 1 for y axis
        distance - number of pixels the objects should be moved
        objectIndex - index of the object in the object list
        """

        clash = object
        target = self.objects[objectIndex]
        new_position = copy.copy(target.dimensions)
        new_position[axis] += distance
        overlap = False
        for item in self.objects:
            if self.objects.index(item) != objectIndex:
                if geometry.OverlappingBoxes(item.dimensions,new_position):
                    overlap = True
                    clash = item

        if overlap == False:
            target.dimensions[axis] += distance
            target.contact = False
        else:
            target.contact = True

            if axis == 1:
                target.yVelocity = 0

            c = clash.dimensions[axis]
            t = target.dimensions[axis]

            if (clash.id in ['koopa','goomba'] and target.id == 'player'):
                if (axis == 1 and c > t):
                    self.objects.remove(clash)
                    self.target.yVelocity = -1000
                else:
                    self.fail = True

            if (clash.id == 'player' and target.id in ['koopa','goomba']):
                if (axis == 1 and c < t):
                    self.objects.remove(clash)
                    self.target.yVelocity = -1000
                else:
                    self.fail = True

            if (clash.id == 'border' and target.id in ['koopa','goomba']) and (axis == 0):
                target.xVelocity = target.xVelocity * -1

            if c > t:
                target.dimensions[axis] = clash.dimensions[axis] - target.dimensions[axis + 2] - 1
            elif t > c:
                target.dimensions[axis] = clash.dimensions[axis] + clash.dimensions[axis + 2] + 1


    def fall(self,last_time):
        for item in self.objects:
            if item.dynamic == True:
                t = time.time() - last_time
                self.move(1,round(item.yVelocity * t + (1 / 2) * self.acceleration * t, 2),self.objects.index(item))
                item.yVelocity = round(self.acceleration * t + item.yVelocity, 2)

    def run(self):
        for item in self.objects:
            if item.dynamic == True:
                self.move(0,item.xVelocity,self.objects.index(item))

    def CreateScreenBorders(self):
        x = self.border_width
        tb = GameObjects.border([-(x),-(x),self.mb[0] + 2*(x), x])
        rb = GameObjects.border([self.mb[0],0,x,self.mb[1]])
        bb = GameObjects.border([-(x),self.mb[1],self.mb[0] + 2*(x), x])
        lb = GameObjects.border([-(x),0,x,self.mb[1]])
        self.objects += [tb,rb,bb,lb]

    def RandomEnemy(self):
        b = GameObjects.goomba([random.randint(100,560),random.randint(100,360),40,40],random.choice([1,-1]))
        self.objects.append(b)

    def createFloor(self):
        for i in range(int(round((self.mb[0] / 40),0)) + 1):
            b = GameObjects.block([i*40,460])
            self.objects.append(b)