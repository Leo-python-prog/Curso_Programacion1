lista1 = [3, 5, 8]
lista2 = [5, 9, 12]

def comparar(lista1, lista2):
    # Primero debo convertir las listas en conjuntos para poder verificar si hay intersección
    # Hago que retorne un tipo de dato Booleano
    return bool(set(lista1) & set(lista2))  

print("\n")
print(comparar(lista1, lista2))
print("\n")