import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.datasets import make_moons
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_circles

# 1. step1
X, y = make_moons(n_samples=400, noise=0.1, random_state=10)
plt.scatter(X[:, 0], X[:, 1])
plt.savefig('assets/img/dbscan_step1.png')
plt.clf()

def cluster_result(X, y, title, filename):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green', marker='o', s=40, label='Cluster_1')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='red', marker='s', s=40, label='Cluster_2')
    plt.title(title)
    plt.legend()
    plt.savefig(filename)
    plt.clf()

# 2. kmeans
km = KMeans(n_clusters=2, random_state=10)
y_km = km.fit_predict(X)
cluster_result(X, y_km, title='k-means', filename='assets/img/dbscan_kmeans.png')

# 3. dbscan
db = DBSCAN(eps=0.2, min_samples=15, metric='euclidean')
y_db = db.fit_predict(X)
cluster_result(X, y_db, title='DBSCAN', filename='assets/img/dbscan_dbscan.png')

def vis_cluster_plot(clusterobj, dataframe, label_name, filename, iscenter=True):
    if iscenter:
        centers = clusterobj.cluster_centers_

    unique_labels = np.unique(dataframe[label_name].values)
    markers = ['o', 's', '^', 'x', '*']
    isNoise = False

    for label in unique_labels:
        label_cluster = dataframe[dataframe[label_name] == label]
        if label == -1:
            cluster_legend = 'Noise'
            isNoise = True
        else:
            cluster_legend = 'Cluster ' + str(label)

        marker_idx = int(label) % len(markers)
        plt.scatter(
            x=label_cluster['trans1'], y=label_cluster['trans2'], s=70,
            edgecolor='k', marker=markers[marker_idx], label=cluster_legend
        )

        if iscenter and label != -1:
            center_x_y = centers[label]
            plt.scatter(
                x=center_x_y[0], y=center_x_y[1], s=250, color='white',
                alpha=0.9, edgecolor='k', marker=markers[marker_idx]
            )
            plt.scatter(
                x=center_x_y[0], y=center_x_y[1], s=70, color='k',
                edgecolor='k', marker='$%d$' % label
            )

    legend_loc = 'upper center' if isNoise else 'upper right'
    plt.legend(loc=legend_loc)
    plt.savefig(filename)
    plt.clf()

# 4. circles target
X, y = make_circles(n_samples=1000, shuffle=True, noise=0.05, random_state=0, factor=0.5)
clusterDF = pd.DataFrame(data=X, columns=['trans1', 'trans2'])
clusterDF['target'] = y
vis_cluster_plot(None, clusterDF, 'target', filename='assets/img/dbscan_circles_target.png', iscenter=False)

# 5. circles kmeans
kmeans = KMeans(n_clusters=2, max_iter=100, random_state=0)
kmeans_labels = kmeans.fit_predict(X)
clusterDF['kmeans_cluster'] = kmeans_labels
vis_cluster_plot(kmeans, clusterDF, 'kmeans_cluster', filename='assets/img/dbscan_circles_kmeans.png', iscenter=True)

# 6. circles dbscan
dbscan = DBSCAN(eps=0.2, min_samples=15, metric='euclidean')
dbscan_labels = dbscan.fit_predict(X)
clusterDF['dbscan_cluster'] = dbscan_labels
vis_cluster_plot(dbscan, clusterDF, 'dbscan_cluster', filename='assets/img/dbscan_circles_dbscan.png', iscenter=False)
