class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    def __init__(self,x = 0, y = 0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y
    @classmethod
    def __is_verify(cls,value):
        return type(value) in (int,float) and cls.MIN_COORD <= value <= cls.MAX_COORD

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__is_verify(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__is_verify(value):
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector[0] ** 2 + vector[1] ** 2

v1 = RadiusVector2D()
v2 = RadiusVector2D(12020, 202020)
v3 = RadiusVector2D(1, 2)
res = RadiusVector2D.norm2([v3.x, v3.y])