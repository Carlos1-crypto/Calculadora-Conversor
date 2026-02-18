from conversor.conversões import C_F, F_C

def decisão(escolha):
    match escolha:
        case 1:
            C_F()
        case 2:
            F_C()
        case 3:
            print('Saindo...')
            exit()