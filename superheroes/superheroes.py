import random


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def is_alive(self):
        return self.current_health > 0

    def defend(self):
        tot_blck = 0
        if self.current_health == 0:
            return 0
        else:
            for armor in self.armors:
                tot_blck += armor.block()
            return tot_blck

    def add_kill(self, num_kills):
        self.kills += num_kills

    def take_damage(self, damage):
        self.current_health -= damage

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            hero_damage = self.attack()
            print(
                f"{self.name} attacks {opponent.name} for {hero_damage} damage")
            opponent_damage = opponent.attack()
            print(f"{opponent.name} attacks {self.name} for {opponent_damage} damage")

            opponent.take_damage(hero_damage)
            print(opponent.current_health)
            self.take_damage(opponent_damage)
            print(self.current_health)
        if not opponent.is_alive():
            self.add_kill(1)
            opponent.deaths += 1
        if not self.is_alive():
            opponent.add_kill(1)
            self.deaths += 1

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)


class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)


class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        removed = False
        for i in range(len(self.heroes)):
            if self.heroes[i].name == name:
                self.heroes.pop(i)
                removed == True
        if not removed:

            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def alive_heroes(self):
        alive_list = []
        for hero in self.heroes:
            if hero.is_alive():
                alive_list.append(hero)
        return alive_list

    def attack(self, other_team):
        while len(self.alive_heroes()) > 0 and len(other_team.alive_heroes()) > 0:
            hero = random.choice(self.alive_heroes())
            opponent = random.choice(other_team.alive_heroes())
            hero.fight(opponent)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        print(self.name)
        for hero in self.heroes:
            print(
                f"- {hero.name} kills: {hero.kills} - {hero.name} deaths: {hero.deaths} ")


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        print("You are about to create an ability")
        ability_name = input("Give me an ability name: ")
        ability_damage = int(input("Give me the max damage of an ability: "))
        ability = Ability(ability_name, ability_damage)
        return ability

    def create_weapon(self):
        print("You are about to create a weapon")
        weapon_name = input("Give me a weapon name: ")
        weapon_damage = int(input("Give me the max damage of your weapon: "))
        weapon = Weapon(weapon_name, weapon_damage)
        return weapon

    def create_armor(self):
        armor_name = input("Give me an armor name: ")
        armor_defense = int(input("Give me the max defense of your armor: "))
        armor = Armor(armor_name, armor_defense)
        return armor

    def create_hero(self):
        hero_name = input("Give me the name of your hero: ")
        hero = Hero(hero_name)
        hero.add_ability(self.create_ability())
        hero.add_armor(self.create_armor())
        hero.add_weapon(self.create_weapon())
        return hero

    def build_team(self):
        team_name = input("Give your team a name: ")
        team = Team(team_name)
        hero_num_input = int(input("How may heroes are on your team?: "))
        while hero_num_input > 0:
            hero = self.create_hero()
            hero_num_input -= 1
            team.add_hero(hero)
        return team

    def build_team_one(self):
        print("You are about to build team one!")
        self.team_one = self.build_team()

    def build_team_two(self):
        print("You are about to build team two!")
        self.team_two = self.build_team()

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()
        if len(self.team_one.alive_heroes()) > 0:
            print("Team one is the winner!")
            for hero in self.team_one.alive_heroes():
                print(hero.name)
        else:
            print("Team two won")
            for hero in self.team_two.alive_heroes():
                print(hero.name)


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
