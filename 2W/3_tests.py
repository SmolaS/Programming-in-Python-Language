import random
import time
import matplotlib.pyplot as plt
from sort_2 import parallel_sort

if __name__ == "__main__":
    rozmiary = [100000, 1000000, 10000000]
    liczby_procesow = [1, 2, 4, 8]
    wyniki = {}

    for rozmiar in rozmiary:
        dane = [random.randint(0, 1000000) for _ in range(rozmiar)]
        czasy = []

        print(f"\nTest dla {rozmiar} elementów:")
        for p in liczby_procesow:
            start = time.time()
            parallel_sort(dane, procesy=p)
            end = time.time()
            czas = end - start
            czasy.append(czas)
            print(f"Procesy: {p}, Czas: {czas:.4f} s")

        wyniki[rozmiar] = czasy

    for rozmiar, czasy in wyniki.items():
        plt.plot(liczby_procesow, czasy, marker='o', label=f"rozmiar={rozmiar}")

    plt.xlabel("Liczba procesów")
    plt.ylabel("Czas [s]")
    plt.title("Porównanie czasu sortowania równoległego")
    plt.legend()
    plt.grid(True)
    plt.show()
