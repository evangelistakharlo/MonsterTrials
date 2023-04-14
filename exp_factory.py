from enemy_factory import EnemyFactory
from goblin import Goblin
from ogre import Ogre
from troll import Troll
from random import choice

class ExpertFactory(EnemyFactory):
    def create_random_enemy(self):
        """ 
        Gets a random enemy between Goblin, Ogre, and Troll
        Returns:
            (Entity): Random enemy
        """
        return choice([Goblin(), Ogre(), Troll()])