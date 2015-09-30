class Model(object):
    """ A representaion of a basic 2d object in terms of sequential edges """

    def __init__(self, edges):
        self.edges = edges

    def __repr__(self):
        return "E:%s" % str(self.edges)

    def bounding_rectangle(self):
        ''' complicated, will do later '''

    def bounding_area(self, pad=0.0):
        ''' complicated, will do later '''
        return 1.0
