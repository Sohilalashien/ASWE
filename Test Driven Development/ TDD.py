#!/usr/bin/env python
# coding: utf-8

# In[45]:


import unittest


# In[51]:


import math

def add(a, b):
    pass

def subtract(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def power(a, b):
    pass

def square_root(a):
    pass


# In[52]:


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(divide(3, 1), 3)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)


# In[53]:


suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
unittest.TextTestRunner().run(suite)


# In[59]:


import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return math.sqrt(a)


# In[60]:


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertNotEqual(add(3, 5), 7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertNotEqual(subtract(5, 3), 3)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertNotEqual(multiply(3, 5), 12)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertNotEqual(divide(10, 2), 4)
        self.assertAlmostEqual(divide(1, 3), 0.33333, places=5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertNotEqual(power(2, 3), 7)
        self.assertAlmostEqual(power(2, 0.5), 1.41421, places=5)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        self.assertNotEqual(square_root(9), 4)
        self.assertAlmostEqual(square_root(2), 1.41421, places=5)
        with self.assertRaises(ValueError):
            square_root(-1)


# In[61]:


# Create a test suite
suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)

# Run the test suite
unittest.TextTestRunner().run(suite)


# In[ ]:


#Refactor
def add(a, b):
    return a + b

def add(*args):
    return sum(args)

