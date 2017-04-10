from Read.ReadDataSet import *
import networkx as nx
from GraphProcessor.FeatureExtractraction import *
from Util.accuracy import *
from Util.load import *
import timeit

if __name__ == '__main__':

    start = timeit.default_timer()

    """rd = ReadDataSet("Data/12831")
    G = nx.Graph()
    for ln in rd.readEdges():
        a,b = map(int,ln.split())
        G.add_edge(a,b)

    ProcessNetwork(G,27985216)
    print sorted(list(G.neighbors(27985216)))"""

    # CSV Dataset Read and Flushed
    """rd = ReadDataSet("Data/Dataset")
    rd.readCSV()"""

    # Create Graph and save
    """rd = ReadDataSet("Data/Slashdot0811")
    G = nx.Graph()
    for ln in rd.readTxt():
        a, b = map(int, ln.split())
        G.add_edge(a, b)"""

    # Save Graph
    """flush(G)"""

    # Load Graph
    G = load()

    # Print Node Contents
    """for item in G.nodes(data=True):
        print item"""


    # Get Friends of node
    node = '2014BCS072'
    print G.node[node]
    print ""
    pairL = ProcessNetwork(G, node)
    for item in pairL:
        print item,G.node[item]

    # Calculate accuracies
    """lst = []
    for nodes in G.nodes():
        pairL = ProcessNetwork(G, nodes)
        neighborL = sorted(list(G.neighbors(nodes)))
        lst.append(evaluatePairList(pairL, neighborL))

    print lst
    print reduce(lambda x, y: x + y, lst) / float(len(lst))"""

    # Pagerank Simulation
    """pr = nx.pagerank(G, alpha=0.9)
    print pr"""

    stop = timeit.default_timer()

    print stop - start
