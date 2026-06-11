import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

imp = [0.31303771, 0.29685569, 0.22213184, 0.16797476]
columns = ['무게_g', '길이_cm', '색상', '당도']

plt.figure()
plt.bar(range(len(imp)), imp)
plt.xticks(range(len(imp)), columns, rotation=90)
plt.savefig('c:/Users/user/Desktop/taesub0204.github.io/assets/img/rf_feature_importances.png')
plt.close()
