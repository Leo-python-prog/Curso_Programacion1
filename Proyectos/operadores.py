def input_v_f():
    while True:
        res = input().strip().lower()
        if res == 'v' or res == 't' or res == '1':
            return True
        elif res == 'f' or res =='0':
            return False
        else:
            print("Ingresar 'v' o 'f'.")

def eval_exp():
    while True:
        expr = expr.lower()
        o_pr = input().strip().lower()
        if o_pr == 'o' or o_pr == '∨' or o_pr == 'disyuncion':
            if o_pr in ['o', '∨', 'disyuncion']:
                expr = expr.replace('∨', 'or').replace('o', 'or').replace('disyuncion', 'or')
        else:
            print("ingresar un conector válido")

        y_pr = input().strip().lower()
        if y_pr == 'y' or y_pr == '∧' or y_pr == 'conjuncion':
            if y_pr in ['y', '∧', 'conjuncion']:
                expr = expr.replace('∧', 'and').replace('y', 'and').replace('conjuncion', 'and')
        else:
            print("ingresar un conector válido")

        n_pr = input().strip().lower()
        if n_pr == 'no' or n_pr == '¬' or n_pr == 'negacion':
            if n_pr in ['no', '¬', 'negacion']:
                expr = expr.replace('¬', 'not').replace('no', 'not').replace('negacion', 'and')
        else:
            print("ingresar un conector válido")
        
        """
        i_pr = input().strip().lower()
        if i_pr == 'y' or i_pr == '→' or i_pr == 'implicacion':
            return True
        else:
            print("ingresar un conector válido")

        d_i_pr = input().strip().lower()
        if d_i_pr == 'si y solo si' or d_i_pr == '↔' or d_i_pr == 'doble implicacion':
            return True
        else:
            print("ingresar un conector válido")

        d_inc_pr = input().strip().lower()
        if d_inc_pr == '⊕' or d_inc_pr == 'disyuncion exclusiva':
            return True
        else:
            print("ingresar un conector válido")
        """

print('ingresar proposición')
prop = eval_exp()
print('ingresar el valor de verdad de p')
p = input_v_f()
print('ingresar el valor de verdad de q')
q = input_v_f()