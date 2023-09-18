from random import randint


def attack(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} dealt damage to the enemy {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} dealt damage to the enemy {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} dealt damage to the enemy {5 + randint(-3, -1)}')


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} blocked {10 + randint(5, 10)} damage')
    if char_class == 'mage':
        return (f'{char_name} blocked {10 + randint(-2, 2)} damage')
    if char_class == 'healer':
        return (f'{char_name} blocked {10 + randint(2, 5)} damage')


def special(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} used the special skill «endurance {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} used the special skill «attack {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} used the special skill «defence {10 + 30}»')


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'''{char_name}, you are a warrior -
an excellent melee fighter.''')
    if char_class == 'mage':
        print(f'''{char_name}, you are a magician -
an excellent tamer of the elements.''')
    if char_class == 'healer':
        print(f'''{char_name}, you are a healer - a sorcerer
who can heal wounds.''')
    print('practice managing your skills.')
    print('''enter on of the commands:
attack - to attack the enemy,
defence — to block the enemy"s attack or
special — to use your superpower.''')
    print('If you don"t want to practice, use skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('enter the command: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'training is over.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Enter character name:warrior, mage, healer: ')
        if char_class == 'warrior':
            print('warrior - strong.')
        if char_class == 'mage':
            print('mage.')
        if char_class == 'healer':
            print('healer.')
        approve_choice = input('''
press (Y), to confirm your choise or any other button
to choose another character ''').lower()
    return char_class


def main():
    print('Hello, adventurer!')
    print('Before you start...')
    char_name = input('...introduce yourself: ')
    print(f'Hello, {char_name}! '
          'Now your endurance — 80, attack — 5 and defense — 10.')
    print('You can choose one of three power paths:')
    print('worrior, mage, healer')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
