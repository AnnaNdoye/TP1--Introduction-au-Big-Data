import matplotlib.pyplot as plt
import csv

sizes = []
averages = []
with open('results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    for row in reader:
        sizes.append(int(row[0]))
        averages.append(float(row[6]))

plt.figure(figsize=(10, 6))
plt.plot(sizes, averages, marker='o', linestyle='-', color='b')
plt.title('Temps d\'exécution moyen en fonction de la taille d\'entrée')
plt.xlabel('Taille d\'entrée (MB)')
plt.ylabel('Temps d\'exécution moyen (secondes)')
plt.grid(True)
plt.savefig('plot.png')
plt.show()
print('Plot saved as plot.png')
