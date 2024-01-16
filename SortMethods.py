from BD import unic


def sortByCompany(arr, choice):
    newArr = []
    for el in arr:
        if el[1] == choice:
            newArr.append(el)
    return newArr


def sortByTypeName(arr, choice):
    newArr = []
    for el in arr:
        if el[3] == choice:
            newArr.append(el)
    return newArr


def sortByInches(arr, choice):
    newArr = []
    for el in arr:
        if el[4] == choice:
            newArr.append(el)
    return newArr


def sortByScreenResolution(arr, choice):
    newArr = []
    for el in arr:
        if el[5] == choice:
            newArr.append(el)
    return newArr


def sortByRam(arr, choice):
    newArr = []
    for el in arr:
        if el[7] == choice:
            newArr.append(el)
    return newArr


def sortByMemory(arr, choice):
    newArr = []
    for el in arr:
        if el[8] == choice:
            newArr.append(el)
    return newArr


def sortByOpSys(arr, choice):
    newArr = []
    for el in arr:
        if el[10] == choice:
            newArr.append(el)
    return newArr


def sortByWeight(arr, choice):
    newArr = []
    for el in arr:
        weight = float(el[11].replace("kg", ""))
        if weight < 1.0 and choice == 'Меньше 1 килограмма':
            newArr.append(el)
        elif weight < 1.5 and choice == 'Меньше 1,5 килограмм':
            newArr.append(el)
        elif weight < 2.0 and choice == 'Меньше 2 килограмм':
            newArr.append(el)
        elif weight < 2.5 and choice == 'Меньше 2,5 килограмма':
            newArr.append(el)
        elif weight < 3.0 and choice == 'Меньше 3 килограмм':
            newArr.append(el)
    return newArr


def sortByPrice(arr, choice):
    newArr = []
    for el in arr:
        price = float(el[12]) * 100
        if price < 50000 and choice == 'Меньше 50000 руб':
            newArr.append(el)
        elif price < 100000 and choice == 'Меньше 100000 руб':
            newArr.append(el)
        elif price < 150000 and choice == 'Меньше 150000 руб':
            newArr.append(el)
        elif price < 200000 and choice == 'Меньше 200000 руб':
            newArr.append(el)
        elif price < 250000 and choice == 'Меньше 250000 руб':
            newArr.append(el)
        elif price >= 250000 and choice == 'Больше 250000 руб':
            newArr.append(el)
    return newArr