class Car:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Car:", self.name)

c1 = Car("BMW")
c1.show()
