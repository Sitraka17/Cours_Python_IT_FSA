## Cours pour IT FSA Post Finance: Introduction à Python pour Développeurs Expérimentés (JAVA, THALER, SQL Developer Oracle)

### Objectif du cours :
Ce cours est conçu pour Marco et Bilel qui ont une solide expérience en développement avec JAVA, THALER, et SQL Developer Oracle. Il offre une introduction pratique à Python, en mettant en évidence les différences et similitudes avec ces technologies tout en abordant les fonctionnalités puissantes et modernes de Python.

### Pré-requis :
- vous avez genre 20 ans d'expérience en JAVA, THALER et SQL Developer Oracle.
- Et une compréhension approfondie des concepts de programmation orientée objet (POO), des bases de données relationnelles, et des transactions financières.

---

### Plan du cours

#### 1. **Introduction à Python : Comparaison avec JAVA**
   - **Philosophie de Python** : Simplicité, lisibilité et productivité.
   - **Différences clés avec JAVA** : Typage dynamique, absence de compilation, indentation stricte.
   - **Environnement de développement** : Configuration de Python, IDEs recommandés (PyCharm, VSCode).

   **Exemple simple en Python :**
   ```python
   # Hello World en Python
   print("Hello, World!")
   ```

   **Comparaison avec JAVA :**
   ```java
   public class HelloWorld {
       public static void main(String[] args) {
           System.out.println("Hello, World!");
       }
   }
   ```

#### 2. **Structures de contrôle en Python**
   - **Boucles** : `for`, `while`
   - **Conditions** : `if`, `elif`, `else`
   - **Exemple d'implémentation d'une boucle et d'une condition** :
     ```python
     for i in range(5):
         if i % 2 == 0:
             print(f"{i} est pair")
         else:
             print(f"{i} est impair")
     ```

#### 3. **Programmation Orientée Objet (POO) en Python**
   - Création de classes en Python et comparaison avec la POO en JAVA.
   - **Constructeur**, **méthodes** et **héritage**.
   - **Exemple d'une classe simple** :
     ```python
     class Voiture:
         def __init__(self, marque, modele):
             self.marque = marque
             self.modele = modele

         def afficher_info(self):
             print(f"Marque: {self.marque}, Modèle: {self.modele}")

     voiture = Voiture("Tesla", "Model S")
     voiture.afficher_info()
     ```

#### 4. **Manipulation des fichiers**
   - **Lire/écrire des fichiers** en Python, utile pour le traitement de fichiers transactionnels.
   - Utilisation de `with` pour une gestion propre des fichiers :
     ```python
     with open('transactions.txt', 'r') as file:
         contenu = file.read()
         print(contenu)
     ```

#### 5. **Gestion des Exceptions**
   - Introduction à la gestion d'erreurs en Python : `try`, `except`, `finally`.
   - **Exemple** :
     ```python
     try:
         result = 10 / 0
     except ZeroDivisionError:
         print("Erreur : Division par zéro !")
     ```

#### 6. **Les Collections en Python : Listes, Dictionnaires, Tuples**
   - **Listes** : Similaires aux tableaux en JAVA mais dynamiques.
   - **Dictionnaires** : Utilisation des clés/valeurs, similaire aux `Map` en JAVA.
   - **Exemple avec une liste et un dictionnaire** :
     ```python
     fruits = ['pomme', 'banane', 'orange']
     inventaire = {'pommes': 10, 'bananes': 5, 'oranges': 8}
     ```

#### 7. **Interactions avec les Bases de Données**
   - Introduction à `sqlite3` et à l’utilisation de **pandas** pour la manipulation de données.
   - Connexion à une base de données SQL :
     ```python
     import sqlite3

     conn = sqlite3.connect('example.db')
     cursor = conn.cursor()

     cursor.execute('''CREATE TABLE transactions (id INTEGER PRIMARY KEY, montant REAL)''')
     conn.commit()
     conn.close()
     ```

#### 8. **Introduction à NumPy et Pandas : Puissance du traitement de données**
   - Présentation des bibliothèques **NumPy** pour les calculs numériques et **Pandas** pour la manipulation des données tabulaires.
   - **Exemple de création et manipulation d’un DataFrame Pandas** :
     ```python
     import pandas as pd

     data = {'Produit': ['A', 'B', 'C'], 'Ventes': [100, 150, 200]}
     df = pd.DataFrame(data)
     print(df)
     ```

#### 9. **Automatisation avec Python : Interaction avec des API**
   - Utilisation de la bibliothèque `requests` pour interagir avec des APIs REST.
   - **Exemple** :
     ```python
     import requests

     response = requests.get('https://api.exemple.com/data')
     print(response.json())
     ```

#### 10. **Utilisation des Expressions Régulières : Comparaison avec Java**
   - **Regex en Python** avec le module `re`.
   - **Exemple d’utilisation** :
     ```python
     import re

     texte = "L'email est exemple@test.com"
     email = re.search(r'\S+@\S+', texte)
     print(email.group())
     ```

#### 11. **Conclusion et Bonnes Pratiques**
   - Comparaison finale des paradigmes entre Python et JAVA/THALER/SQL Oracle.
   - **Gestion des ressources** en Python (GC, gestion mémoire, etc.).
   - Importance de l’écriture **lisible**, utilisation de l'outil **PEP8** pour respecter les conventions Python.

---

### Projets pratiques à réaliser
1. **Conversion d’un script SQL en script Python** utilisant la bibliothèque `sqlite3`.
2. **Implémentation d’une classe transactionnelle** pour simuler une opération financière.
3. **Automatisation de tâches** avec Python (ex. téléchargement et manipulation de fichiers, génération de rapports).

---

### Matériel supplémentaire :
- [Documentation officielle Python](https://docs.python.org/3/)
- Tutoriels avancés sur NumPy et Pandas pour la manipulation de données financières
- Exemples de projets Python orientés finance
