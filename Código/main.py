from lib.interface import *
from lib.arquivo import *
from lib.funcionalidades import *

arq = 'registro.txt'

if not arq_existe(arq):
    criar_arquivo(arq)
    
while True:
    resposta = menu(['Mostrar usuários cadastradas', 'Cadastrar novos usuários', 'Editar dados de usuários cadastrados', 'Apagar dados de usuários cadastrados', 'Sair do programa'])
    if resposta == 1: # lista o conteúdo do arquivo de "registro"
        cabeçalho('PESSOAS CADASTRADAS')
        ler_arquivo(arq) 
    elif resposta == 2: # cadastrar novas pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = ler_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3: # Editar dados de usuários cadastrados
        cabeçalho('EDITAR DADOS')
        editar(arq)
    elif resposta == 4: # Apagar dados de usuários cadastrados
        cabeçalho('APAGAR DADOS')
        apagar(arq)
    elif resposta == 5:
        cabeçalho('SAINDO DO PROGRAMA... ATÉ LOGO!')
        break            
    else:
        cabeçalho('\033[31mErro, digite uma opção válida!\033[m')