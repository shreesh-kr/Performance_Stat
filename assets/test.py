import matplotlib.pyplot as plt


date = ['29/10/19', '30/10/19', '31/10/19', '01/11/19']
score = [2, 4, 3, 6]
score_2 = [1,3,6,2]
'''pos = [0,1,2,3]
pos_2 = [0.3, 1.3, 2.3, 3.3]
pos_3 = [0.15, 1.15, 2.15, 3.15]
plt.bar(pos, score, width=0.3)
plt.bar(pos_2, score_2, width=0.3)
plt.xticks(pos_3, date)
plt.show()
'''

import csv
import matplotlib.pyplot as plt

# path = os.getcwd()
path = '/home/shreesh/Project/Performance-Stat/assets/data.csv'
#file = 'data.csv'

with open(path, 'r') as csv_file:
    csv_writer = csv.reader(csv_file)
    #print(csv_writer.readrow())
    date = []
    true = []
    false = []
    csv_len = len(list(csv_writer))

    for row in csv_writer:
    	date.append(row[0])
    	true.append(int(row[1]))
    	false.append(int(row[2]))


pos = []
for x in range(csv_len):
    pos.append(x)


pos_2 = []
for x in range(csv_len):
    pos_2.append(x + 0.3)


pos_3 = []
for x in range(csv_len):
    pos_3.append(x+0.15)


plt.bar(pos, true, width=0.3)
plt.bar(pos_2, false, width=0.3)
plt.xticks(pos_3, date)
plt.show()
print(pos)
print(pos_2)
print(pos_3)