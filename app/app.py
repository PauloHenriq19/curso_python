import os

restaurantes = [{'nome': 'Seven Kings', 'categoria': 'fastfood', 'ativo':False},
                {'nome': 'Pizzaria Romani', 'categoria': 'massas', 'ativo':True},
                {'nome': 'Sushi Bar', 'categoria': 'Japonesa', 'ativo':False}]


def exibir_nome_do_programa():
    '''
        Essa função exibe o nome do programa
    '''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''
        Essa função exibe as opções do menu principal da aplicação
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função finaliza o app e apresenta uma mensagem confirmando a finalização'''
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    '''Essa função solicita uma tecla para voltar ao menu principal
       Outputs:
       - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função informa que a opção escolhida é inválida
      
       Outputs:
       - retorna para o menu principal'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função exibe os subtitulos 
       Inputs:
       - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função cadastrar um novo restaurante
       Inputs:
       - Nome do restaurante
       - Categoria   
       
       Output:
       - Adiciona um novo restaurante na lista de restaurante
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categora do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados com o nome, categoria e status
       Outputs:
       - Exibe a lista de restaurantes na tela  
    '''
    exibir_subtitulo('Listando restaurantes')
    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | Status:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_status():
    '''Essa função altera o status ativo ou inativo do restaurante cadastrado, 
       caso o restaurante não tenha cadastro, será informado.
       Output:
       - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alternar Status do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante}foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função recebe a escolha digitada no menu principal
       Output:
       - Executa a opção escolhida do usuário'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_status()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()