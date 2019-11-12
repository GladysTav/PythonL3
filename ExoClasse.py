class Voiture :
    def __init__(self, marque, immat="XX000XX", datecircul="01-01-1970"):
        self.marque = marque
        self.immat = immat
        self.datecircul=datecircul

    def get_Marque(self):
        return self.marque

    def get_Immat(self):
        return self.immat

    def get_Datecircul(self):
        return self.datecircul

    def set_Marque(self, marque):
        self.marque = marque

    def set_Immat(self, immat):
        self.immat = immat

    def set_Datecircul(self, datecircul):
        self.datecircul=datecircul

    def __str__(self):
        return "Voiture de marque "+self.get_Marque()+", immatriculée "+self.get_Immat()+", mise en circulation le "+self.get_Datecircul()

    def isDeCollection(self):
        if int(self.get_Datecircul()[6:])<=1999:
            return "est de collection"
        else:
            return "n'est pas de collection"


v1=Voiture("Renault","BQ950HT","13-05-1997")
v2=Voiture("BMW")

print(v1)
print(v2)
print()

v2.set_Immat("DQ887NS")
v2.set_Datecircul("10-02-2001")
print(v2)
print(v1.isDeCollection())
print(v2.isDeCollection())