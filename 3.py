import csv
file = open('market.csv')
c = list(csv.reader(file, delimiter = ","))

for i in c:
    print(i[0],"-",i[1], "шт. за ", i[2])
s = sum([int(i[1])*int(i[2]) for i in c])
print("Cумма: ", s)