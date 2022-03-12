



class Plane:
    def __init__(self, vectors):
        self.basis1 = vectors[0]
        self.basis2 = vectors[1]
    def getVectors(self):
        return [self.basis1, self.basis2]
