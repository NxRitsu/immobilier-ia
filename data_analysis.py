import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.tree import plot_tree

# Charger le dataset préparé
file_path = 'ParisHousing_prepared.csv'
data = pd.read_csv(file_path)

# Estimation du prix
X_price = data.drop(columns=['price', 'category'])
y_price = data['price']
X_train, X_test, y_train, y_test = train_test_split(X_price, y_price, test_size=0.2, random_state=42)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Erreur quadratique moyenne (MSE) pour l'estimation du prix :", mean_squared_error(y_test, y_pred))

# Classification Basic/Luxe
X_category = data.drop(columns=['category', 'price'])
y_category = data['category'].map({'Basic': 0, 'Luxury': 1})
X_train, X_test, y_train, y_test = train_test_split(X_category, y_category, test_size=0.2, random_state=42)

classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("Précision de la classification (Basic ou Luxe) :", accuracy_score(y_test, y_pred))

# Visualisation des règles
plt.figure(figsize=(12, 8))
plot_tree(classifier, feature_names=X_category.columns, class_names=['Basic', 'Luxury'], filled=True)
plt.title('Arbre de décision pour la classification')
plt.show()

# Clusterisation pour identifier les similitudes
features = ['squareMeters', 'numberOfRooms']
kmeans = KMeans(n_clusters=2, random_state=42)
data['Cluster'] = kmeans.fit_predict(data[features])

# Visualisation des clusters
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['squareMeters'], y=data['numberOfRooms'], hue=data['Cluster'], palette='deep')
plt.title('Clusters basés sur la surface et le nombre de pièces')
plt.xlabel('Surface (m²)')
plt.ylabel('Nombre de pièces')
plt.legend(title='Cluster')
plt.show()

# Moyennes par cluster
cluster_means = data.groupby('Cluster')[features].mean()
print("Caractéristiques moyennes par cluster :\n", cluster_means)
