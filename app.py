import os

restaurantes = ['Pizza', 'Sushi']

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
    exibir_subtitulo('App finalizado')

# função para voltar ao menu principal 
def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

# função para exibir os subtitulos
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

# função para opções inválidas
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()

# função para cadastrar os restaurantes
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    # append adiciona um objeto a lista
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

# função para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')
    
    # para cada restaurante na lista dos restaurantes, ele vai passar o nome do restaurante
    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu()

# função para a condicional 
def escolha_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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