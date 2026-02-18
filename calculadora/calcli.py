from calculadora.calc import verificar, decisão, resultado

def calculadora_interface():
    print("Bem Vindo à Calculadora Simples!!!!")
    while True:
        print("\n1. Soma\n"
              "2. Subtração\n"
              "3. Multiplicação\n"
              "4. Divisão\n"
              "5. Sair\n")
        while True:
            try:
                operacao = int(input("Escolha a operação: "))
                break
            except ValueError:
                print('Operação inválida. Digite apenas um número de 1 a 5.')
                
        resposta = verificar(operacao)

        if resposta in [1, 2, 3, 4]:
            print(f"Você escolheu a operação {decisão(resposta)}.\n"
                    "Digite os números:")
            while True:
                try:
                    num1 = float(input("Número 1: "))
                    num2 = float(input("Número 2: "))
                    break
                except ValueError:
                    print('Resposta inválida, tente digitar apenas números.')

            print(f'Resultado: {resultado(resposta, num1, num2)}')
        else:
            print('Saindo...')
            return

