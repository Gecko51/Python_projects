# Exercices d'apprentissage Python

# 1. Variables
nom = input("Quel est votre nom ? ")
age = int(input("Quel âge avez-vous ? "))

# 2. Conditions
if age >= 18:
    statut = "majeur"
else:
    statut = "mineur"

print(f"Bonjour {nom}, vous êtes {statut}.")

# 3. Boucle et liste
notes = []
for i in range(3):
    note = float(input(f"Note {i+1}/3 : "))
    notes.append(note)

# 4. Calcul moyenne
moyenne = sum(notes) / len(notes)
print(f"Moyenne : {moyenne:.2f}")

# 5. Dictionnaire
eleve = {
    "nom": nom,
    "age": age,
    "notes": notes,
    "moyenne": moyenne
}

print("\nRésumé :")
for cle, valeur in eleve.items():
    print(f"{cle}: {valeur}")
