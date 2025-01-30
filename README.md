# **Développement d'une IA pour une Agence Immobilière**

## **Description du projet**
Ce projet a été développé pour répondre aux besoins spécifiques d'une agence immobilière en créant une Intelligence Artificielle (IA) capable de :
1. **Estimer le prix d'un logement à Paris** à partir de ses caractéristiques.
2. **Classer les logements dans les catégories "Basic" ou "Luxury".**
3. **Identifier des caractéristiques similaires entre ces deux catégories.**

Le projet suit une méthodologie rigoureuse, comprenant la préparation des données, la modélisation, et l’analyse des résultats avec des visualisations pertinentes.

---

## **Structure du projet**
### **1. Préparation des données**
- Nettoyage et transformation du dataset brut pour garantir des données fiables.
- Gestion des valeurs manquantes, suppression des doublons, traitement des valeurs aberrantes.
- Conversion des formats pour assurer la compatibilité avec les modèles IA.

### **2. Modélisation IA**
- Modèle de régression linéaire pour l'estimation des prix.
- Modèle d'arbre de décision pour la classification "Basic" ou "Luxury".
- Algorithme KMeans pour identifier les similitudes et les clusters.

---

## **Technologies utilisées**
- **Python** : Langage principal pour la manipulation des données et le développement des modèles IA.
- **Bibliothèques Python** :
  - `pandas` : Gestion et manipulation des données.
  - `matplotlib` et `seaborn` : Visualisation des données.
  - `scikit-learn` : Implémentation des modèles de machine learning.

---

## **Guide d'exécution**

### **1. Installation**
Cloner le projet et installer les dépendances nécessaires :
```bash
git clone https://github.com/votre-projet/immobilier-ia.git
cd immobilier-ia
pip install -r requirements.txt
```

### **2. Préparation des données**
Exécuter le script `data_preparation.py` pour nettoyer et préparer les données :
```bash
python data_preparation.py
```
Le script produit un fichier `ParisHousing_prepared.csv` contenant les données prêtes pour l’analyse.

### **3. Modélisation IA**
Exécuter le script `data_analysis.py` pour entraîner les modèles et produire les visualisations :
```bash
python data_analysis.py
```
Les résultats des modèles et les graphiques générés sont affichés directement.

---

## **Résultats clés**
### **Estimation des prix**
- **Modèle** : Régression linéaire.
- **Erreur quadratique moyenne (MSE)** : `7,272,273.48`.
- **Interprétation** : Les prédictions sont raisonnablement proches des valeurs réelles, mais il existe une marge d'amélioration.

### **Classification (Basic ou Luxury)**
- **Modèle** : Arbre de décision.
- **Précision** : `1.0`.
- **Interprétation** : Le modèle distingue parfaitement les catégories grâce à des données bien séparées.

### **Clusterisation**
- **Modèle** : KMeans (2 clusters).
- **Résultats** :
  - Cluster 0 : Moyenne des surfaces = `24,745 m²` ; Moyenne des pièces = `49.85`.
  - Cluster 1 : Moyenne des surfaces = `74,467 m²` ; Moyenne des pièces = `50.85`.
- **Interprétation** : La surface est une caractéristique clé pour différencier les clusters.

---

## **Structure des fichiers**
- **`ParisHousing.csv`** : Dataset brut utilisé pour le projet.
- **`data_preparation.py`** : Script pour nettoyer et préparer les données.
- **`data_analysis.py`** : Script contenant les modèles IA et les visualisations.
- **`ParisHousing_prepared.csv`** : Dataset nettoyé et prêt à l’analyse (généré par `data_preparation.py`).
- **`README.md`** : Documentation détaillée du projet.

---

## **Recommandations**
1. **Améliorations des modèles** :
   - Ajouter des caractéristiques comme la localisation ou l'état du logement.
   - Tester des algorithmes avancés (XGBoost, Random Forest).
2. **Analyse approfondie** :
   - Effectuer une validation croisée pour évaluer la robustesse des modèles.
   - Étudier les relations entre les caractéristiques secondaires.

---

## **Conclusion**
Ce projet a permis de construire une IA robuste et reproductible capable de :
- Prédire les prix des logements avec une bonne précision.
- Classer les logements dans des catégories claires.
- Identifier des groupes de logements partageant des caractéristiques similaires.

Le pipeline mis en place est extensible et peut être amélioré avec des données supplémentaires et des modèles plus avancés.
