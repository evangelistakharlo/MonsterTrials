from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, name, hp):
        """
        Initializes the name and hp of an entity
        """
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        """
        Getter property for the name
        Returns:
            _name (str)
        """
        return self._name
    
    @property
    def hp(self):
        """
        Getter property for the hp
        Returns:
            _hp (int)
        """
        return self._hp
    
    def take_dmg(self, dmg):
        """
        Allows the entity to take damage and subtract it from its hp
        Parameters:
            dmg (int): The damage to take
        """
        self._hp -= dmg

        if self.hp < 0:
            self._hp = 0

    def __str__(self):
        """
        Returns the string representation of the class
        Returns:
            (str): name and hp
        """
        return f"{self.name} HP: {self.hp}"
    
    @abstractmethod
    def melee_attack(self, enemy):
        """
        Allows the entity to perform a melee attack. This is abstract to be implemented by subclasses.
        """
        pass