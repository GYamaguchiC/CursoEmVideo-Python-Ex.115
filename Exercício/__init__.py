import Funcoes
from time import sleep

lista_opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
arquivo = 'cadastros.txt'
if not Funcoes.arq_existe(arquivo):
    Funcoes.criar_arquivo(arquivo)


while True:
    opc = Funcoes.menu(lista_opcoes)
    if opc == 1:
        Funcoes.cabeçalho('Pessoas cadastradas')
        with open('cadastros.txt', 'r') as arquivo:
            for linha in arquivo:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>16} anos')
    if opc == 2:
        Funcoes.cabeçalho('Novo Cadastro')
        with open('cadastros.txt', 'a') as arquivo:
            arquivo.write(f'{input("Nome: ")};')
            arquivo.write(f'{input("Idade: ")}\n')
    if opc == 3:
       Funcoes.cabeçalho('Saindo do sistem... Até logo!')
       break
    sleep(1)
