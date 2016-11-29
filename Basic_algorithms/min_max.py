#a következő két függvényben egy listában lévő számok minimumát és maximumát kereshetjük meg

def find_min(numbers_list):
    # azért kell először megadni min-nek egy nagy számot hogy pl: az első elem 5674353 a listában
    # akkor is változzon ez a minimum érték
    min = 9999999999
    for iterator in range(0, len(numbers_list)):
        if min > numbers_list[iterator]:
            min = numbers_list[iterator]
    return min


def find_max(numbers_list):
    max = -9999999999
    for iterator in range(0, len(numbers_list)):
        if max < numbers_list[iterator]:
            max = numbers_list[iterator]
    return max


my_list = [1231,-345,3453,23453,453,453,453,45,345235,34,53,453,45,345,578689,5456]
minimum = find_min(my_list)
maximum = find_max(my_list)
print("Min: " + str(minimum) + " Max: " + str(maximum))