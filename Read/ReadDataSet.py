import re
import networkx as nx
from Util.load import *


class ReadDataSet:
    def __init__(self, filename):
        self.filename = str(filename)

    def readEdges(self):
        fp = open(self.filename + ".edges", 'r')
        return fp.readlines()

    def readCircles(self):
        fp = open(self.filename + ".circles", 'r')
        return fp.readlines()

    def readEgoFeat(self):
        fp = open(self.filename + ".egofeat", 'r')
        return fp.readlines()

    def readFeat(self):
        fp = open(self.filename + ".feat", 'r')
        return fp.readlines()

    def readFeatName(self):
        fp = open(self.filename + ".featnames", 'r')
        return fp.readlines()

    def readTxt(self):
        fp = open(self.filename + ".txt", 'r')
        while (fp.readline()[0] == "#"):
            pass
        return fp.readlines()

    def readCSV(self):
        fp = open(self.filename + ".csv", 'r')
        G = nx.Graph()
        for ln in fp.readlines()[1:]:
            readPersonalDetails(G, ln)
        flush(G)


# Changes Required Below
def readPersonalDetails(G, line):
    details = line.split(',')[1:6]
    iterator = 0
    rollNo = None
    flag = True
    for item in details:
        if (verifyDetails(item, iterator)):
            if iterator == 0:
                rollNo = fit(item)
                G.add_node(rollNo)
                extract(G,rollNo)
            elif iterator == 1:
                G.node[rollNo]['name'] = item
            elif iterator == 2:
                G.node[rollNo]['gender'] = item
            elif iterator == 3:
                G.node[rollNo]['native_place'] = item
            elif iterator == 4:
                G.node[rollNo]['mail'] = item
        else:
            try:
                G.remove_node(rollNo)
                flag = False
            except:
                pass
            break
        iterator += 1

    if flag:
        neighbors = line.split(',')[6:]
        for item in neighbors:
            if item != "" and not G.has_node(item):
                ln1 = "Default Timestamp,"+item+",Default User,Male,Other,,,,,,"
                readPersonalDetails(G, ln1)

def fit(rollNo):

    if rollNo[-1] == "\n":
        rollNo = rollNo[:len(rollNo)-1]

    if len(rollNo) == 10:
        rollNo = rollNo[:4] + rollNo[4:7].upper() + rollNo[7:]
    elif len(rollNo) == 14:
        rollNo = rollNo[:4] + rollNo[4:9].upper() + rollNo[9:]

    return rollNo


def extract(G, item):
    dict = {"BTECS":"BCS","BTECV":"BCV","BTEIT":"BIT","BTEEL":"BEL","BTEEN":"BEN","BTEME":"BME"}
    year = int(item[0:4])
    department = None
    if len(item) == 10:
        department = item[4:7].upper()

    elif len(item) == 14:
        department = dict[item[4:9].upper()]

    G.node[item]['year'] = year
    G.node[item]['department'] = department


def verifyDetails(item, index):
    if index == 0:
        if len(item) == 10:
            if (item[0:4].isdigit() and item[4:7].isalpha() and item[7:10].isdigit()):
                return True
        elif len(item) == 14:
            if (item[0:4].isdigit() and item[4:9].isalpha() and item[9:14].isdigit()):
                return True
        return False

    # Name could contain spaces
    """if index == 1:
        if (item.isalpha()):
            return True
        else:
            return False"""

    if index == 4:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', item)
        if match == None and item != "":
            return False
        else:
            return True

    return True
