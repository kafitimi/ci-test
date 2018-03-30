class Cplx:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def r(self):
        return (self.x**2 + self.y**2)**0.5
    def arg(self):
        if self.r():
            return None
        else:
            return 0  # FIXME!