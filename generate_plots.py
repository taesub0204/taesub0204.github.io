import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import os

os.makedirs('c:/Users/user/Desktop/taesub0204.github.io/assets/img', exist_ok=True)

data = {
    '종류': ['수박']*10 + ['참외']*5,
    '무게': [2000, 2500, 1800, 1500, 900, 2500, 2250, 1860, 2100, 1500, 500, 400, 450, 400, 600],
    '길이': [30.0, 25.0, 20.0, 16.0, 10.0, 33.0, 23.0, 17.0, 21.0, 17.0, 8.0, 7.5, 5.0, 4.5, 8.5]
}
df = pd.DataFrame(data)

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

X = np.column_stack((df['무게'], df['길이']))
y = df['종류']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=40)

plt.figure()
plt.scatter(X_train[:,0], X_train[:,1])
plt.scatter(1000, 15, marker='o')
plt.xlabel('무게')
plt.ylabel('길이')
plt.savefig('c:/Users/user/Desktop/taesub0204.github.io/assets/img/knn_12_1.png')
plt.close()

k_list = range(1,12)
accuracies = []
for k in k_list:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    accuracies.append(clf.score(X_test, y_test))

plt.figure()
plt.plot(list(k_list), accuracies)
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('최적의 이웃 값 찾기')
plt.savefig('c:/Users/user/Desktop/taesub0204.github.io/assets/img/knn_13_1.png')
plt.close()
