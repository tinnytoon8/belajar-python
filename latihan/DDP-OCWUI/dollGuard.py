print("### REQUEST TACTICAL DOLL ###")

tactical_doll = input("\nMasukan nama Tactical Doll: ")
firepower = int(input("Masukan Firepower: "))
rate_of_fire = int(input("Masukan Rate of Fire: "))
accuracy = int(input("Masukan Accuracy: "))
evasion = int(input("Masukan Evasion: "))

damage_per_second = (firepower * rate_of_fire) / 60
combat_effectiveness = (
    30 * firepower + 40 * (rate_of_fire**2 / 120) + 15 * (accuracy + evasion)
)

print("\n### SUCCESS ###")
print("Tactical Doll:", tactical_doll)
print("Firepower:", firepower)
print("Rate of Fire:", rate_of_fire)
print("Accuracy:", accuracy)
print("Evasion:", evasion)

print("\nDamage per Second: %0.2f" % damage_per_second)
print("Combat Effectiveness:", round(combat_effectiveness))
