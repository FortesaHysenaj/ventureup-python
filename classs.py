class Dog:
    
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
dog1 = Dog("Dog1", 7)
dog2 = Dog("Dog2", 4)
dog3 = Dog("Dog3", 5)


# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)


# Output
print("The oldest dog is ",(get_biggest_number(dog1.age, dog2.age, dog3.age))," years old.")