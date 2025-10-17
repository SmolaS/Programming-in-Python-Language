class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration
        self.count += 1
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


# Test
for num in Fibonacci(10):
    print(num)
