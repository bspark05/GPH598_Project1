import pysal

def __init__(self, params):
    '''
    Constructor
    '''

def openFile(connectionString, mode='r'):
        point = pysal.pysal.core.FileIO.FileIO.open(connectionString, mode='r')  # @UndefinedVariable
        point.seek(0)
        outputList = []
        for i in point:
            outputList.append(i)
        return outputList
