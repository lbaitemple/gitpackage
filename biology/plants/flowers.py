from biology.util import loadData
import os.path  as path

class Flowers:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        # self.members = ['Sun Flowers', 'Rose', 'Daisy']
        filename = path.join(path.dirname(__file__), "../conf/biology.csv")
        self.members =loadData(filename, "flowers")


    def printMembers(self):
        print('Printing members of the Flowers class')
        for member in self.members:
            print('\t%s ' % member)