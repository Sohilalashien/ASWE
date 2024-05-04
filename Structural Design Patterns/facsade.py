# facsade
class Engine:
    def __init__(self):
        self.speed = 0

    def start(self):
        print("Engine started")
        self.speed = 100

    def stop(self):
        print("Engine stopped")
        self.speed = 0

class Lights:
    def turn_on(self):
        print("Lights on")

    def turn_off(self):
        print("Lights off")

# Facade
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()

    def start_car(self):
        self.lights.turn_on()
        self.engine.start()

    def stop_car(self):
        self.engine.stop()
        self.lights.turn_off()

# Client code
def main():
    car = CarFacade()
    car.start_car()
    # Do something
    car.stop_car()

if __name__ == "__main__":
    main()
