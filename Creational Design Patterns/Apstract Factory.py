#!/usr/bin/env python
# coding: utf-8

# In[2]:


"The Abstract Factory Interface"
from abc import ABCMeta, abstractmethod
class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract Furniture Factory Interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "The static Abstract factory interface method"

class FurnitureFactory(IFurnitureFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_furniture(furniture):
        "Static get_factory method"
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory.get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory.get_table(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None

class ChairFactory:  
    "The Factory Class"

    @staticmethod
    def get_chair(chair):
        "A static method to get a chair"
        try:
            if chair == 'BigChair':
                return BigChair()
            if chair == 'MediumChair':
                return MediumChair()
            if chair == 'SmallChair':
                return SmallChair()
            raise Exception('Chair Not Found')
        except Exception as _e:
            print(_e)
        return None

"The Chair Interface"
class IChair(metaclass=ABCMeta):
    "The Chair Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"

"A Class of Chair"
class SmallChair(IChair):
    "The Small Chair Concrete Class implements the IChair interface"

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

"A Class of Chair"
class MediumChair(IChair):
    """The Medium Chair Concrete Class implements the IChair interface"""

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

"A Class of Chair"
class BigChair(IChair):
    "The Big Chair Concrete Class that implements the IChair interface"

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


"The Factory Class"
class TableFactory:
    "The Factory Class"

    @staticmethod
    def get_table(table):
        "A static method to get a table"
        try:
            if table == 'BigTable':
                return BigTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()
            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None

"The Table Interface"
from abc import ABCMeta, abstractmethod

class ITable(metaclass=ABCMeta):
    "The Table Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"

"A Class of Table"
class SmallTable(ITable):
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

"A Class of Table"
class MediumTable(ITable):
    "The Medium Table Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 110
        self._depth = 70

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

"A Class of Table"
class BigTable(ITable):
    "The Big Chair Concrete Class implements the ITable interface"

    def __init__(self):
        self._height = 60
        self._width = 120
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

"Abstract Factory Use Case Example Code"
FURNITURE = FurnitureFactory.get_furniture("SmallChair")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory.get_furniture("MediumTable")
print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")


# In[ ]:




