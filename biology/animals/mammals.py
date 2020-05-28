class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals, add monkey
        self.members = ['Tiger', 'Elephant', 'Wild Cat', 'Monkey']

    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)