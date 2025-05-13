def main():
    valores_proposiciones = {}
    letras_disponibles = ['p', 'q']
    
    print("===== EVALUADOR DE PROPOSICIONES LÓGICAS =====")
    print("Este programa te permite evaluar expresiones lógicas.")
    
    for letra in letras_disponibles:
        valor = int(input(f"Ingrese el valor de verdad para '{letra}' (0 para Falso, 1 para verdadero)"))
        valores_proposiciones[letra] = bool(valor)
        
    print("\nValores asignados:")
    for letra, valor in valores_proposiciones.items():
        print(f"{letra}: {1 if valor else 0}")
        
    print("\nAhora puedes ingresar una expresión lógica utilizando las letras")


    
    