import re


def testar_password(n, password):
    # tamanho_minimo = 6
    numeros_minimo = 1
    minusculas_minimo = 1
    maiusculas_minimo = 1
    especial_char_minimo = 1
    valor_minimo = 0  # valor minimo de caracteres que precisam ser informados para que a senha seja considerada forte

    # Todos os caracteres de password devem respeitar [a-z], [A-Z], [0-9] e [!@#$%^&*()-+]
    if 1 <= n <= 100 and (re.match(r'^[a-zA-Z0-9!@#$%^&*()+-]+$', password)):
        # Se todos os digitos numericos achados for menor que pelo menos 1, ou seja, se não houver.
        if len(re.findall(r"[0-9]", password)) < numeros_minimo:
            valor_minimo += 1
        # Se não houver pelo menos um caractere minusculo
        if len(re.findall(r"[a-z]", password)) < minusculas_minimo:
            valor_minimo += 1
        # Se não houver pelo menos um caractere maiusculo
        if len(re.findall(r"[A-Z]", password)) < maiusculas_minimo:
            valor_minimo += 1
        # Se não houver pelo menos um caractere especial
        if len(re.findall(r"[!@#$%^&*()+-]", password)) < especial_char_minimo:
            valor_minimo += 1

        ''' # Acho que seria mais correto sugerir para a senha completar ate n ou ate o valor minimo
            # Mas aparentemente a questao nao pede
        if (valor_minimo + len(password)) < n:
            valor_minimo += (n - (valor_minimo + len(password)))
        if (valor_minimo + len(password)) < tamanho_minimo:
            valor_minimo += (tamanho_minimo - (valor_minimo + len(password)))
        '''

        print(valor_minimo)


n = int(input())
password = input()
testar_password(n, password)
