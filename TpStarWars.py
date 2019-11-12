from pip._vendor.distlib.compat import raw_input


class Film:
    def __init__(self, titre, annee="0000", numero=1, cout=0, recette=0, acteurs=[],truc=[]):
        # Quand on crée un objet de class Film, on doit donner un titre, les autres sont facultatifs
        self.titre = titre
        self.annee = annee
        self.numero = numero
        self.cout = cout
        self.recette = recette
        self.acteurs=acteurs
        self.truc=truc

    def get_Titre(self):  # pour obtenir le titre
        return self.titre

    def get_Annee(self):  # pour obtenir l'année de sortie
        return self.annee

    def get_Numero(self):  # pour obtenir le numéro d'épisode
        return self.numero

    def get_Cout(self):  # pour obtenir le cout
        return self.cout

    def get_Recette(self):  # pour obtenir la recette
        return self.recette

    def get_Truc(self):  # pour obtenir la recette
        return self.truc

    def set_Titre(self,titre):  # pour définir le titre
        self.titre=titre

    def set_Annee(self,annee):  # pour définir l'année de sortie
        self.annee=annee

    def set_Numero(self,numero):  # pour définir le numéro d'épisode
        self.numero=numero

    def set_Cout(self,cout):  # pour définir le cout
        self.cout=cout

    def set_Recette(self,recette):  # pour définir la recette
        self.recette=recette

    def set_Truc(self,truc):  # pour définir la recette
        self.truc=truc

    def __str__(self):  # comme ça on peut obtenir les infos avec un print(monfilm)
        return self.titre+" n°"+str(self.numero)+", année de sortie : "+\
               str(self.annee)+"\ncout : "+str(self.cout)+"€\nrecette: "+str(self.recette)+"€"

    def get_Acteurs(self):
        return parcoureListe(self.acteurs)

    def set_Acteurs(self, acteurs):
        self.acteurs=acteurs

    def add_Acteur(self, acteur):
        self.acteurs.append(acteur)

    def nbActeurs(self):
        i=0
        for d in self.acteurs:
            i+=1
        return i

    def nbPersonnages(self):
        i=0
        for d in self.persos:
            i+=1
        return i

    def calculBenefice(self):
        return str(self.recette-self.cout)+"€"

    def isBefore(self,annee):
        if(self.annee<annee):
            return True
        else:
            return False

    def tri(self):
        self.acteurs = sorted(self.acteurs, key=lambda acteur: acteur.prenom)


class Acteur:
    def __init__(self, prenom,nom, duet=[]):
        self.nom = nom
        self.prenom=prenom
        self.duet=duet

    def get_Nom(self):
        return self.nom

    def get_Prenom(self):
        return self.prenom

    def get_Duet(self):
        return parcoureListe(self.duet)

    def set_Nom(self,nom):
        self.nom = nom

    def set_Prenom(self,prenom):
        self.prenom=prenom

    def set_Duet(self,duet):
        self.duet=duet

    def add_Duet(self,duet):
        self.duet.append(duet)

    def __str__(self):
        return self.prenom + " " + self.nom+"\nDuets:\n"+self.get_Duet()

    def nbPersonnages(self):
        i=0
        for d in self.duet:
            i+=1
        return i


class Personnage:
    def __init__(self, nom, prenom, duet=""):
        self.nom= nom
        self.prenom=prenom
        self.duet=duet

    def get_Nom(self):
        return self.nom

    def get_Prenom(self):
        return self.prenom

    def get_Duet(self):
        return self.duet

    def set_Nom(self,nom):
        self.nom = nom

    def set_Prenom(self,prenom):
        self.prenom=prenom

    def set_Duet(self,duet):
        self.duet=duet

    def __str__(self):
        return self.prenom + " " + self.nom


class Gentil:
    def __init__(self, force=True):
        self.force = force

    def get_Force(self):
        return self.force

    def set_Force(self, force):
        self.force = force

    def __str__(self):
        return self.force


class Mechant:
    def __init__(self, obscur=True):
        self.obscur = obscur

    def get_Obscur(self):
        return self.obscur

    def set_Obscur(self, obscur):
        self.obscur = obscur

    def __str__(self):
        return self.obscur


sw4=Film("Star Wars","1977",4,1456321,14563213)
#sw5=Film(raw_input("Titre du film : "),raw_input("Année : "),
         #raw_input("Numéro d'épisode : "),raw_input("Cout :"),raw_input("Recette : "))

sw5=Film("Star Wars","1980",5,4789652486, 417859632147586)

print(sw4)
print()
print(sw5)

chewbacca=Personnage("Chewbacca","Brhhhh")
maCollec=[]
maCollec.append(sw4)
maCollec.append(sw5)
maCollec.append(chewbacca)

def parcoureListe(liste):
    rep=""
    for l in liste:
        rep=rep + str(l) + "\n"
    return rep
print()
print(parcoureListe(maCollec))

minoton = Personnage("Minoton","")
PeterMayhew=Acteur("Peter","Mayhew",[chewbacca,minoton])
print()
print(PeterMayhew)
print()
print(PeterMayhew.nbPersonnages())

sw4.set_Truc(maCollec)
sw4.set_Acteurs([PeterMayhew, Acteur("Machin","Truc"), Acteur("Bidule","Muche")])
sw4.tri()
print("Acteurs de sw4 : \n")
print(sw4.get_Acteurs())

def makeBackUp(dico):
    print("Fonction makeBackUp\n")
    for objet in dico:
        print("Année : " + dico[objet].get_Annee())
        print("Titre : " + dico[objet].get_Titre())
        print("Bénéfice : " + str(dico[objet].calculBenefice()))
        print()

print()
mesFilms={sw4.get_Annee():sw4,sw5.get_Annee():sw5}
makeBackUp(mesFilms)

def makeBackUpTxt(dico):
    fichier = open("backUp.txt", "a")
    print("Fonction makeBackUpTxt\n")
    for objet in dico:
        fichier.write("Année : " + dico[objet].get_Annee()+"\n")
        fichier.write("Titre : " + dico[objet].get_Titre()+"\n")
        fichier.write("Bénéfice : " + str(dico[objet].calculBenefice())+"\n")
        fichier.write("\n\n")
    fichier.close()

makeBackUpTxt(mesFilms)

