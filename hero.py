from entity import Entity
from random import randint

class Hero(Entity):
    def __init__(self, name):
        """
        Initializes the name of the entity and hp to 25
        """
        super().__init__(name, 25)
    
    def ranged_attack(self, enemy):
        """
        Performs a ranged attack dealing damage between 1-12
        Parameters:
            enemy (Entity) : The target of attack
        Returns:
            (str): Message after the attack
        """
        dmg = randint(1, 12)
        enemy.take_dmg(dmg)

        return f"{self.name} pierces a {enemy.name} with an arrow for {dmg} damage."
    
    def melee_attack(self, enemy):
        """
        Performs a melee attack dealing damage between 1-6
        Parameters:
            enemy (Entity) : The target of attack
        Returns:
            (str): Message after the attack
        """
        dmg = randint(1, 6)
        enemy.take_dmg(dmg)

        return f"{self.name} smashes a {enemy.name} with an hammer for {dmg} damage."