class Vehicle :
    # properties
    def __init__(self, v_brand, v_model, v_color, average):
        self.brand = v_brand
        self.model = v_model
        self.color = v_color
        self.average = average

    # Functionality
    def __repr__(self):
        return f"I own {self.brand} : {self.model} of {self.color} color. Average : {self.average}kmph"

    def engine(self):
        return f"{self.brand} have good engine qualtiy."


class ElectricVehicle(Vehicle):
    def __init__(self, v_brand, v_model, v_color, average, battery):
        super().__init__(v_brand, v_model, v_color, average)
        self.battery = battery



car = Vehicle("Toyota", "Fortuner", "White", 15)
print(car.engine())

bike = Vehicle("Honda", "Activa 5G", "Metallic Grey",30)
print(bike)

ev = ElectricVehicle("Tata", "Nexon", "Black", "15", "EV")
print(ev)