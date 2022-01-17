import matplotlib.pyplot as plt
import pandas as pd
import csv

with open('C:\\Users\\JJ\\source\\repos\\covid19_project\\covid19_record.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        name = line[1]
        break

plt.style.use('bmh')
df = pd.read_csv('C:\\Users\\JJ\\source\\repos\\covid19_project\\covid19_record.csv')
x=df[name]
y=df['Cases']


plt.xlabel(name, fontsize=18)
plt.ylabel('Cases', fontsize=16)
plt.bar(x,y)


plt.show()
