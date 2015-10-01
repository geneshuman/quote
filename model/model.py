from edge import *
from sets import Set

class Model(object):
    """ A representaion of a basic 2d object in terms of a collection of edges """

    def __init__(self, edges):
        self.edges = edges

    def __repr__(self):
        return "E:%s" % str(self.edges)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and Set(self.edges) == Set(other.edges))

    def __ne__(self, other):
        return not self.__eq__(other)

    def bounding_rectangle(self):
        ''' assume rectangle for now '''
        return [edge.vertices[0] for edge in self.edges]

    def bounding_area(self, pad=0.0):
        ''' computes the area of the bounding rectangle with padding '''
        rect = self.bounding_rectangle()
        w = LinearEdge([rect[0], rect[1]]).arc_length()
        h = LinearEdge([rect[1], rect[2]]).arc_length()
        return (w + pad) * (h + pad)
