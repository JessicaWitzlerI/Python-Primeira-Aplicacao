import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

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
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}
    # append adiciona um objeto a lista
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

# função para listar os restaurantes
def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes')
    
    # para cada restaurante na lista dos restaurantes, ele vai passar o nome do restaurante
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu()

def alternar_estado():
    exibir_subtitulo('Alternando estado do restaurante\n')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    # IMPORTANTE FAZER UMA EXPLICAÇÃO MAIS DETALHADA
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            # restaurante na chave ativo vai ser igual a inversão do valor que ele tem 
            # não importa o valor que ele esta, sempre será o oposto dele
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado.')

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
            alternar_estado()
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