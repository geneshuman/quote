import pytest

from point import *
from edge import *
from model import *
from util import *

def test_cut_speed():
    edge = LinearEdge([Point(33,0), Point(-27,1)])
    assert cut_speed(edge) == 1.0

    edge = CircularEdge([Point(0,0)], Point(3, 0))
    assert abs(cut_speed(edge) - 0.71653131057) < 0.000001

    edge = CircularEdge([Point(0,0), Point(1,0)], Point(3, 0))
    assert abs(cut_speed(edge) - 0.71653131057) < 0.000001

def test_quote():
    vertices = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(quote(model) - 1.4675) < 0.00000001

    vertices = [Point(0,0), Point(0,5), Point(3,5), Point(3,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]), LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)
    assert abs(quote(model) - 14.0975) < 0.00000001

    # come back to this
    # model = Model([CircularEdge([Point(1,0)], Point(0,0))])
    # assert abs(quote(model) - 14.0975) < 0.00000001
