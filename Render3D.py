from vector import Vector

class Render3D:
    '''
    Renders 3D points on 2D screen.
    '''

    def __init__(self, d = 1000, c = Vector(0, 0, 0)):
        '''
        d = perpendicular distance in pixels between eye and screen.
        c = projection of center of 3D perspective on screen.
        '''
        self.d = d
        self.c = c

    def render(self, v):
        '''
        Convert vector v to 2D point.
        
        returns 2 tuple of integers,
        representing (x, y) on screen.
        '''
        return (round(self.c.x + (self.d * (v.x - self.c.x) / (self.d + (v.z - self.c.z)))),
            round(self.c.y + (self.d * (v.y - self.c.y) / (self.d + (v.z - self.c.z)))))

