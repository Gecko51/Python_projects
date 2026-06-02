import random
a = random.randint(1, 10)
b = random.randint(1, 10)

if b > a:
    print("Le nombre b est plus grand que le nombre a. ")
elif a > b:
    print("Le nombre a est plus grand que le nombre b. ")
else:
  print("Les deux nombres sont égaux. ")
