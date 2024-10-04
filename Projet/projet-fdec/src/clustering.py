import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv('donnees-defi-egc.csv')

coordonnees = df[['coord_x', 'coord_y']].values

max = 0
nb_clusters = 0

'''for i in range(100, 500, 50):
    kmeans = KMeans(n_clusters=i, random_state=42)

    kmeans.fit(coordonnees)

    clusters = kmeans.labels_

    score = silhouette_score(coordonnees, clusters)
    print(f'Indice de silhouette pour {i} clusters : {score}')
    
    if score > max:
        max = score
        nb_clusters = i
        
print(f'Le meilleur score est {max} pour {nb_clusters} clusters')'''

kmeans = KMeans(n_clusters=400, random_state=42)

kmeans.fit(coordonnees)

clusters = kmeans.labels_

score = silhouette_score(coordonnees, clusters)
print(f'Indice de silhouette pour 400 clusters : {score}')


df['cluster'] = clusters

plt.scatter(df['coord_x'], df['coord_y'], c=df['cluster'], cmap='viridis', s=10)
plt.title('Résultats du clustering K-Means')
plt.xlabel('Coordonnée x')
plt.ylabel('Coordonnée y')
plt.show()

# Supprimer les colonnes 'coord_x' et 'coord_y'
df = df.drop(columns=['coord_x', 'coord_y'])

# Réorganiser les colonnes pour mettre 'cluster' à l'emplacement initial de 'coord_x' et 'coord_y'
col_index = df.columns.get_loc('cluster')  # Récupérer l'index actuel de la colonne 'cluster'
cols = df.columns.tolist()  # Liste des colonnes actuelles
cluster_col = cols.pop(col_index)  # Retirer la colonne 'cluster' de sa position actuelle
# Insérer 'cluster' à la place des colonnes 'coord_x' et 'coord_y'
cols.insert(27, cluster_col)  # Ici 0 est l'index où se trouvaient les coordonnées (1er et 2ème)

# Réorganiser le DataFrame avec la nouvelle liste des colonnes
df = df[cols]

df.to_csv('resultats_kmeans.csv', index=False)


