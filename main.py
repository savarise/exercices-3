import random

class NPC:
    def __init__(self, nom, race, espèce, profession):
        self.nom = nom
        self.race = race
        self.espèce = espèce
        self.profession = profession

        self.force = self.rouler_4d6()
        self.agilité = self.rouler_4d6()
        self.constitution = self.rouler_4d6()
        self.intelligence = self.rouler_4d6()
        self.sagesse = self.rouler_4d6()
        self.charisme = self.rouler_4d6()

        self.classe_armure = random.randint(1, 12)
        self.point_de_vie = random.randint(1, 20)

    def rouler_4d6(self):
        result = 0
        for _ in range(4):
            result += random.randint(1, 6)
        result -= min(random.randint(1, 6) for _ in range(4))
        return result

    def afficher_caracteristiques(self):
        print("Nom:", self.nom)
        print("Race:", self.race)
        print("Espèce:", self.espèce)
        print("Profession:", self.profession)
        print("Force:", self.force)
        print("Agilité:", self.agilité)
        print("Constitution:", self.constitution)
        print("Intelligence:", self.intelligence)
        print("Sagesse:", self.sagesse)
        print("Charisme:", self.charisme)
        print("Classe d'armure:", self.classe_armure)
        print("Point de vie:", self.point_de_vie)


class Kobold(NPC):
    def attaquer(self, cible):
        dommages = random.randint(1, 6)
        print(f"{self.nom} attaque {cible.nom} et inflige {dommages} points de dommage!")
        cible.subir_dommage(dommages)

    def subir_dommage(self, quantite):
        print(f"{self.nom} subit {dommages} points de dommage!")
        self.point_de_vie -= dommages

class Hero(NPC):
    def attaquer(self, cible):
        critique = random.randit(1, 20)
        if critique==20:
            dommages = random.randint(1, 8) 
        elif critique==0:
            dommages = 0
        else:   
            if critique < cible.classe_armure:
                dommages = 0
            else:
                dommages = random.randint(1, 6) 
                print(f"{self.nom} attaque {cible.nom} et inflige {dommages} points de dommage!")
                cible.subir_dommage(dommages)

    def subir_dommage(self, quantite):
        print(f"{self.nom} subit {dommages} points de dommage!")
        self.point_de_vie -= dommages
