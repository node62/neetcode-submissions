class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    @property 
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, n):
        if n in range(0, 101):
            self.__health = n
        elif n > 100:
            print("You can't set the health to more than 100")
        else:
            print("You can't set the health to less than 0")
    
    @property
    def power_level(self):
        return self.__power_level
    
    @power_level.setter
    def power_level(self, n):
        if n in range(1, 11):
            self.__health = n
        elif n > 10:
            print("You can't set the power level to more than 10")
        else:
            print("You can't set the power level to less than 1")

# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power_level) # this should print 9
super_hero.power_level = 100 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1


# TODO: print the hero's attributes 
print(
    f'{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level'
)
