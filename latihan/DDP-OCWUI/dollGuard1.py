print("### MY TACTICAL DOLL ###")

my_tactical_doll = input("\nMasukan nama Tactical Doll anda: ")
my_firepower = int(input("Masukan Firepower: "))
my_rate_of_fire = int(input("Masukan Rate of Fire: "))
my_accuracy = int(input("Masukan Accuracy: "))
my_evasion = int(input("Masukan Evasion: "))

my_damage_per_second = my_firepower * my_rate_of_fire / 60
my_combat_effectiveness = (
    30 * my_firepower
    + 40 * (my_rate_of_fire**2 / 120)
    + 15 * (my_accuracy + my_evasion)
)

print("\n### SUCCESS ###")
print("Tactical Doll:", my_tactical_doll)
print("Firepower:", my_firepower)
print("Rate of Fire:", my_rate_of_fire)
print("Accuracy:", my_accuracy)
print("Evasion:", my_evasion)

print("\nDamage per Second: %0.2f" % my_damage_per_second)
print("Combat Effectiveness:", round(my_combat_effectiveness))


print("\n### ENEMY TACTICAL DOLL ###")

en_tactical_doll = input("\nMasukan nama Tactical Doll musuhmu: ")
en_firepower = int(input("Masukan Firepower: "))
en_rate_of_fire = int(input("Masukan Rate of Fire: "))
en_accuracy = int(input("Masukan Accuracy: "))
en_evasion = int(input("Masukan Evasion: "))

en_damage_per_second = en_firepower * en_rate_of_fire / 60
en_combat_effectiveness = (
    30 * en_firepower
    + 40 * (en_rate_of_fire**2 / 120)
    + 15 * (en_accuracy + en_evasion)
)

print("\n### SUCCESS ###")
print("Tactical Doll:", en_tactical_doll)
print("Firepower:", en_firepower)
print("Rate of Fire:", en_rate_of_fire)
print("Accuracy:", en_accuracy)
print("Evasion:", en_evasion)

print("\nDamage per Second: %0.2f" % en_damage_per_second)
print("Combat Effectiveness:", round(en_combat_effectiveness))

if (
    my_damage_per_second > en_damage_per_second
    and my_combat_effectiveness > en_combat_effectiveness
):
    print("\nKeputusan : Lawan!")
elif (
    my_damage_per_second == en_damage_per_second
    and my_combat_effectiveness == en_combat_effectiveness
):
    print("\nKeputusan : Seimbang!")
else:
    print("\nKeputusan : Kaborrrr!")
