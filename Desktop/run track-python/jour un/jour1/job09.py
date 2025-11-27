
nom = "Ordinateur"
prix_unitaire = 800
quantité_en_stock = 7

print(nom, prix_unitaire, quantité_en_stock)


q = int(input("quantité saisie : 2"))
q = min(max(q , 7), quantité_en_stock)  
quantité_en_stock-= q
print("achat", q)
print("montant", q * prix_unitaire)


prix_unitaire *= 1.10 #inflation

print(nom, prix_unitaire, quantité_en_stock) 