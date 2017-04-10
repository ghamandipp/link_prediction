import networkx as nx
from operator import itemgetter
import operator


def common_neighbors(G, ebunch):
    ret = []

    for edge in ebunch:
        u, v = edge[0], edge[1]
        neighbors = sum(1 for _ in nx.common_neighbors(G, u, v))
        ret.append((u, v, neighbors))

    return ret

def ProcessNetwork(G, u):
    ebunch = []
    for v in G.nodes():
        if v not in G.neighbors(u) and v != u:
            ebunch.append((u, v))

    year_list = sim_index(G, ebunch, community='year')
    department_list = sim_index(G, ebunch, community='department')
    native_place_list = sim_index(G, ebunch, community='native_place')
    gender_list = sim_index(G, ebunch, community='gender')

    year = sorted(year_list, key=itemgetter(2), reverse=True)#[:10]
    department = sorted(department_list, key=itemgetter(2), reverse=True)#[:10]
    native_place = sorted(native_place_list, key=itemgetter(2), reverse=True)#[:10]
    gender = sorted(gender_list, key=itemgetter(2), reverse=True)#[:10]


    rankList = []
    rankList.append(year)
    rankList.append(department)
    rankList.append(native_place)
    rankList.append(gender)
    weights = [1,1,1,1]

    return rank(rankList,weights)


def rank(list1, list2):  # O(n^2)
    final_list = []
    rows = len(list1)
    flattened = [val[1] for sublist in list1 for val in sublist]
    flattened = set(flattened)
    d = dict.fromkeys(flattened, 0)
    for row in xrange(rows):
        p = list2[row]
        cols = len(list1[row])
        d[list1[row][0][1]] += p
        for col in xrange(1, cols):
            x = col - 1
            if list1[row][col][2] == list1[row][x][2]:
                d[list1[row][col][1]] += p
            else:
                p *= 0.8
                d[list1[row][col][1]] += p
    sortedx = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    for i in sortedx:
        final_list.append(i[0])
    return final_list


def sim_index(G, ebunch=None, community='department'):
    if ebunch is None:
        ebunch = nx.non_edges(G)

    def predict(u, v):
        Cu = _community(G, u, community)
        Cv = _community(G, v, community)
        if Cu == Cv:
            if G.node[v]['name'] == 'Default User':
                return 0.5
            else:
                return 1
        else:
            return 0

    return ((u, v, predict(u, v)) for u, v in ebunch)


def _community(G, u, community):
    """Get the community of the given node."""
    node_u = G.node[u]
    try:
        return node_u[community]
    except KeyError:
        raise nx.NetworkXAlgorithmError('No community information')
