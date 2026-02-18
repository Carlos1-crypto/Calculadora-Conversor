from calculadora.cálculos import soma, subtracao, multiplicacao, divisao

def verificar(operacao):
        if operacao in [1, 2, 3, 4, 5]:
            return operacao
        else:
            raise ValueError('Algo deu errado, digite apenas números de 1 a 5.')

def decisão(operacao):
    match operacao:
        case 1:
            escolha = 'soma'
        case 2:
            escolha = 'subtração'
        case 3:
            escolha = 'multiplicação'
        case 4:
            escolha = 'divisão'

    return escolha

def resultado(operacao, num1, num2):
    match operacao:
        case 1:
            resultado = soma(num1, num2)
        case 2:
            resultado = subtracao(num1, num2)
        case 3:
            resultado = multiplicacao(num1, num2)
        case 4:
            resultado = divisao(num1, num2)

    return resultado