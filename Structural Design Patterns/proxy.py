from abc import ABC, abstractmethod

# Subject interface
class Subject(ABC):
    """
    Subject is an interface that both RealSubject and Proxy implement. 
    It defines a request method that must be implemented by both classes.
    """
    @abstractmethod
    def request(self) -> None:
        pass

# RealSubject class
class RealSubject(Subject):
    """
    RealSubject is a class that contains the actual implementation of the request method. 
    This class performs the core business logic.
    """
    def request(self) -> None:
        print("RealSubject: Handling request.")

# Proxy class
class Proxy(Subject):
    """
    Proxy is a class that acts as a proxy for RealSubject.
    It has a reference to a RealSubject object and controls access to it. 
    The request method in Proxy first checks access, 
    then delegates the request to the RealSubject if access is allowed.
    """
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The request method of Proxy checks access before delegating the request to the RealSubject 
        and logs the access time.
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        """
        Check access before allowing the request to be forwarded to the real subject.
        """
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        """
        Log the time of request.
        """
        print("Proxy: Logging the time of request.", end="")

# Client code
def client_code(subject: Subject) -> None:
    """
    The client code demonstrates how the client can work with both RealSubject
    and Proxy objects interchangeably through the Subject interface.
    """
    subject.request()

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
