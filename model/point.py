class Point(object):
    """ Simple representation of a 2d point """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(x:%.2f, y:%.2f)" % (self.x, self.y)
