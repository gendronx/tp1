"""
Xavier Gendron
404
ce programme compte le nombre de mots d'une phrase
"""

chaine = str(input("Entrer une chaine de caracteres: "))
chaine2 = chaine.lower()
chaine3 = chaine2.strip()
chaine4 = chaine3.count(" ")
print(chaine4 + 1)
