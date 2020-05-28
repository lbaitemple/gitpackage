class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals, add peacock
        self.members = ['Sparrow', 'Robin', 'Duck', 'Peacock']

    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)
