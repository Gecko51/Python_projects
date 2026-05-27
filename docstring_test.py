"""utilisateur = "admin"
if utilisateur == "admin":
    print("accès autorisé")
elif utilisateur == "root":
    print("accès autorisé !")
else:
    print("accès refusé...")

liste = ["Python", ["Java", "C++",["C"]], ["Ruby"]]
print(liste[0])
list(range(5))
ma_liste = ["Pierre", "Paul", "Marie"]
resultat = ma_liste[0]
print(resultat)"""

resultat_1 = input("Entrez un premier nombre")
resultat_2 = input("Entrez un deuxième nombre")
num1 = int(resultat_1)
num2 = int(resultat_2)
if num1.isdigit() and num2.isdigit():
    print(f"Le résultat de l'addition de {num1} avec {num2} est égal à {num1 + num2}")
else:
    print("Veuillez entrer deux nombres valides")
    
