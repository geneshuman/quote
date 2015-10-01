from point import *
from edge import *
from model import *

def parse_json(data):
    """ turn a json object into a model.
        raises NotImplementedError for unknown edge types
        raises LookupError for dupliate vertex ids(dont care about edge ids as they aren't used)
        raises KeyError if the json is malformed
    """
    # vertices
    all_vertices = {}
    for i, v in data["Vertices"].iteritems():
        try:
            if all_vertices.has_key(int(i)):
                raise LookupError("duplicate vertex id - %s" % i)
            all_vertices[int(i)] = Point(v["Position"]["X"], v["Position"]["Y"])
        except (LookupError, KeyError) as e:
            raise ValueError("invalid json %s\nwith msg: %s" % (str(v), str(e)))

    # edges
    edges = []
    for _, edge in data["Edges"].iteritems():
        try:
            vertices = [all_vertices[int(v)] for v in edge["Vertices"]]
            if edge["Type"] == "LineSegment":
                edges.append(LinearEdge(vertices))
            elif edge["Type"] == "CircularArc":
                start = all_vertices[edge["ClockwiseFrom"]]
                if start != vertices[0]:
                    vertices = reversed(vertices)
                center = Point(edge["Center"]["X"], edge["Center"]["Y"])
                edges.append(CircularEdge(vertices, center))
            else:
                raise NotImplementedError("invalid edge type")
        except (NotImplementedError, KeyError, ValueError) as e:
            raise ValueError("invalid json %s\nwith msg: %s" % (str(edge), str(e)))

    return Model(edges)

# i'm going to skip this.  the quoting mechanism will work just fine if the clients
# provide topologically peculiar models.  it would probably be good to let them know though.
# but as it's somewhat irrelevant to the stated problem(and a bit complicated), i'm going to
# skip it.
def validate(model):
    """
    topology is reasonable <- I would assume that what clients legitimately want would be
      to cut out some number of closed curves from the stock.  maybe just make sure
      all vertices have degree 2 and there's no intersection?

    minimal distance between edges <- given the laser's non-zero thickness,
      theres a smallest distance between edges that we can cut

    maybe make sure edges dont everlap except at single points for efficiency?

    """
    pass


def cut_speed(edge):
    ''' the relative rate at which the machine can cut the edge (in/s) '''
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

    # print area, speeds, total_time

    return area * mat_cost + total_time * mac_cost
