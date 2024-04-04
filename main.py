# Этот код демонстрирует применение принципа открытости/закрытости:
# Мы можем легко добавить новые типы оружия, создав классы, наследующие Weapon,
# и реализующие метод 'attack', не изменяя при этом классы 'Fighter', 'Monster'.

from abc import ABC, abstractmethod
# Создаем абстрактный класс 'Weapon', который не имеет
# собственной реализации.
class Weapon(ABC):
    @abstractmethod     # декоратор, который показывает, что метод 'attack' является абстрактным.
    def attack(self):   # Является шаблоном, который должены реализовывать подклассы:
        pass            # сам метод не выполняет никаких действий.

# Создаем класс оружия 'Sword' - Меч по шаблону 'Weapon":
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

# Создаем класс оружия 'Bow' - Лук по шаблону 'Weapon" :
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Создаем класс бойца 'Fighter':
class Fighter():
    def __init__(self):
        self.weapon = None  # Боец 'Fighter' без оружия по умолчанию:

# Функция смены оружия:
    def changeWeapon(self, weapon):
        self.weapon = weapon


    def fight(self):
        if self.weapon is not None:
            return self.weapon.attack()  # Проверка, есть ли 'Fighter' оружия:
        else:
            return "Боец без оружия не может сражаться!, Пусть выберет оружие!" # Если оружие нет:

# Создаем класс 'Monstr':
class Monster():
    # Монстр имеет только одно состояние - "жив" или "побежден".
    def __init__(self):
        self.defeated = False

    def defeat(self):   # Метод поражения -'defeat' Монстра:
        self.defeated = True
        return "Монстр побежден!"


# Функция демонстрация игрового боя:
def battle_demo(fighter, monster, weapon):
    fighter.changeWeapon(weapon)    # Смена оружия:
    print(fighter.fight())          # Атака Fighter:
    print(monster.defeat())         # Поражение Monster:

fighter = Fighter()
monster = Monster()
sword = Sword()
bow = Bow()

# Боец выбирает меч и сражается с монстром
battle_demo(fighter, monster, sword)

# Создаем нового монстра для демонстрации боя с луком
monster = Monster()
# Боец выбирает лук и сражается с монстром
battle_demo(fighter, monster, bow)
# вывод сообщения, что у бойца нет оружия:
battle_demo(fighter, monster, None)