from entity import Entity
from random import randint

class Troll(Entity):
    def __init__(self) -> None:
        """
        Initializes the name and random hp of the Entity
        """
        super().__init__(name='Troll', hp=randint(10, 14))

    def melee_attack(self, enemy):
        """
        Implements the abstract method and attacks the given enemy
        Parameters:
            enemy (Entity): target of attack
        Returns"
            (srt): Message of the attack
        """
        rand_dmg = randint(8, 12)
        enemy.take_dmg(rand_dmg)

        return f'{self.name} hits {enemy.name} for {rand_dmg} damage.'
