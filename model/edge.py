import math

class Edge(object):
    """ A generic representation of a two dimensional line segment of variable type """
    def __init__(self, vertices):
        self.vertices = vertices

        if(self.arc_length() == 0):
            raise ValueError('edge must have nonzero length')

    def arc_length(self):
        raise NotImplementedError("subclass responsibly")

    def theta_bound(self):
        raise NotImplementedError("subclass responsibly")

    def __ne__(self, other):
        return not self.__eq__(other)

class LinearEdge(Edge):
    """ A representation of a two dimensional linear line segment """
    def __init__(self, vertices):
        if(len(vertices) != 2):
            raise ValueError('linear edges need exactly 2 vertices')

        super(LinearEdge, self).__init__(vertices)

    def arc_length(self):
        return math.hypot(self.vertices[0].x - self.vertices[1].x,
                          self.vertices[0].y - self.vertices[1].y)

    def theta_bound(self, th):
        ''' finds [distance to closest point, distance to farthest point]
        on edge wrt line going through the origin that makes angle(th) wrt the x-axis
        values are positive for points counter clockwise from the line
        '''
        a = -1.0 * math.sin(th)
        b = math.cos(th)
        d = [a * v.x + b * v.y for v in self.vertices]
        d.sort()
        return d

    def __repr__(self):
        return "LinearEdge:%s" % str(self.vertices)


    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and set(self.vertices) == set(other.vertices))

    def __hash__(self):
        return hash(frozenset(self.vertices))

# utility method
def angular_distance(th0, th1):
    ''' given two values of theta, compute the angular distance
    0 < d < 2pi from th0 -> th1 moving clockwise from th0 to th1
    '''
    th0 = th0 % (2 * math.pi)
    th1 = th1 % (2 * math.pi)

    if th0 < th1:
        return th0 + (2 * math.pi - th1)
    else:
        return th0 - th1

class CircularEdge(Edge):
    """ A representation of a two dimensional circular arc
    Either a 1-verticed circle, or a 2-verticed arc
    moving clockwise from v[0] -> v[1]
    """
    def __init__(self, vertices, center):
        if(len(vertices) != 1 and len(vertices) != 2):
            raise ValueError('circular edges need exactly 1 or 2 vertices')

        self.center = center
        super(CircularEdge, self).__init__(vertices)

        # make sure vertices are same distance from center
        if(len(vertices) == 2 and abs(LinearEdge([self.vertices[1], self.center]).arc_length() -
                                      LinearEdge([self.vertices[0], self.center]).arc_length()) > 0.00000001): # should probably codify the acceptable floating point error somewhere
            raise ValueError('vertices must be same distance from center')

        if(self.r() == 0):
            raise ValueError('circular edges must have non zero radius')


    # could memoize this & some other stuff if our object was immutable & it mattered
    def r(self):
        return LinearEdge([self.vertices[0], self.center]).arc_length()

    # could probably refactor to use angular_distance() here
    def arc_length(self):
        r = self.r()
        if(len(self.vertices) == 1):
            return 2.0 * math.pi * r
        else:
            v0 = (self.vertices[0].x - self.center.x, self.vertices[0].y - self.center.y)
            v1 = (self.vertices[1].x - self.center.x, self.vertices[1].y - self.center.y)
            dp = v0[0] * v1[0] + v0[1] * v1[1]
            th = math.acos(dp / (r ** 2))

            # dot product gives us multiple possible th values, find right one
            if(v1[1] * v0[0] <= v0[1] * v1[0]):
                th = 2 * math.pi - th

            return r * th

    def theta_bound(self, th):
        ''' finds [distance to closest point, distance to farthest point]
        on edge wrt line going through the origin that makes angle(th) wrt the x-axis
        values are positive for points counter clockwise from the line
        '''

        # closest & furthest points of circle to th-line
        a = -1.0 * math.sin(th)
        b = math.cos(th)
        d = a * self.center.x + b * self.center.y

        circle_d = [d + self.r(), d - self.r()]
        circle_d.sort()

        if len(self.vertices) == 1:
            return circle_d

        # vertex distances
        v_dist = [a * v.x + b * v.y for v in self.vertices]
        v_dist.sort()

        # if poles of circle(wrt th-line) are in the arc, add to list
        th0 = math.atan2(self.vertices[0].y - self.center.y, self.vertices[0].x - self.center.x)
        th1 = math.atan2(self.vertices[1].y - self.center.y, self.vertices[1].x - self.center.x)

        if angular_distance(th0, th + math.pi / 2) <= angular_distance(th0, th1):
            v_dist.append(circle_d[1])

        if angular_distance(th0, th + 3 * math.pi / 2) <= angular_distance(th0, th1):
            v_dist.append(circle_d[0])

        v_dist.sort()

        return [v_dist[0], v_dist[-1]]

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.vertices == other.vertices
            and self.center == other.center)

    def __repr__(self):
        return "CircularEdge:%s r:%s" % (str(self.vertices), str(self.center))

    def __hash__(self):
        return hash(frozenset(self.vertices)) + hash(self.center)
