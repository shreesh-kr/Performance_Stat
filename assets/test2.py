import csv
import numpy as np

path = '/home/shreesh/Project/Performance-Stat/assets/data.csv'

file = open(path, 'r')
csv_file = csv.reader(file)


date = []
true = []
false = []

for row in csv_file:
  date.append(row[0])
  true.append(int(row[1]))
  false.append(int(row[2]))
    

date = np.array(date)
true = np.array(true)
false = np.array(false)

number_of_days = len(date)
true_avg = int(np.mean(true))
false_avg = int(np.mean(false))
max_true = np.max(true)
max_false = np.max(false)
max_true_day = np.argmax(true, axis=0)
max_false_day = np.argmax(false, axis=0)

report = f'''
Average task performed during the period of {number_of_days} days is {true_avg}.
Average task's not performed during the period of {number_of_days} days is {false_avg}.
Maximum performing day was {max_true_day} with {max_true} task's performed.
Least performing day was {max_false_day} with {max_false} task's not performed.

Day 1 of observation is {date[0]}, Last day of observation is {date[-1]}.
'''

print(report)