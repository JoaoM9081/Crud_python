def arq_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mErro ao abrir aquivo\033[m!')
    else:
        print(f'\033[32mArquivo "{nome}" criado com sucesso!\033[m')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
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
          print('\033[31mErroErro no momento de inserção de dados no arquivo!\033[m')
        else:
            print(f'\033[32mNovo registro de "{nome}" adicionado com sucesso!\033[m')
            a.close()