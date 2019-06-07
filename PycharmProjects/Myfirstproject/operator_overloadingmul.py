class mulover:

    def __init__(self, a):
        self.a = a

    def __mul__(self, other):
        a = self.a + other.a
        return a

number_a = mulover(3)

number_b = mulover(4)

print(number_a * number_b)
