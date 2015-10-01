import pytest, json

from point import *
from edge import *
from model import *
from util import *

# parsing
def test_parse_json():
    with open('data/rectangle.json') as data_file:
        data = json.load(data_file)
    loaded = parse_json(data)

    vertices = [Point(0,0), Point(0,3), Point(5,3), Point(5,0)]
    edges = [LinearEdge([vertices[0], vertices[1]]), LinearEdge([vertices[1], vertices[2]]),
             LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)

    assert loaded == model

    with open('data/cut_circular_arc.json') as data_file:
        data = json.load(data_file)

    loaded = parse_json(data)

    vertices = [Point(0,0), Point(2,0), Point(2,1), Point(0,1)]
    edges = [LinearEdge([vertices[0], vertices[1]]),
             CircularEdge([vertices[1], vertices[2]], Point(2.0, 0.5)),
             LinearEdge([vertices[2], vertices[3]]), LinearEdge([vertices[3], vertices[0]])]
    model = Model(edges)

    assert loaded == model

# quoting
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
