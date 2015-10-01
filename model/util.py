from edge import *

def load(f):
    """ """
    pass


def validate(model):
    """
    loops are well formed
    loops dont intersect
    minimal distance between edges
    """
    pass


def cut_speed(edge):
    if(type(edge) == LinearEdge):
        return 1.0
    elif(type(edge) == CircularEdge):
        return math.exp(-1.0 / edge.r())
    else:
        raise NotImplementedError("invalid edge type")


def quote(model, pad=0.1, mat_cost=0.75, mac_cost=0.07, v_max=0.5):
    """ """

    area       = model.bounding_area(pad)
    speeds     = [v_max * cut_speed(edge) for edge in model.edges]
    total_time = sum([elt[1].arc_length() / elt[0] for elt in zip(speeds, model.edges)])

    print area, speeds, total_time

    return area * mat_cost + total_time * mac_cost
