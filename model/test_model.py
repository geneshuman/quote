import pytest

from point import *
from edge  import *
from model import *

def test_default():
    vertices = [Point(0,0), Point(0,1), Point(1,1), Point(1,0)]
    edges = [Edge([vertices[0], vertices[1]]), Edge([vertices[1], vertices[2]]), Edge([vertices[2], vertices[3]]), Edge([vertices[3], vertices[0]])]
    model = Model(edges)

    print model
    assert True == False
