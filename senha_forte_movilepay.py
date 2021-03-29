import re


n = int(input())
password = input()


def testar_password(n, password):
    tamanho_minimo = 6
    numeros_minimo = 1
    minusculas_minimo = 1
    maiusculas_minimo = 1
    especial_char_minimo = 1
    valor_minimo = 0
    if 1 <= n <= 100:
        if n < tamanho_minimo:
            valor_minimo = tamanho_minimo - n

        if len(re.findall("\d+", password)) < numeros_minimo:
            valor_minimo += 1
        if len(re.findall(r"[a-z]", password)) < minusculas_minimo:
            valor_minimo += 1
        if len(re.findall(r"[A-Z]", password)) < maiusculas_minimo:
            valor_minimo += 1
        if len(re.findall(r"[!@#$%^&*()+-]", password)) < especial_char_minimo:
            valor_minimo += 1
        if (valor_minimo + len(password)) < n:
            valor_minimo += (n - len(password))
            #valor_minimo += (n - valor_minimo)

        # if re.match(r"^(?=.*[\d])(?=.*[AZ])(?=.*[az])(?=.*[@#$])[\w\d@#$]{6,12}$", password):
            # print("match")
        # else:
            # print("Not Match")

        print(valor_minimo)


testar_password(n, password)
# test_password("J3sus0")
# test_password("  # Te5t300")
# test_password("J * 90j12374")
# test_password("Michheeul")
# test_password("Monk3y6")
