import math
class Cplx:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def r(self):
        return (self.x**2 + self.y**2)**0.5
    def arg(self):
        if self.r():
            result=0
            if self.x>0:
                result=math.atan2(self.y, self.x)
            if self.x<0 and self.y>=0:
                result=math.atan2(self.y, self.x)
            if self.x<0 and self.y<0:
                result=-math.pi+math.atan2(self.y, self.x)
            if self.x==0 and self.y>0:
                result=math.pi/2
            if self.x==0 and self.y<0:
                result=-math.pi/2
            return result
        else:
            return 0
