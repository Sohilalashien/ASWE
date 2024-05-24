"Singleton Concept Sample Code"
class Logger:
    "The Singleton Class"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialization code can go here
        return cls._instance

    def log(self, message):
        print(message)

# client
logger1 = Logger()
logger2 = Logger()

# test if logger1=logger2
logger1.log("Hello from logger1")  
logger2.log("Hello from logger2")  

print(logger1 == logger2)  
