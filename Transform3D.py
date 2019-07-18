import numpy as np
from vector import Vector

class Transform3D:
    '''
    Maintains the resultant transformation of successive translation/rotations.
    '''

    def __init__(self):
        # order 4 transformation matrix
        # size is 4 to accomodate translations as linear transformations.
        self.matrix = np.identity(4)

    def translate(self, v):
        '''
        Translate by Vector v.
        '''
        m = np.identity(4)
        m[:3,3] = v.x, v.y, v.z
        self.matrix = m @ self.matrix

    def rotate(self, theta, axis = Vector(0, 0, 1), center = Vector(0, 0, 0)):
        '''
        Rotate about an axis.

        theta = angle in radians.
        axis = orientation vector of rotation axis,
            need not be unitary.
        center = a point on the axis.
        '''
        
        m = np.identity(4)
        am = axis.norm()
        x, y, z = axis.x / am, axis.y / am, axis.z / am
        c = np.cos(theta)
        s = np.sin(theta)
        m[0, 0] = c + x * x * (1 - c)
        m[1, 1] = c + y * y * (1 - c)
        m[2, 2] = c + z * z * (1 - c)
        m[0, 1] = x * y * (1 - c) - z * s
        m[0, 2] = x * z * (1 - c) + y * s
        m[1, 0] = y * x * (1 - c) + z * s
        m[1, 2] = y * z * (1 - c) - x * s
        m[2, 0] = z * x * (1 - c) - y * s
        m[2, 1] = z * y * (1 - c) + x * s
        self.translate(center * (-1))
        self.matrix = m @ self.matrix
        self.translate(center)

    def scale(self, factor, center = Vector(0, 0, 0)):
        '''
        Scale about center by factor.
        '''

        self.translate(center * (-1))
        m = np.identity(4) * factor
        m[3][3] = 1
        self.matrix = m @ self.matrix
        self.translate(center)

    def transform(self, v):
        '''
        Transform v by transformation self.matrix.

        Returns transformed vector.
        '''

        nv = np.array([v.x, v.y, v.z, 1])
        nv = self.matrix @ nv
        return Vector(*map(float, nv[:3]))

