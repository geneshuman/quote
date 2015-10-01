class Point(object):
    """ Simple representation of a 2d point """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(x:%.2f, y:%.2f)" % (self.x, self.y)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.x == other.x
            and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return (self.x, self.y).__hash__()
