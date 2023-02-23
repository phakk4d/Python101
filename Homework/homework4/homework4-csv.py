import csv

def writecsv(datalist):
    with open('homework4-data.csv', 'a', encoding = 'utf-8', newline = '') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)



data = []
writecsv(data)