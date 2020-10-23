from Task1.car import car
from Task1.auto import Auto

def main():
    car1 = car("Ferrari", 320, 100)
    car2 = car("Bentley", 280, 2500)
    car3 = car("Lada Calina", 130, 10000)
    print(car1, ", ",  car2, ", ", car3)
    auto1 = Auto("red", 154, "ferrari")
    auto2 = Auto("green", 232, "bmw")

    print(auto2.get_color())
    auto2.set_color("black")
    print(auto2.get_color())
    print(auto2)
    auto1.increase_speed(76)
    print(auto1)

main()


