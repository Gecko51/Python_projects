print("--CALCULATRICE INTER-SPACIALE--")
while True:
  nombre_1 = input("Entrez un premier nombre : ") # Cette ligne invite l'utilisateur à entrer le premier nombre en utilisant la fonction input() et stocke la valeur saisie sous forme de chaîne de caractères dans la variable nombre_1.
  nombre_2 = input("Entrez un deuxième nombre : ") #  Similaire à la ligne précédente
  if nombre_1.isdigit() and nombre_2.isdigit(): # Il s'agit d'une instruction conditionnelle qui vérifie si nombre_1 et nombre_2 contiennent uniquement des chiffres en utilisant la méthode de chaîne de caractères .isdigit().
    print(f"Le résultat de l'addition de {nombre_1} avec {nombre_2} est égal à {int(nombre_1) + int(nombre_2)} ") # Si la condition dans l'instruction if est vraie (les deux entrées sont des chiffres), cette ligne affiche le résultat de l'addition. Elle utilise une f-string pour formater la sortie et convertit les chaînes de caractères d'entrée (nombre_1 et nombre_2) en entiers en utilisant int() avant d'effectuer l'addition.
    break
  else:
      print("Veuillez entrer deux nombres valides")
      continue
