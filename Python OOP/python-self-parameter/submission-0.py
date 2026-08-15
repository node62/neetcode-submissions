class SuperHero:
    def __init__(buster, name: str, power: str, strength: int):
        buster.name = name
        buster.power = power
        buster.strength = strength
    
    def power_boost(buster, strength_increase) -> None:
        buster.strength += strength_increase
        print(f"{buster.name}'s strength increased to {buster.strength}!")



# Don't modify the following code
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

ironman.power_boost(15)
