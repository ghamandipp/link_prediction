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
        ebunch.append((u, v))

    adamic_adar_index_list = sim_index(G, ebunch, community='year')
    jaccard_coefficient_list = sim_index(G, ebunch, community='department')
    common_neighbors_list = sim_index(G, ebunch, community='native_place')

    common_neighbor = sorted(common_neighbors_list, key=itemgetter(2), reverse=True)#[:10]
    adamic_adar_index = sorted(adamic_adar_index_list, key=itemgetter(2), reverse=True)#[:10]
    jaccard_coefficient = sorted(jaccard_coefficient_list, key=itemgetter(2), reverse=True)#[:10]

    rankList = []
    rankList.append(common_neighbor)
    rankList.append(adamic_adar_index)
    rankList.append(jaccard_coefficient)
    weights = [1,1,1]

    return rank(rankList,weights)

# Upgrade needed - same value of p for same sim_index value
def rank(list1, list2):  # O(n^2)
    final_list = []
    rows = len(list1)
    flattened = [val for sublist in list1 for val in sublist]
    flattened = set(flattened)
    d = dict.fromkeys(flattened, 0)
    for row in xrange(rows):
        p = list2[row]
        cols = len(list1[row])
        for col in xrange(cols):
            d[list1[row][col]] += p
            p *= 0.8
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
