from abc import ABC, abstractmethod

# Component interface
class FileSystemComponent(ABC):
    @abstractmethod
    def list_contents(self):
        pass

# Leaf class
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def list_contents(self):
        print(f"File: {self.name}")

# Composite class
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, component):
        self.contents.append(component)

    def list_contents(self):
        print(f"Directory: {self.name}")
        for component in self.contents:
            component.list_contents()

# Client code
if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    directory1 = Directory("Folder 1")
    directory1.add(file1)
    directory1.add(file2)

    directory2 = Directory("Folder 2")
    directory2.add(file3)

    root = Directory("Root")
    root.add(directory1)
    root.add(directory2)

    root.list_contents()
