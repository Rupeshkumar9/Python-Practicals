
print("--- 1. Absolute Import Example ---")

 # Absolute import: Specifying the full path from the project root
import shapes.circle
    
# We have to use the full namespace here
c1 = shapes.circle.Circle(0, 0, 5)
print(f"Created via absolute import: {c1}")
print(f"Area: {c1.area():.2f}")
print(f"Perimeter: {c1.perimeter():.2f}\n")


print("--- 2. Package-Level Import (using __init__.py logic) ---")
# This relies on the code inside shapes/__init__.py
# The __init__.py uses RELATIVE imports (from .rectangle import Rectangle)
# to expose the class to us here.
from shapes import Rectangle 
    
r1 = Rectangle(4, 6)
print(f"Created via package import: {r1}")
print(f"Area: {r1.area()}")
print(f"Perimeter: {r1.perimeter()}\n")



print("--- 3. Import * Example (using __all__) ---")
# This pulls in ONLY 'Circle' and 'Rectangle' as defined in shapes/__init__.py
from shapes import *
    
# Point is NOT imported because it was not in __all__
try:
    p = Point(1, 2)
except NameError:
    print("Success: 'Point' class was correctly hidden by __all__.")
    
c2 = Circle(2, 2, 10)
print(f"Created via import *: {c2}")







