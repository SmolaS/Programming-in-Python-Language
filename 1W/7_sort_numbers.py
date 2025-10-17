import random

N = 10
numbers = []
for i in range(N):
    liczba = random.randint(0, 100)
    numbers.append(liczba)

print("Wylosowane liczby:", numbers)

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > klucz:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
    return lista

numbers_selection = numbers[:] 
numbers_insertion = numbers[:]

print("Po sortowaniu (Selection Sort):", selection_sort(numbers_selection))
print("Po sortowaniu (Insertion Sort):", insertion_sort(numbers_insertion))
