from multiprocessing import Pool
import random

def sortuj_fragment(lista):
    return sorted(lista)

def parallel_sort(dane, procesy=2):
    dlugosc = len(dane)
    rozmiar_czesci = dlugosc // procesy

    fragmenty = []
    for i in range(0, dlugosc, rozmiar_czesci):
        czesc = dane[i:i + rozmiar_czesci]
        fragmenty.append(czesc)

    with Pool(processes=procesy) as p:
        posortowane_fragmenty = p.map(sortuj_fragment, fragmenty)

    wynik = []
    for czesc in posortowane_fragmenty:
        wynik.extend(czesc)

    return sorted(wynik)

if __name__ == "__main__":
    dane = [random.randint(0, 100) for _ in range(20)]
    print("Przed sortowaniem:", dane)
    print("Po sortowaniu:", parallel_sort(dane, procesy=4))
