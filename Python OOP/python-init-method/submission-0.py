class Pet:
    # TODO: Implement the __init__ method here
    def __init__(slef, n, s, a):
        slef.name = n
        slef.species = s
        slef.age = a


# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")
