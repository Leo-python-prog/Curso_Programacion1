import random

f1 = ["Ferrari", "Mclaren", "Redbull", "Aston Martin"]

distancias = {auto: 0 for auto in f1}

for segundo in range(1, 11):
    print(f"Segundo {segundo}:")
    for auto in f1:
        velocidad = random.randint(1, 10)
        distancias[auto] += velocidad
        print(f" {auto} avanza {velocidad} unidades. Total: {distancias[auto]} unidades.")
    print()
    
distancia_maxima = max(distancias.values())
ganadores = [auto for auto, distancia in distancias.items() if distancia == distancia_maxima]

print("Resultado final:")
for auto, distancia in distancias.items():
    print(f"{auto}: {distancia} unidades")

if len(ganadores) == 1:
    print(f"\n¡El ganador es {ganadores[0]}!")
else:
    print(f"\n¡Es un empate entre: {', '.join(ganadores)}!")