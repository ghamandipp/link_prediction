class ReadDataSet:
    def __init__(self,filename):
        self.filename = str(filename)
    def ReadEdges(self):
        fp = open(self.filename+".edges",'r')
        return fp.readlines()
    def ReadCircles(self):
        fp = open(self.filename + ".circles", 'r')
        return fp.readlines()
    def ReadEgoFeat(self):
        fp = open(self.filename + ".egofeat", 'r')
        return fp.readlines()
    def ReadFeat(self):
        fp = open(self.filename + ".feats", 'r')
        return fp.readlines()
    def ReadFeatName(self):
        fp = open(self.filename + ".featnames", 'r')
        return fp.readlines()