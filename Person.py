import datetime

class Person:
    def __init__(self, name, genre, birth, quotation):
        self.name = name
        self.birth = birth
        self.genre = genre
        self.quotation = quotation
    
    def __str__(self):
        return self.name + " " + self.genre + " " + str(self.birth.year) + " " + str(self.quotation)

    def AbleIVSSPension(self):
        if self.genre == "M" or self.genre=="m":
            return (self.quotation >= 750 and datetime.datetime.now().year - self.birth.year >= 60)
        else:
            return (self.quotation >= 750 and datetime.datetime.now().year - self.birth.year >= 55)





