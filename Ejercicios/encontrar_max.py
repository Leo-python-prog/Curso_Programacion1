def encontrar_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

# Ejemplo de uso
numeros = [3, 5, 1, 8, 2]
maximo = encontrar_maximo(numeros)
print(f"El número máximo es: {maximo}")
# Este código define una función que encuentra el número máximo en una lista de números.