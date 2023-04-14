from enemy_factory import EnemyFactory

from easy_goblin import EasyGoblin
from easy_ogre import EasyOgre
from easy_troll import EasyTroll
from random import choice

class BeginnerFactory(EnemyFactory):
    def create_random_enemy(self):
        """ 
        Gets a random enemy between EasyGoblin, EasyOgre, and EasyTroll
        Returns:
            (Entity): Random enemy
        """
        return choice([EasyGoblin(), EasyOgre(), EasyTroll()])