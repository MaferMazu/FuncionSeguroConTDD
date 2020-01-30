import datetime

MIN_AGE_PENSIONM=60
MIN_AGE_PENSIONF=55
MIN_QUOT= 750
class Person:
    def __init__(self, name, genre, birth, quotation):
        self.name = name
        self.birth = birth
        self.genre = genre
        self.quotation = quotation
    
    def __str__(self):
        return "Persona de genero: " + self.genre + ", año: " + str(birthYear) + ", y cotización: " + str(self.quotation)

    def AbleIVSSPension(self):
        birthYear=self.birth.year
        personQuot=self.quotation
        personAge=datetime.datetime.now().year - self.birth.year
        if self.genre == "M" or self.genre=="m":
            return (personQuot >= MIN_QUOT  and personAge >= MIN_AGE_PENSIONM)
        else:
            return (personQuot >= MIN_QUOT  and personAge >= MIN_AGE_PENSIONF)






