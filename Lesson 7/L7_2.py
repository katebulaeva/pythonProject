class Clothes:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def square_coat(self):
        return self.w / 6.5 + 0.5

    def square_jecket(self):
        return self.h * 2 + 0.3

    @property
    def square_full(self):
        return round(self.w / 6.5 + 0.5) + (self.h * 2 + 0.3)


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.w / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_j}'

coat = Coat(1, 2)
jacket = Jacket(2, 1)

print(coat.square_full + jacket.square_full)

