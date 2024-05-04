# Adaptee class (incompatible interface)
class CelsiusTemperature:
    def get_temperature(self):
        return 25

# Target interface (expected by the client)
class FahrenheitTemperatureInterface:
    def get_temperature(self):
        pass

# Adapter class
class Adapter(FahrenheitTemperatureInterface):
    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature

    def get_temperature(self):
        # Convert Celsius to Fahrenheit
        return (self.celsius_temperature.get_temperature() * 9/5) + 32

# Client code
def display_temperature(temperature):
    print(f"Temperature: {temperature.get_temperature()}°F")

if __name__ == "__main__":
    celsius_temperature = CelsiusTemperature()
    adapter = Adapter(celsius_temperature)
    display_temperature(adapter)
