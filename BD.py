import csv


# Открываем файл laptop_price.csv и считываем данные с него
def getDataSet():
    with open('laptop_price.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        DataSet = []
        for row in spamreader:
            DataSet.append(row)
        del DataSet[0]
        return DataSet


# Метод возвращающий уникальные значения
def unic(choice):
    with open('laptop_price.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        DataSet = []
        for row in spamreader:
            if row[choice] not in DataSet:
                DataSet.append(row[choice])
        del DataSet[0]
        return DataSet
