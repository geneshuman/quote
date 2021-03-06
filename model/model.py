import math

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

    # Ok this is a bit curious.  I'm assuming we need to figure out optimal orientation, which
    # as far as I can tell is a bit tricky.  The solution I've implemented is an approximation,
    # and fairly dumb, although is fairly simple and should be practically effective up to a point.
    # The basic question is what is the minimum value w * h of bounding_box(th), as
    # 0 <= th <= pi / 2, where a box is oriented at angle th wrt the x axis.  There is
    # certainly a mathematically correct answer, but I can't find any particuarly elegant or
    # efficent(codewise) ways of doing this.  This is certainly a solved problem so the
    # ultimately correct solution would involve researching the problem and either implementing or
    # finding an existing version of the solution.  Probably overkill here.  So what I do is
    # basically just manually iteratate over 0 < th < pi / 2 and compute the bounding box for
    # each value of th.  I bet this is practically good enough.  It's linear in the number of
    # edges, although the constant might be big.  Probably doesn't matter.  Can be made arbitrarily
    # precise.  I'm sure you could be smart & dynamicaly choose your values of th to test, but this
    # seems tricky.  Probably a decent optimization though.  But unless you're machining a zillion
    # pieces, this should be fine.
    def bounding_area(self, pad=0.0):
        '''  '''
        N = 100 # just a guess
        min_data = None # (th, a, w, h)

        for n in xrange(N + 1):
            th = n * math.pi / (2 * N)

            w_min = w_max = h_min = h_max = None
            for edge in self.edges:
                b_min, b_max = edge.theta_bound(th)
                if w_min == None or b_min < w_min:
                    w_min = b_min
                if w_max == None or b_max > w_max:
                    w_max = b_max

                b_min, b_max = edge.theta_bound(th + math.pi / 2.0)
                if h_min == None or b_min < h_min:
                    h_min = b_min
                if h_max == None or b_max > h_max:
                    h_max = b_max

            w = w_max - w_min
            h = h_max - h_min
            area = w * h

            if min_data == None or area < min_data[1]:
                min_data = (th, area, w, h)

        return (min_data[2] + pad) * (min_data[3] + pad)
