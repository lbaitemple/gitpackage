class Flowers:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sun Flowers', 'Rose', 'Daisy']

    def printMembers(self):
        print('Printing members of the Flowers class')
        for member in self.members:
            print('\t%s ' % member)