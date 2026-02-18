def C_F():
    graus = (input("Digite a temperatura em Celsius: "))
    try:
        graus = float(graus)
    except ValueError:
        print('Algo deu errado, digite apenas números.')
        return C_F()
    Fahrenheit = (graus * 1.8) + 32
    return print(f'{graus} Graus Celsius em Fahrenheit é: {Fahrenheit} Graus Gahrenheit.')

def F_C():
    graus = (input("Digite a temperatura em Fahrenheit: "))
    try:
        graus = float(graus)
    except ValueError:
        print('Algo deu errado, digite apenas números.')
        return F_C()
    Celsius = (graus - 32) * 5 / 9
    return print(f'{graus} Graus Fahrenheit em Celsius é: {Celsius} Graus Celsius.')