def menu(lista):
    cabeçalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c} -\033[34m {item}\033[m')
        c +=1
    linha()
    opc = recebe_opcao()
    return opc


def recebe_opcao():
    while True:
        escolha = input('\033[33mSua opção:\033[m ')
        try:
            escolha = int(escolha)
        except:
            print(f'\033[31mErro! Digite uma opção válida.\033[m')
        else:
            if escolha < 1 or escolha > 3:
                print(f'\033[31mErro! Digite uma opção válida.\033[m')
            else:
                return escolha


def linha():
    print('-'*50)


def cabeçalho(txt):
    linha()
    print(f'{txt:^50}')
    linha()


def arq_existe(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    a = open(nome, 'w+')
    a.close()
