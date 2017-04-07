import cPickle as pickle

def flush(G):
    with open("Graph/UserGraph.pkl", 'wb') as output:
        pickle.dump(G, output, pickle.HIGHEST_PROTOCOL)


def load():
    with open("Graph/UserGraph.pkl", 'rb') as input:
        G = pickle.load(input)
    return G