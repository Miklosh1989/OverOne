class car:
    def __init__(self, name, speed, rally):
        self.name = name
        self.speed = speed
        self.rally = rally

    def __str__(self):
        return f'тачка - {self.name}, максмальная скорость - {self.speed}, с автопробегом {self.rally}'

    def ride_ability(self):
        if self.rally >= 1000:
            print("Не годен для эксплуатации")
        else:
            print("Можно ехать")

    def speedrun(self):
        if self.speed > 180:
            print("Ракета")
        else:
            print("Корыто")

