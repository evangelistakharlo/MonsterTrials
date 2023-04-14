from entity import Entity
from random import randint

class EasyTroll(Entity):
    def __init__(self):
        """
        Initializes the name and random hp of the Entity
        """
        super().__init__(name='Easy Troll', hp=randint(6, 9))

    def melee_attack(self, enemy):
        """
        Implements the abstract method and attacks the given enemy
        Parameters:
            enemy (Entity): target of attack
        Returns"
            (srt): Message of the attack
        """
        rand_dmg = randint(5, 9)
        enemy.take_dmg(rand_dmg)

        return f'{self.name} hits {enemy.name} for {rand_dmg} damage.'
