from conversor.convcli import conversor_temperatura

def intermediador():
    while True:
        resposta = input('Antes de ir, gostaria de usar o conversor de Temperatura? (S/N)'
        '\nResposta: ')
        if resposta in ['S', 's', 'sim', 'Sim', 'SIM']:
            conversor_temperatura()
        elif resposta in ['N', 'n', 'nao', 'não', 'Não', 'Nao', 'NÃO', 'NAO']:
            print('Ok, até mais!')
            break
        else:
            print('Digite apenas sim ou não.')
            continue