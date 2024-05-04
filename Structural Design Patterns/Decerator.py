from abc import ABC, abstractmethod

# Component interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 1.0

    def description(self) -> str:
        return "Simple coffee"

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()

# Concrete decorators
class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.5

    def description(self) -> str:
        return self._coffee.description() + ", milk"

class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 0.2

    def description(self) -> str:
        return self._coffee.description() + ", sugar"

# Client code
def main():
    coffee = SimpleCoffee()
    print(f"Cost: ${coffee.cost()}, Description: {coffee.description()}")

    coffee_with_milk = Milk(coffee)
    print(f"Cost: ${coffee_with_milk.cost()}, Description: {coffee_with_milk.description()}")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print(f"Cost: ${coffee_with_milk_and_sugar.cost()}, Description: {coffee_with_milk_and_sugar.description()}")

if __name__ == "__main__":
    main()
