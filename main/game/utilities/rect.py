import math
from game.definitions.color_definitions import Colors
from game.definitions.global_definitions import GlobalDefinitions

class Rect():
    def __init__(self, p=[(0, 0, 0)*4], c=Colors.WHITE, s=(0, 0, 0)):
        self.pos = p
        self.col = c
        self.shade = (0, 0, 0)
        self.sideLight = s
        self.rectList = GlobalDefinitions().rectList
        self.rectList.append(self)
        self.gamepad = GlobalDefinitions().gamepad
        self.size = GlobalDefinitions().size

    def sumVec2(self,v1, v2):    
        return (v1[0] + v2[0], v1[1] + v2[1])
    
    def getPointList(self, screenCenter):
        return [self.sumVec2(self.getPointOnScreen(pt), screenCenter) for pt in self.pos]
    
    def destroy(self):
        self.rectList.remove(self)
    
    def getMid(self):
        mPos = (0, 0, 0)
        for m in self.pos:
            mPos = self.sumVec(mPos, m)
        return self.calcVec(mPos, (4, 4, 4), lambda x, y: x/y)
    
    def getCol(self):
        return self.addCol(self.addCol(self.col, self.shade), self.sideLight)
    

    def getPointOnScreen(self,point):
        global camAngle, idep, iv, ih, cam
        dV = self.subVec(point, cam[0])
        l = self.dot(idep, dV)
        rat = camAngle / l
        dV = self.calcVec((rat, rat, rat), dV, lambda x, y: x * y)
        return (self.dot(ih, dV), self.dot(iv, dV))

    def calcVec(self,v1, v2, f):
        return tuple(f(a, b) for a, b in zip(v1, v2))

    def addCol(self,col1,col2):
        r1,g1,b1=col1
        r2,g2,b2=col2
        return (max(0,min(255,r1+r2)),max(0,min(255,g1+g2)),max(0,min(255,b1+b2)))
    
    def dot(self,v1,v2):
        x1,y1,z1=v1
        x2,y2,z2=v2
        return (x1*x2)+(y1*y2)+(z1*z2)
    
    def norm(self,v):
        l = math.sqrt(self.dot(v, v))
        return tuple(a/l for a in v)
    
    def pyToVec(self,py, l):
        pitch, yaw = py
        return (l*math.cos(yaw)*math.cos(pitch), l*math.sin(yaw)*math.cos(pitch), l*math.sin(pitch))

    def sumVec(self,v1, v2):
        return tuple(a+b for a, b in zip(v1, v2))

    def subVec(self,v1, v2):
        return tuple(a-b for a, b in zip(v1, v2))

    def cross(self,v1, v2):
        x1, y1, z1 = v1
        x2, y2, z2 = v2
        return (y1*z2 - y2*z1, z1*x2 - z2*x1, x1*y2 - x2*y1)
    
    def drawCube(self,loc, col):
        size = self.size
        pi = math.pi
        pl = [self.sumVec((0, 0, -size/2), self.pyToVec((0, (1 + 2*i) * pi/4), size/2 * math.sqrt(2))) for i in range(4)] + \
            [self.sumVec((0, 0, size/2), self.pyToVec((0, (1 + 2*i) * pi/4), size/2 * math.sqrt(2))) for i in range(4)]
        for i, v in enumerate(pl):
            pl[i] = self.sumVec(loc, v)
        self.drawRect([pl[i] for i in [0, 1, 2, 3]], col)
        self.drawRect([pl[i] for i in [4, 5, 6, 7]], col)
        self.drawRect([pl[i] for i in [0, 1, 5, 4]], col)
        self.drawRect([pl[i] for i in [2, 3, 7, 6]], col)
        self.drawRect([pl[i] for i in [1, 2, 6, 5]], col)
        self.drawRect([pl[i] for i in [3, 0, 4, 7]], col)
