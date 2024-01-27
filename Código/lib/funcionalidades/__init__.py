def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo\033[m')
    else:
        conteudo = a.read()
        if conteudo:
            a.seek(0)  # volta ao início do arquivo
            for linha in a:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
        else:
            print('\033[1mO registro ainda está vazio.\033[m')
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mErro na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
          print('\033[31mErro no momento de inserção de dados no arquivo!\033[m')
        else:
            print(f'\033[32mNovo registro de "{nome}" adicionado com sucesso!\033[m')
            a.close()

def editar(arq):
    while True:
        nome = input('Digite o nome do usuário que deseja editar: ')
        try:
            linhas = []
            a = open(arq, 'rt')
            for l in a:
                linhas.append(l)
            nome_encontrado = False
            a.close()

            a = open(arq, 'wt')
            for l in linhas:
                dados = l.split(';')
                if dados[0] != nome.strip().lower():
                    # rescrevendo os dados novamente
                    a.write(l)
                else:
                    nome_encontrado = True
                    print(f'Editando dados de: "{nome}".')
                    novo_nome = input('Novo nome: ')
                    nova_idade = input('Nova idade: ')
                    a.write(f'{novo_nome};{nova_idade}\n') 
            a.close()   
        except:
            print('\033[31mErro ao editar dados!\033[m')
        else:
            if nome_encontrado:
                print(f'\033[32mEdição concluída com sucesso!\033[m')
                break
            else:
                print(f'\n\033[31mNão foi possível encontrar o nome "{nome}"\033[m\n')

def apagar(arq):
    while True:
        nome = input('Digite o nome do usuário que deseja apagar: ')
        try:
            linhas = []
            a = open(arq, 'rt')
            for l in a:
                linhas.append(l)
            nome_encontrado = False
            a.close()

            a = open(arq, 'wt')
            for l in linhas:
                dados = l.split(';')
                if dados[0] != nome.strip().lower():
                    a.write(l)
                else:
                    # não eh escrito os dados deste usuário novamente
                    nome_encontrado = True
                    print(f'Dados de: "{nome}" apagados.')
            a.close()   
        except:
            print('\033[31mErro ao apagar dados!\033[m')
        else:
            if nome_encontrado:
                print(f'\033[32mDados apagados com sucesso!\033[m')
                break
            else:
                print(f'\n\033[31mNão foi possível encontrar o nome "{nome}"\033[m\n')