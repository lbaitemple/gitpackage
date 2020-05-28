from biology.util import loadData
import os.path  as path
class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals, add peacock
        #self.members = ['Sparrow', 'Robin', 'Duck', 'Peacock']
        filename = path.join(path.dirname(__file__), "../conf/biology.csv")
        self.members =loadData(filename, "birds")

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)
