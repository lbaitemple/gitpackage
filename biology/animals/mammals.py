from biology.util import loadData
import os.path  as path


class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals, add monkey
    #        self.members = ['Tiger', 'Elephant', 'Wild Cat', 'Monkey']
        filename = path.join(path.dirname(__file__), "../conf/biology.csv")
        self.members = loadData(filename, "mammals")

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)