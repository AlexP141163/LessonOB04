from abc import ABC, abstractmethod
# Создаем абстрактный класс 'Weapon', который не имеет
# собственной реализации.
class Weapon(ABC):
    @abstractmethod     # декоратор, который показывает, что метод 'attack' является абстрактным.
    def attack(self):   # Является шаблоyом который должены реализовывать подклассы:
        pass            # сам метод не выполняет никаких действий.

# Создаем класс оружия 'Sword' - Меч:
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

# Создаем класс оружия 'Bow' - Лук:
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Создаем класс бойца 'Fighter':
class Fighter:
    def __init__(self):
        self.weapon = None  # Боец 'Fighter' без оружия:

# Функция смены оружия:
    def changeWeapon(self, weapon):
        self.weapon = weapon


    def fight(self):
        if self.weapon is not None:
            return self.weapon.attack()  # Выбор оружия:
        else:
            return "Боец без оружия не может сражаться!" # Если оружие не выбрано:

# Создаем класс 'Monstr':
class Monster:
    # Монстр имеет только одно состояние - "жив" или "побежден".
    def __init__(self):
        self.defeated = False

    def defeat(self):
        self.defeated = True
        return "Монстр побежден!"


# Демонстрация игрового боя
def battle_demo(fighter, monster, weapon):
    fighter.changeWeapon(weapon)
    print(fighter.fight())
    print(monster.defeat())

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
