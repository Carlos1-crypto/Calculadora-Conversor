from conversor.conv import decisão

def conversor_temperatura():
    print("====Bem Vindo ao Conversor de Temperatura!====\n")
    while True:
        print("1. Celsius para Fahrenheit\n"
              "2. Fahrenheit para Celsius\n"
              "3. Sair\n")
        while True:
            try:
                escolha = int(input("Escolha a opção: "))
                break
            except ValueError:
                print('Algo deu errado, digite apenas números\n.')

        if escolha in [1, 2, 3]:
            decisão(escolha)
        else:
            print('Digite apenas números de 1 a 3.')
            break