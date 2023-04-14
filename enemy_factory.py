from abc import ABC, abstractmethod

class EnemyFactory(ABC):
    @abstractmethod
    def create_random_enemy(self):
        ''' Creates a random Entity object. To be implemented by subclasses. '''
        pass