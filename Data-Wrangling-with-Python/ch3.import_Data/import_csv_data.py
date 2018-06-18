#-*- coding: utf-8 -*-

import csv

csvdocu = open('data-text.csv','rb')
reader = csv.reader(csvdocu)

for row in reader :
    print row 
    