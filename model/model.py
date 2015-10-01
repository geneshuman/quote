from edge import *

class Model(object):
    """ A representaion of a basic 2d object in terms of sequential edges """

    def __init__(self, edges):
        self.edges = edges

    def __repr__(self):
        return "E:%s" % str(self.edges)

    def bounding_rectangle(self):
        ''' assume rectangle for now '''
        return [edge.vertices[0] for edge in self.edges]

    def bounding_area(self, pad=0.0):
        ''' computes the area of the bounding rectangle with padding '''
        rect = self.bounding_rectangle()
        w = LinearEdge([rect[0], rect[1]]).arc_length()
        h = LinearEdge([rect[1], rect[2]]).arc_length()
        return (w + 2.0 * pad) * (h + 2.0 * pad)
