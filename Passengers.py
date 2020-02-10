from People import People

class Passengers(People):

    def __init__(self, name, passport):
        self.passport = passport
        self.name = name