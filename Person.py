import re


class Person:
    def __init__(self):
        self.rollNo = None
        self.name = None
        self.gender = None
        self.native_place = None
        self.mail = None

    def verifyDetails(self, item, index):
        if index == 0:
            if (item.isalpha()):
                return True
            else:
                return False
        if index == 1:
            if (item[0:4].isdigit() and item[4:7].isalpha() and item[7:10].isdigit()):
                return True
            else:
                return False
        if index == 4:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', item)
            if match == None:
                return False
            else:
                return True
        return True

    def readPersonalDetails(self, line):
        details = line.split(',')[:5]
        iterator = 0
        for item in details:
            if (self.verifyDetails(item, iterator)):
                if iterator == 0:
                    self.name = item
                elif iterator == 1:
                    self.rollNo = item
                elif iterator == 2:
                    self.gender = item
                elif iterator == 3:
                    self.native_place = item
                elif iterator == 4:
                    self.mail = item
            iterator += 1