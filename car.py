class Car:
    wheels = 4
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Wheels:", Car.wheels)
    def start(self):
        print(self.brand, "car is starting...")
    @classmethod
    def change_wheels(cls, w):
        cls.wheels = w
        print("Wheels changed to", cls.wheels)
    @staticmethod
    def check_speed(speed):
        if speed <= 100:
            print("Speed is safe")
        else:
            print("Speed limit exceeded")

car1 = Car("Toyota", "Innova", 2500000)
car1.display()
car1.start()

Car.change_wheels(6)

Car.check_speed(80)
Car.check_speed(120)
            