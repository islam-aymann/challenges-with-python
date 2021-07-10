from math import sqrt


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        return [[i, t] for i in self.ingredients for t in self.toppings]


def find_roots(a, b, c):
    d = sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)

    return x1, x2


if __name__ == '__main__':
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(
        machine.scoops()
    )  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]

    print(find_roots(2, 10, 8))
