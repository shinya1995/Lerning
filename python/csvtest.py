import csv

file = open('new.csv','w')
w = csv.writer(file)
w.writerow(['a','a','a'])
w.writerows([['a','a','a'],['a','a','a'],['a','a','a']])

file.close()