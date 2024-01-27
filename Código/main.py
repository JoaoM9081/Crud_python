from lib.interface import *
from lib.arquivo import *

arq = 'registro.txt'

if not arq_existe(arq):
    criar_arquivo(arq)
    
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novo usuários', 'Sair do programa'])
    match resposta:
        case 1: # lista o conteúdo do arquivo de "registro"
            cabeçalho('PESSOAS CADASTRADAS')
            ler_arquivo(arq) 
        case 2: # cadastrar novas pessoas
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = int(input('Idade: '))
            cadastrar(arq, nome, idade)
        case 3:
            cabeçalho('SAINDO DO PROGRAMA... ATÉ LOGO!')
            break            
        case _:
            cabeçalho('\033[31mErro, digite uma opção válida!\033[m')