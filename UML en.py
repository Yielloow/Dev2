# ANIMAL

class Habitat:
    def __init__(self, type_habitat):
        self.type_habitat = type_habitat

class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def manger(self):
        pass

class Herbivore(Animal):
    def manger(self):
        print("Le herbivore mange des plantes.")

class Carnivore(Animal):
    def manger(self):
        print("Le carnivore mange de la viande.")

class Tete:
    def __init__(self, taille):
        self.taille = taille

class Corps:
    def __init__(self, taille, poids):
        self.taille = taille
        self.poids = poids

class Membres:
    def __init__(self, nombre):
        self.nombre = nombre


# Classe

class DossierPersonnel:
    def __init__(self, etat_civil, coordonnees):
        self.etat_civil = etat_civil
        self.coordonnees = coordonnees

class Professeur:
    def __init__(self, nom, prenom, matiere):
        self.nom = nom
        self.prenom = prenom
        self.matiere = matiere
        self.dossier_personnel = None

    def attribuer_dossier(self, dossier):
        self.dossier_personnel = dossier

class Eleve:
    def __init__(self, nom, prenom, niveau_etude):
        self.nom = nom
        self.prenom = prenom
        self.niveau_etude = niveau_etude
        self.dossier_personnel = None

    def attribuer_dossier(self, dossier):
        self.dossier_personnel = dossier

class Classe:
    def __init__(self):
        self.professeur = None
        self.eleves = []

    def ajouter_professeur(self, professeur):
        self.professeur = professeur

    def ajouter_eleve(self, eleve):
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            print("La classe est déjà pleine.")

#Email

class FichierJoint:
    def __init__(self, nom_fichier, type_fichier, taille):
        self.nom_fichier = nom_fichier
        self.type_fichier = type_fichier
        self.taille = taille

class Email:
    def __init__(self, titre, texte, expediteur, destination):
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destination = destination
        self.fichiers_joints = []

    def ajouter_fichier_joint(self, fichier_joint):
        self.fichiers_joints.append(fichier_joint)
