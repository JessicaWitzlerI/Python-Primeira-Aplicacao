import os

restaurantes = []

# função para o nome do programa
def nome_programa():
    print('''
          𝔼𝕩𝕡𝕣𝕖𝕤𝕤
          ''')

# função para as opções
def opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


# função para finalizar o app e limpar o terminal
def finalizar_app():
    os.system('cls')
    print('App finalizado\n')

# função para opções inválidas
def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal. ')
    main()

#função para cadastrar os restaurantes
def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    # append adiciona um objeto a lista
    restaurantes.append
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

# função para a condicional 
def escolha_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()        

# função do programa principal
def main():
    os.system('cls')
    nome_programa()
    opcoes()
    escolha_opcao()

# definição do programa como principal 
if __name__ == '__main__':
    main()