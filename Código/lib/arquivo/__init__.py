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