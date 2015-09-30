class Edge(object):
    """ """
    def __init__(self, vertices):
        self.vertices = vertices

    def arc_length(self):
        pass


class LinearEdge(Edge):
    """ """
    def __init__(self, vertices):
        super(LinearEdge, self).__init__(vertices)


class CircularEdge(Edge):
    """ """
    def __init__(self, vertices, center):
        super(CircularEdge, self).__init__(vertices)
