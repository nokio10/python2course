
## Автомобиль

#Описать класс Car

class Car:
    def __init__(self, gas = 0, capacity = 0, gas_per_100km = 0, mileage = 0):
        # heads-орел/tails-решка
        self.gas = gas
        self.capacity = capacity
        self.gas_per_100km = gas_per_100km
        self.mileage = mileage

    def fill(self, fillup) -> float:
        if (self.gas + fillup) > self.capacity:
            print("Вылито на асфальт ", self.gas + fillup - self.capacity, " литров")
            self.gas = self.capacity
        else:
            self.gas = self.gas + fillup

    def ride(self, km) -> float:
        goup = self.gas / self.gas_per_100km * 100
        if goup < km:
            self.mileage = self.mileage + goup
            print("Вы проехали ", goup, "км, дальше пешочком ", km - goup, "км до заправки,господин")
            self.gas = self.gas - (goup / 100 * self.gas_per_100km)
        else:
            self.mileage += km
            print("Вы проехали ", km, " км")
            self.gas = self.gas - (km / 100 * self.gas_per_100km)


    def info(self):
        print("Бензина в баке: ", self.gas, " литров")
        print("Вместимость бака: ", self.capacity, " литров")
        print("Расход топлива: ", self.gas_per_100km, " л/100км")
        print("Пробег: ", self.mileage)
        # Значит должны быть значения по умолчанию
car1 = Car(10, 60, 9.5, 1000)
car1.fill(50)
car1.info()
car1.ride(700)
car1.info()
car1.fill(30)
car1.info()
car1.ride(200)
car1.info()
car1.ride(200)
car1.info()