# imported from my_module.py
import my_module
my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)


# AN EASIER MORE INTUITIVE WAY OF WRITING CODE
from my_module import greet, flavor

greet("Roger Rabbit")
print("My favorite ice cream flavor is", flavor)