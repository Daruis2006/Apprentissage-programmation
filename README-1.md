# 🎮🤖 Mon Parcours d'Apprentissage en Programmation

> De la POO aux jeux immersifs et à la robotique intelligente

## 👋 À propos

Bienvenue sur mon repo d'apprentissage ! Je documente ici mon parcours pour devenir développeur, avec deux objectifs majeurs :

1. **🎮 Créer des jeux immersifs** (Unity/Unreal Engine + VR/AR)
2. **🤖 Fabriquer des robots dotés d'intelligence artificielle** (faire sortir l'IA du virtuel vers le physique)

## 🛠️ Mes compétences actuelles

- **Python** - Niveau intermédiaire
- **R** - Bases
- **C** - Bases
- **POO (Programmation Orientée Objet)** - En cours d'apprentissage

## 📚 Ce que j'ai appris

### Session 1 : Fondamentaux de la POO (07/02/2026)

#### ✅ Concepts maîtrisés

- [x] Différence entre **Classe** et **Objet**
- [x] Créer des classes avec `__init__`
- [x] Ajouter des **méthodes** (actions) aux classes
- [x] **L'héritage** : créer des classes spécialisées
- [x] Utiliser `super()` pour hériter du parent

#### 💻 Projets réalisés

**Système de Robots avec héritage**
- Classe parent `Robot` avec nom, énergie et méthode `attaquer()`
- Classe enfant `RobotMedecin` qui hérite et ajoute la capacité de soigner

```python
class Robot:
    def __init__(self, nom, energie):
        self.nom = nom
        self.energie = energie
    
    def attaquer(self):
        return f"{self.nom} attaque !"

class RobotMedecin(Robot):
    def __init__(self, nom, energie, patients_soignes):
        super().__init__(nom, energie)
        self.patients_soignes = patients_soignes
    
    def soigner(self):
        return f"{self.nom} soigne un robot !"
```

## 🎯 Prochaines étapes

### À court terme
- [ ] Polymorphisme
- [ ] Encapsulation
- [ ] Classes abstraites
- [ ] Design Patterns

### Parcours Game Dev 🎮
- [ ] Python → PyGame (comprendre la game loop)
- [ ] C# → Unity
- [ ] Unreal Engine + C++
- [ ] VR/AR et optimisation

### Parcours Robotique + IA 🤖
- [ ] Python avancé + bases d'IA
- [ ] Arduino/Raspberry Pi
- [ ] ROS (Robot Operating System)
- [ ] IA embarquée (vision, NLP)

## 📂 Structure du repo

```
.
├── README.md                          # Tu es ici !
├── recaps/
│   └── session_1_bases_poo.md        # Récapitulatif détaillé de la session 1
├── code/
│   └── exercice_robots.py            # Mes exercices POO
└── projets/
    └── (à venir)
```

## 🌟 Ma philosophie d'apprentissage

> "La pratique est plus importante que la théorie"

- **Apprendre par projet** : créer des choses concrètes
- **Progresser pas à pas** : maîtriser les bases avant d'avancer
- **Documenter le parcours** : pour moi et pour aider les autres
- **Ne jamais abandonner** : même depuis un téléphone, on peut coder ! 📱💪

## 📖 Ressources

- [Documentation Python](https://docs.python.org/fr/)
- [Unity Learn](https://learn.unity.com/)
- [ROS Tutorials](https://wiki.ros.org/ROS/Tutorials)

## 🤝 Contact

Si tu es sur le même parcours ou si tu veux échanger sur la programmation, n'hésite pas !

---

**Dernière mise à jour :** Février 2026  
**Statut :** 🔥 En plein apprentissage !

---

<div align="center">

### 💡 "Le voyage de mille lieues commence par un premier pas"

*De zéro à développeur de jeux et roboticien, un concept à la fois.*

</div>
