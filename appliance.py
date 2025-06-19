class Appliance:
    def __init__(self, brand, powerConsumption):
        self.brand = brand
        self.powerConsumption = powerConsumption

    def show_details(self):
        return f"Brand: {self.brand}, Power Consumption: {self.powerConsumption}W"

class Fan(Appliance):
    def __init__(self, brand, powerConsumption, blades):
        super().__init__(brand, powerConsumption)
        self.blades = blades

    def show_details(self):
        return f"{super().show_details()}, Blades: {self.blades}"

class AC(Appliance):
    def __init__(self, brand, powerConsumption, tonnage):
        super().__init__(brand, powerConsumption)
        self.tonnage = tonnage

    def show_details(self):
        return f"{super().show_details()}, Tonnage: {self.tonnage} Ton"

class Heater(Appliance):
    def __init__(self, brand, powerConsumption, heatingType):
        super().__init__(brand, powerConsumption)
        self.heatingType = heatingType

    def show_details(self):
        return f"{super().show_details()}, Heating Type: {self.heatingType}"


fan = Fan("Usha", 75, 3)
ac = AC("LG", 1500, 1.5)
heater = Heater("Bajaj", 2000, "Infrared")

print(fan.show_details())
print(ac.show_details())
print(heater.show_details())
