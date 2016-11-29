#szimplán a listában szereplő elemeket adja össze a függvény és visszatér ezzel az értékkel
def sum_numbers(numbers_list):
    #"segédváltozó" csak itt használom a függvényen belül, ehhez fogom hozzáadni a listában lévő elemeket
    result = 0
    for number in numbers_list:
        result += number
    return result

#sum_numbers_test
my_numbers = [5,76,23,54,34,4,5]
sum = sum_numbers(my_numbers)
print(sum)

#Az előző függvény összeadja a listában lévő számokat, viszont mi a helyzet, ha csak minden 2.ik vagy 5.ik
#számot akarok összeadni, erre itt egy másik function :)
def sum_some_numbers(numbers_list, number):
    result = 0
    # itt az iterator ha number = 2 akkor ezeket az értékeket fogja felvenni [0,2,4,6,8,10... numbers_list hossza]
    for iterator in range(0,len(numbers_list), number):
        result += numbers_list[iterator]
    return result

#sum_some_numbers test
my_numbers = [5,76,23,54,34,4,5]
sum = sum_some_numbers(my_numbers,3)
print(sum)