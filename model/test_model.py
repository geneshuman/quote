import pytest, math

from point import *
from edge  import *
from model import *

def test_bounding_area():
    vertices = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]

    model = Model(edges)
    assert model.bounding_area() == 1.0

    vertices = [Point(0,0), Point(0,2), Point(1,2), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]

    model = Model(edges)
    assert model.bounding_area(1.0) == 12.0
