import pandas as pd

# Charger le dataset
file_path = 'ParisHousing.csv'
data = pd.read_csv(file_path)

# Supprimer les doublons
data = data.drop_duplicates()

# Gérer les valeurs manquantes
num_cols = data.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    data[col] = data[col].fillna(data[col].mean())

cat_cols = data.select_dtypes(include=['object']).columns
for col in cat_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Normaliser la colonne 'category'
if 'category' in data.columns:
    data['category'] = data['category'].str.strip().str.capitalize()
    data['category'] = data['category'].replace({
        'Basi': 'Basic',
        'Luxry': 'Luxury',
        'Luxy': 'Luxury',
        'Lxury': 'Luxury'
    })

# Convertir les colonnes contenant des chiffres formatés comme texte
for col in data.columns:
    if data[col].dtype == 'object' and data[col].str.contains(r'^\d+,\d+$').any():
        data[col] = data[col].str.replace(',', '.').astype(float)

# Convertir les colonnes booléennes 'Yes'/'No' en 1/0
for col in data.select_dtypes(include=['object']).columns:
    if set(data[col].unique()) <= {'Yes', 'No'}:
        data[col] = data[col].map({'Yes': 1, 'No': 0})

# Supprimer les valeurs aberrantes
for col in num_cols:
    q1, q3 = data[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound, upper_bound = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

# Sauvegarder le dataset nettoyé
output_file_path = 'ParisHousing_prepared.csv'
data.to_csv(output_file_path, index=False)
print(f"Dataset nettoyé sauvegardé dans : {output_file_path}")
