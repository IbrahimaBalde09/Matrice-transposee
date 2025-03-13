
rows = int(input("Entrez le nombre de lignes de la matrice: "))
cols = int(input("Entrez le nombre de colonnes de la matrice: "))


matrice = []
print("Entrez les éléments de la matrice ligne par ligne:")
for i in range(rows):
    ligne = list(map(int, input().split()))
    while len(ligne) != cols:
        print(f"Veuillez entrer exactement {cols} valeurs.")
        ligne = list(map(int, input().split()))
    matrice.append(ligne)

transposee = [[matrice[j][i] for j in range(rows)] for i in range(cols)]

print("Matrice transposée:")
for ligne in transposee:
    print(" ".join(map(str, ligne)))