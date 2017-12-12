class Character:
    """Represents abstract object as for
    each character in arena."""
    n_character = 0

    def __init__(self, name, race, max_health):
        self.name = name
        self.race = race
        self.max_health = max_health
        self.health = max_health
        self.dead = False

        Character.n_character += 1

        print("{0} ({1}) was created".format(self.name, self.race))

    def heal(self):
        """Heal for 5 HP"""
        if self.health <= self.max_health - 5:
            self.health += 5
            print("{0} heals {1} HP".format(self.name, self.health))


    def __str__(self):
        return "Name: {0}, Health: {1}".format(self.name, str(self.health), end=" ")

    @classmethod
    def count_character(cls):
        """Class method for counting all characters"""
        print("Number of characters {0}".format(cls.n_character))


class Fighter(Character):
    """Fighter character can use berseker for furious
    attack and to regular sword attack.
    """

    def __init__(self, name, race, max_health, berseker=False):
        Character.__init__(self, name, race, max_health)
        self.berseker = berseker

    def __str__(self):
        return Character.__str__(self) + ", Berseker: {0}".format(str(self.berseker))

    def attack_sword(self, oponent):
        """Regular attack"""
        from numpy import random
        attack = random.randint(0, 5)
        print("{0} attacks by sword with {1} points".format(self.name, attack))
        if oponent.health >= attack:
            oponent.health -= attack
        else:
            print("{0} kills {1}".format(self.name, oponent.name))
            oponent.dead = True

    def rage(self):
        """Gets in the berseker mode"""
        self.berseker = True
        print("{0} get into berseker mode".format(self.name))

    def attack_furious(self, oponent):
        """Maximal damage attack"""
        if self.berseker:
            if oponent.health >= 10:
                oponent.health -= 10
                print("{0} attacks furiously with damage of 10".format(self.name))
            else:
                print("{0} kills {1}".format(self.name, oponent.name))
                oponent.dead = True

class Mage(Character):
    """Mage or wizard character which needs mana
    to cast a spell. This character can do fireball
    """

    def __init__(self, name, race, max_health, max_mana):
        Character.__init__(self, name, race, max_health)
        self.max_mana = max_mana
        self.mana = max_mana

    def __str__(self):
        return Character.__str__(self) + ", Mana: {0}".format(self.health)

    def meditate(self):
        """Regenertes a bit of mana"""
        if self.max_mana <= self.mana - 2:
            self.mana += 2
            print("{0} recovers mana to {1}".format(self.name, self.mana))

    def attack_fireball(self, oponent):
        """Fireball basic attack"""
        if self.mana >= 2:
            if oponent.health >= 5:
                oponent.health -= 5
                self.mana -= 2
                print("{0} cast fireball for 5 HP".format(self.name))
            else:
                print("{0} kills {1}".format(self.name, oponent.name))
                oponent.dead = True
        else:
            print("Not enough mana {0}".format(self.mana))


if __name__ == "__main__":
    aragorn = Fighter("Aragorn", "Human", 40)
    gandalf = Mage("Gandalf the Grey", "Human", 30, 20)

    print(aragorn)
    print(gandalf)

    aragorn.attack_sword(gandalf)
    gandalf.attack_fireball(aragorn)

    aragorn.rage()
    gandalf.attack_fireball(aragorn)

    aragorn.attack_furious(gandalf)
    gandalf.attack_fireball(aragorn)

    print(aragorn)
    print(gandalf)










"""
OK
"""

class Arena:

    def __init__(self, name):
        from Character import Fighter
        from Character import Mage

        self.player = Fighter("Drago", "Human", 20)
        self.oponent = Mage("Xandar", "Elf", 20, 10)
        self.name = name
        self.end_of_game = False
        self.wins = "Nobody"

        print("Arena battle {0} begins...".format(self.name))
        print()
        print("***Player***")
        print(self.player)
        print()
        print("***Oponent***")
        print(self.oponent)

    def game(self):
            while not self.end_of_game:
                    action = input("\n(H)eal | Attack with (S)word | Attack with (F)urious | Get (R)age\n")
                    if action == "h":
                        self.player.heal()
                    elif action == "s":
                        self.player.attack_sword(self.oponent)
                    elif action == "f":
                        self.player.attack_furious(self.oponent)
                    elif action == "r":
                        self.player.rage()
                    else:
                        print("Select proper action.\nOponent is on the move...")

                    if self.oponent.health < 2:
                        self.oponent.heal()
                    if self.oponent.mana < self.oponent.max_mana / 2:
                        self.oponent.meditate()
                    else:
                        self.oponent.attack_fireball(self.player)

                    print()
                    print(self.player)
                    print(self.oponent)
                    print("Next round...\n")

                    if self.oponent.dead or self.player.dead:
                        self.end_of_game = True

            if self.player.dead:
                self.wins = "Computer"
            else:
                self.wins = "Player"

            print("End of the game! {0} wins!".format(self.wins))
