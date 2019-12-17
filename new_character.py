class NewCharacter():

    def __init__(self):
        self.stupidity = 0
        self.bravery = 0
        self.points = 30

    def get_stupidity(self):
        return self.stupidity

    def get_bravery(self):
        return self.bravery

    def set_stupidity(self, stupidity):
        self.stupidity = stupidity

    def set_bravery(self, bravery):
        self.bravery = bravery

    def get_points(self):
        return self.points

    def add_points(self, new_points):
        self.points += new_points

    def remove_points(self, new_points):
        self.points -= new_points
