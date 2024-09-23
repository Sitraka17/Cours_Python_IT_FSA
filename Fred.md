## Introduction
Python est un langage de programmation polyvalent, lisible et puissant. Certains concepts sont nouveaux mais beaucoup sont classiques à tous langagues de programmation objet ! 

## 1. Syntaxe de base et différences avec Java

### Indentation
Contrairement à Java, Python utilise l'indentation pour définir les blocs de code.

```python
if condition:
    # Code ici
    pass
else:
    # Autre code ici
    pass
```

### Variables et types de données
Python est à typage dynamique, contrairement à Java.

```python
# Pas besoin de déclarer le type
x = 5
y = "Hello"
z = 3.14
```

### Listes (équivalent des ArrayList en Java)
```python
ma_liste = [1, 2, 3, 4, 5]
ma_liste.append(6)  # Ajoute 6 à la fin
premier_element = ma_liste[0]  # Indexation commence à 0, comme en Java
```

## 2. Fonctions et méthodes

```python
def ma_fonction(param1, param2=None):
    """Docstring: décrit la fonction"""
    if param2 is None:
        return param1
    return param1 + param2

# Appel de la fonction
resultat = ma_fonction(5, 3)
```

## 3. Classes et objets (POO)

```python
class MaClasse:
    def __init__(self, attribut):
        self.attribut = attribut
    
    def ma_methode(self):
        return f"Valeur de l'attribut : {self.attribut}"

# Instanciation
mon_objet = MaClasse("valeur")
print(mon_objet.ma_methode())
```

## 4. Gestion des exceptions

```python
try:
    # Code susceptible de lever une exception
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro !")
finally:
    print("Ce bloc est toujours exécuté")
```

## 5. Travail avec les bases de données (SQL)

Python offre plusieurs bibliothèques pour travailler avec SQL. Voici un exemple avec SQLite :

```python
import sqlite3

conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# Exécution d'une requête
cursor.execute("SELECT * FROM ma_table")
resultats = cursor.fetchall()

conn.close()
```

## 6. Manipulation de fichiers

```python
# Lecture
with open('mon_fichier.txt', 'r') as f:
    contenu = f.read()

# Écriture
with open('nouveau_fichier.txt', 'w') as f:
    f.write("Contenu à écrire")
```

## 7. Modules et packages

Python possède une vaste bibliothèque standard et un écosystème riche de packages tiers.

```python
import datetime
from collections import defaultdict

# Utilisation de modules tiers (après installation)
import pandas as pd
import numpy as np
```

## 8. Compréhensions de liste (spécifique à Python)

C'est une façon concise de créer des listes basées sur des séquences existantes.

```python
carres = [x**2 for x in range(10)]
```

## 9. Générateurs

Les générateurs permettent de créer des séquences de façon paresseuse (lazy evaluation).

```python
def mon_generateur():
    for i in range(10):
        yield i

for valeur in mon_generateur():
    print(valeur)
```

## 10. Décorateurs

Les décorateurs permettent de modifier le comportement des fonctions ou des classes.

```python
def mon_decorateur(func):
    def wrapper():
        print("Avant l'exécution")
        func()
        print("Après l'exécution")
    return wrapper

@mon_decorateur
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()
```
