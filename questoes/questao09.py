
from questao import numero_questao
import os

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")


def abrir_arquivos():
    
    while True:
        nome_arquivo = input("Digite o nome do arquivo (questao01.py a questao10.py) ou -1 para sair: ")
        print()
        if nome_arquivo == "-1": #int(nome_arquivo) == 0 or nome_arquivo == '0':
                print("dentro do if 0")
                return
        try:
            arquivo = open('questoes\{}'.format(nome_arquivo), 'r').readlines()
            ler_arquivo(arquivo)
        except:
            print("Não foi possivel o arquivo informado")
            
        """ finally:
            abrir_arquivos() """



arquivo1 = open('questoes\questao07.py', 'r').readlines()

def ler_arquivo(arquivo):
    num_linha=1
    sem_funcao=True
    for linha in arquivo:
        contador = 0
        nome_funcao = ''
        if (linha[0] == 'd' and linha[1] == 'e' and linha[2] == 'f' and linha[3] == ' '):
            sem_funcao=False
            for letra in linha:
                if contador>3:
                    if(letra != '('):
                        nome_funcao = nome_funcao + letra
                    else:
                        break
                contador += 1
            print("{} | {}".format(num_linha, nome_funcao))
        num_linha=num_linha+1
    if sem_funcao:
       print("Não há nenhuma função definida nesse arquivo\n")
    else:
        print()


out=False
while(not out): 
        
    numero_questao(9)

    print()

    abrir_arquivos()
    #ler_arquivo(arquivo1)

    opcao=input("\nDigite 0 para confirmar saida ou qualquer outra tela para voltar para a questão: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True



