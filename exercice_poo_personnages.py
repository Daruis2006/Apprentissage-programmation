# Code corrigé - Classe Robot avec héritage

class Robot:
    def __init__(self, nom, energie):
        self.nom = nom
        self.energie = energie 
    
    def attaquer(self):
        return f"{self.nom} attaque !"

# CLASSE ENFANT - RobotMedecin (créée par l'utilisateur)
class RobotMedecin(Robot):
    def __init__(self, nom, energie, patients_soignes):
        super().__init__(nom, energie)
        self.patients_soignes = patients_soignes
    
    def soigner(self):
        return f"{self.nom} soigne un robot !"

# Création des objets
Robot1 = Robot("Sam", 100)
medecin = RobotMedecin("Dr. Robot", 90, 15)

# Test
print(f"{Robot1.nom} : {Robot1.attaquer()}")
print()
print(f"{medecin.nom} - Énergie: {medecin.energie}% - Patients soignés: {medecin.patients_soignes}")
print(medecin.attaquer())  # Hérité du parent !
print(medecin.soigner())   # Sa propre méthode !
