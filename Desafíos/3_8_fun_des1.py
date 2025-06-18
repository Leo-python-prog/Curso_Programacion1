numeros = [4, 1, 5, 6, 8, 14, 22]

# Solución 1
def suma_prom_1(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return suma, promedio

print("\n")
res = suma_prom_1(numeros)
print("Solución 1")
print(f"La suma total es: {res[0]}")
print(f"El promedio es: {res[1]:.2f}")

# Solución 2
def suma_prom(lista):
    suma_lista = sum(lista)
    prom_lista = suma_lista / len(lista)
    return suma_lista, prom_lista

print("\n")
suma, promedio = suma_prom(numeros)
print("Solución 2")
print(f"La suma total es: {suma}")
print(f"El promedio es: {promedio:.2f}")

print("\n")