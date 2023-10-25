class Car:
    # Class variable to keep track of the number of cars created
    car_count = 0

    def init(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.engine_status = "off"
        Car.car_count += 1

    def start(self):
        if self.engine_status == "off":
            self.engine_status = "on"
            return f"{self.color} {self.model} has started."
        else:
            return "The car is already running."

    def stop(self):
        if self.engine_status == "on":
            self.engine_status = "off"
            return f"{self.color} {self.model} has stopped."
        else:
            return "The car is already stopped."

    def accelerate(self):
        if self.engine_status == "on":
            return f"{self.color} {self.model} is accelerating."
        else:
            return "Cannot accelerate when the car is not running."

    @staticmethod
    def count_cars():
        return f"Total number of cars created: {Car.car_count}"

# Example usage:
car1 = Car("Toyota", "Red", 25000)
car2 = Car("Honda", "Blue", 30000)

print(car1.start())
print(car1.accelerate())
print(car1.stop())

print(car2.start())
print(car2.accelerate())

print(Car.count_cars())
