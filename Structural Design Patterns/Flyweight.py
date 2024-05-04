class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, unique_state):
        print(f"Shared: {self.shared_state}, Unique: {unique_state}")

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = ConcreteFlyweight(shared_state)
        return self.flyweights[shared_state]

def main():
    factory = FlyweightFactory()

    flyweight1 = factory.get_flyweight("shared_state_1")
    flyweight1.operation("unique_state_1")

    flyweight2 = factory.get_flyweight("shared_state_1")
    flyweight2.operation("unique_state_2")

    flyweight3 = factory.get_flyweight("shared_state_2")
    flyweight3.operation("unique_state_3")

if __name__ == "__main__":
    main()
