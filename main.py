from Read.ReadDataSet import *
import networkx as nx
import matplotlib

if __name__ == '__main__':
    rd = ReadDataSet("Data/12831")
    G = nx.Graph()
    for ln in rd.ReadEdges():
        a,b = map(int,ln.split())
        G.add_edge(a,b)
    print sorted(list(G.nodes()))