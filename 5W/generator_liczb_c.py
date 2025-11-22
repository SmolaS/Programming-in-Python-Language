def generator_liczb(n):
    for i in range(1, n + 1):
        print(f"Generuje: {i}")
        yield i

for liczba in generator_liczb(5):
    print("Uzyskana:", liczba)
