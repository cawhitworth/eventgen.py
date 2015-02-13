class SymbolicConstant(object):
    index = 0

    def __init__(self):
        self.i = SymbolicConstant.index
        SymbolicConstant.index += 1

    def __eq__(self, other):
        return self.i == other.i

