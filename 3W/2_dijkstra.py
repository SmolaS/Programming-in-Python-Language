import matplotlib.pyplot as plt

def dijkstra(graf, start):
    odleglosci = {w: float('inf') for w in graf}
    poprzednik = {w: None for w in graf}
    odleglosci[start] = 0
    odwiedzone = set()

    while len(odwiedzone) < len(graf):
        obecny = None
        for wierzcholek in graf:
            if wierzcholek not in odwiedzone:
                if obecny is None or odleglosci[wierzcholek] < odleglosci[obecny]:
                    obecny = wierzcholek

        if obecny is None:
            break

        odwiedzone.add(obecny)

        for sasiad, waga in graf[obecny].items():
            nowa_odleglosc = odleglosci[obecny] + waga
            if nowa_odleglosc < odleglosci[sasiad]:
                odleglosci[sasiad] = nowa_odleglosc
                poprzednik[sasiad] = obecny

    return odleglosci, poprzednik


graf = {
    'A': {'B': 4, 'C': 5},
    'B': {'A': 4, 'C': 2, 'D': 7},
    'C': {'A': 5, 'B': 2, 'D': 1, 'E': 6},
    'D': {'B': 7, 'C': 1, 'E': 3},
    'E': {'C': 6, 'D': 3}
}

dist, prev = dijkstra(graf, 'A')
cel = 'E'

sciezka = []
v = cel
while v is not None:
    sciezka.insert(0, v)
    v = prev[v]

pos = {
    'A': (0, 1.5),
    'B': (-1.5, 0.5),
    'C': (1.5, 0.5),
    'D': (0, -0.5),
    'E': (0, -1.5)
}

plt.figure()

for a, sasiedzi in graf.items():
    x1, y1 = pos[a]
    for b, w in sasiedzi.items():
        x2, y2 = pos[b]
        plt.plot([x1, x2], [y1, y2], 'lightgray')
        plt.text((x1+x2)/2, (y1+y2)/2, str(w), color='gray', ha='center')

for i in range(len(sciezka)-1):
    a, b = sciezka[i], sciezka[i+1]
    x1, y1 = pos[a]
    x2, y2 = pos[b]
    plt.plot([x1, x2], [y1, y2], 'r', linewidth=2.5)

for w, (x, y) in pos.items():
    color = 'salmon' if w in sciezka else 'skyblue'
    plt.scatter(x, y, s=600, color=color)
    plt.text(x, y, w, ha='center', va='center')

plt.title("Ścieżka z A do E: " + " → ".join(sciezka))
plt.axis('off')
plt.show()
