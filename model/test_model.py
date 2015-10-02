import pytest, math

from point import *
from edge  import *
from model import *

def test_bounding_area():
    # linear
    vertices = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(model.bounding_area() - 1.0) < 0.00000001

    vertices = [Point(0,0), Point(0,-1), Point(1,-1), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(model.bounding_area() - 1.0) < 0.00000001

    vertices = [Point(0,0), Point(0,2), Point(1,2), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(model.bounding_area(1.0) - 6.0) < 0.00000001

    vertices = [Point(-1,0), Point(0,1), Point(1,0), Point(0,-1)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(model.bounding_area() - 2.0) < 0.00000001

    vertices = [Point(-1,0), Point(0,1), Point(1,0), Point(0,-1)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(model.bounding_area() - 2.0) < 0.00000001

    # circular edges
    edges = [CircularEdge([Point(1,0)], Point(0,0))]
    model = Model(edges)
    assert abs(model.bounding_area() - 4.0) < 0.00000001

    edges = [CircularEdge([Point(1,0)], Point(2,0))]
    model = Model(edges)
    assert abs(model.bounding_area() - 4.0) < 0.00000001

    edges = [CircularEdge([Point(1,0)], Point(0,0)), CircularEdge([Point(1,0)], Point(2,0))]
    model = Model(edges)
    assert abs(model.bounding_area() - 8.0) < 0.00000001

    vertices = [Point(1,0), Point(0,1), Point(-1,0), Point(0,-1)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    edges.append(CircularEdge([Point(4,1), Point(4, -1)], Point(4,0)))
    model = Model(edges)
    assert abs(model.bounding_area() - 12.0) < 0.00000001

    vertices = [Point(1,1), Point(1,-1), Point(-1,-1), Point(-1,1)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    edges.append(CircularEdge([Point(8,4), Point(4, 8)], Point(6,6)))
    model = Model(edges)
    assert abs(model.bounding_area() - 56.0) < 0.00000001

    vertices = [Point(1,1), Point(1,-1), Point(-1,-1), Point(-1,1)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    edges.append(CircularEdge([Point(4, -8), Point(8,-4)], Point(6,-6)))
    model = Model(edges)
    assert abs(model.bounding_area() - 56.0) < 0.00000001
