class Edge(object):
    """ """
    def __init__(self, vertices):
        self.vertices = vertices

    def arc_length(self):
        pass

    def __repr__(self):
        return "V:%s" % str(self.vertices)


class LinearEdge(Edge):
    """ """
    def __init__(self, vertices):
        super(LinearEdge, self).__init__(vertices)

    def arc_length(self):
        1.0


class CircularEdge(Edge):
    """ """
    def __init__(self, vertices, center):
        super(CircularEdge, self).__init__(vertices)

    def arc_length(self):
        1.0
