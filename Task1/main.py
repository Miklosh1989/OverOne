from Task1.car import car

car1 = car("Ferrari", 320, 100)
car2 = car("Bentley", 280, 2500)
car3 = car("Lada Calina", 130, 10000)
print(car1, ", ",  car2, ", ", car3)

print(car1.ride_ability(), ", ", car1.speedrun())
print(car2.ride_ability(), ", ", car2.speedrun())
print(car3.ride_ability(), ", ", car3.speedrun())