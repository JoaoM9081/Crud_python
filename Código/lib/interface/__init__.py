from lib.funcionalidades import ler_int

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(l):
    cabeçalho('Menu principal')
    cont = 1
    for item in l:
        print(f'\033[1;33m{cont}\033[m - \033[1;34m{item}\033[m')
        cont += 1
    print(linha())
    opc = ler_int('\033[1;36mDigite uma opção:\033[m ')
    return opc