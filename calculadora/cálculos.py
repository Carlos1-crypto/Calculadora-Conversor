def soma(a=float, b=float):
    soma = a + b
    return soma

def subtracao(a=float, b=float):
    subtracao = a - b
    return subtracao

def multiplicacao(a=float, b=float):
    multiplicacao = a * b
    return multiplicacao

def divisao(a=float, b=float):
    if b != 0:
        divisao = a / b
        return divisao
    else:
        raise ValueError("Divisão por zero não é permitida.")