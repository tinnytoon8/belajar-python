import random


class Superhero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_types = ["normal", "strong", "fast", "heal"]
        self.attack_damages = [15, 30, 12, 0]
        self.heal_amount = 15

    def attack(self, villain, attack_index):
        if attack_index < 0 or attack_index >= len(self.attack_types):
            print("Invalid attack index!")
            return

        damage = self.attack_damages[attack_index]
        villain.take_damage(damage)
        print(
            f"{self.name} attacks {villain.name} with {self.attack_types[attack_index]} attack and deals {damage} damage!"
        )

        if self.attack_types[attack_index] == "heal":
            self.heal()
            return

    def heal(self):
        self.hp = min([100, self.hp + self.heal_amount])
        print(f"{self.name} uses heal and gains {self.heal_amount} HP!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")


class Villain:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_types = ["scracth", "kick", "punch", "heal"]
        self.attack_damages = [10, 18, 15, 0]

        self.heal_amount = 12

    def action(self, superhero):
        attack_index = random.randint(0, len(self.attack_types) - 1)
        random_action = self.attack_types[attack_index]

        if random_action != "heal":
            damage = self.attack_damages[attack_index]
            superhero.take_damage(damage)
            print(
                f"{self.name} attacks {superhero.name} with {self.attack_types[attack_index]} attack and deals {damage} damage!"
            )
        else:
            self.heal()
            print(f"{self.name} uses heal and gains {self.heal_amount} HP!")

    def heal(self):
        self.hp = min([100, self.hp + self.heal_amount])
        print(f"{self.name} uses heal and gains {self.heal_amount} HP!")

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} has been defeated!")


thunderman = Superhero("ThunderMan")
villain = Villain("EvilGuy")

while thunderman.hp > 0 and villain.hp > 0:
    print(
        f"\n{thunderman.name} (HP: {thunderman.hp} vs {villain.name} (HP: {villain.hp} ))"
    )

    print("Superhero`s Available attacks:")
    for i, attack_type in enumerate(thunderman.attack_types):
        print(f"{i+1}. {attack_type}")
    superhero_attack_index = int(input("\nSuperhero, Choose attack (1 - 4): ")) - 1
    thunderman.attack(villain, superhero_attack_index)

    if villain.hp <= 0:
        print(f"{villain.name} has been defeated! {thunderman.name} wins!")
        break

    print("\nVillain`s turn:")
    villain.action(thunderman)

    if thunderman.hp <= 0:
        print(f"{thunderman.name} has been defeated! {villain.name} wins!")
        break
