from sets import Set
import pytest, math

from point import *
from edge  import *

def test_linear_edge_length():
    vertices = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    assert [edge.arc_length() for edge in edges] == [1.0, 1.0, 1.0, 1.0]

def test_linear_theta_bounds():
    edge = LinearEdge([Point(0,0), Point(1,0)])
    assert edge.theta_bound(0) == [0,0]

    edge = LinearEdge([Point(0,0), Point(1,0)])
    assert edge.theta_bound(math.pi / 2) == [-1,0]

    edge = LinearEdge([Point(1,1), Point(2,2)])
    bound = edge.theta_bound(-1.0 * math.pi / 4)
    assert abs(bound[0] - math.sqrt(2)) < 0.0000001 and abs(bound[1] - math.sqrt(8)) < 0.0000001

def test_circular_edge_length():
    # single vertex
    edge = CircularEdge([Point(0,1)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi ) < 0.0000001

    edge = CircularEdge([Point(0,2)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi * 2.0 ) < 0.0000001

    # double vertex
    edge = CircularEdge([Point(0,1), Point(0,1)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi ) < 0.0000001

    edge = CircularEdge([Point(1,0), Point(0,1)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi / 4 ) < 0.0000001

    edge = CircularEdge([Point(0,1), Point(1,0)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi * 3 / 4 ) < 0.0000001

    edge = CircularEdge([Point(0,1), Point(-1,0)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi / 4 ) < 0.0000001

    edge = CircularEdge([Point(-1,0), Point(0,1)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi * 3 / 4 ) < 0.0000001

    edge = CircularEdge([Point(1,0), Point(-1,0)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * math.pi * 2 / 4 ) < 0.0000001

    edge = CircularEdge([Point(1,0), Point(-0.9,0.1)], Point(0,0))
    assert edge.arc_length() < math.pi

    edge = CircularEdge([Point(1,0), Point(-0.9,-0.1)], Point(0,0))
    assert edge.arc_length() > math.pi

    edge = CircularEdge([Point(0,2), Point(0,-2)], Point(0,0))
    assert abs(edge.arc_length() - 2.0 * 2.0 * math.pi * 2 / 4 ) < 0.0000001

    edge = CircularEdge([Point(0,2), Point(-0.1,-0.9)], Point(0,0))
    assert edge.arc_length() < 2.0 * math.pi

    edge = CircularEdge([Point(0,2), Point(0.1,-0.9)], Point(0,0))
    assert edge.arc_length() > 2.0 * math.pi


def test_equality():
    e0 = LinearEdge([Point(0,0), Point(0,1)])
    e1 = LinearEdge([Point(0,0), Point(0,1)])

    assert e0 == e1

    e0 = LinearEdge([Point(0,0), Point(0,1)])
    e1 = LinearEdge([Point(0,1), Point(0,0)])

    assert e0 == e1
