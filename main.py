"""
    Name: <>
    Date: <>
    Description: A simple program that simulates a game where a player tries to defeat 3 enemies
"""


from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
from hero import Hero

from random import randint
from check_input import get_int_range

print('Monster Trials\n')

# Get the name of the player
name = input('What is your name? ')

print('\nYou will face a series of 3 monters, ' + name + '.')
print('Defeat them all to win.\n')

# Get choice of difficulty
print('Difficulty:')
print('1. Beginner')
print('2. Expert')
difficulty = get_int_range('>> ', 1, 2)

# Choose the factory
factory = None
if difficulty == 1:
    factory = BeginnerFactory()
elif difficulty == 2:
    factory = ExpertFactory()

# Generate 3 enemy objects
monsters = list()       # List to store enemies
for i in range(3):
    enemy = factory.create_random_enemy()
    monsters.append(enemy)

# Initialzie the player's hero
hero = Hero(name)
# Counter for enemy in list
enemy_count = len(monsters)
# Loop while hero is still alive and there are still an enemy
while hero.hp > 0 and enemy_count > 0:
    # Display and choose from remaining enemies
    print('\nChoose an enemy to attack:')
    for i in range(0, enemy_count):
        print(f'{(i + 1)}. {monsters[i]}')
    # Ask for enemy number
    enemy_choice = get_int_range('>> ', 1, enemy_count)
    # Get enemy from list
    current_enemy = monsters[enemy_choice - 1]
    
    # Choose the attack
    print(f'\n{hero}')
    print('1. Sword Attack')
    print('2. Arrow Attack')
    attack_choice = get_int_range('>> ', 1, 2)
    
    if attack_choice == 1:
        print('\n' + hero.melee_attack(current_enemy))
    elif attack_choice == 2:
        print('\n' + hero.ranged_attack(current_enemy))

    if current_enemy.hp <= 0:
        print('You have slain the ' + current_enemy.name)
        # Remove enemy from list
        monsters.remove(current_enemy)
        enemy_count = len(monsters)

        # Determine if won or not yet
        if enemy_count == 0:
            print('\nCongratulations! You defeated all three monsters!')
            print('Game over.')
    else:
        # Let the enemy attack
        print(current_enemy.melee_attack(hero))

        # Determine if lose or not yet
        if hero.hp == 0:
            print('\nYou have been defeated by the enemies.')
            print('Better luck next time.')