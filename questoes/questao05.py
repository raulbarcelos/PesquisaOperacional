
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")


meses=['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dias_meses=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def quantos_dias(mes, ano):
    
    if int(ano)==0 or int(mes)==0:
        print("\nSó são aceitos mes e ano maiores que 0.")
        return

    if mes.isdigit() and ((int(ano)>=1000 and int(ano)<10000) and float(ano)%1==0):
        bissexto=False
        print()
        if float(ano)%400==0:
            print('O ano {} é bissexto.'.format(ano))
            bissexto=True
        elif float(ano)%100==0:
            print('O ano {} NÃO é bissexto.'.format(ano))
        elif float(ano)%4==0:
            print('O ano {} é bissexto.'.format(ano))
            bissexto=True
        else:
            print('O ano {} NÃO é bissexto.'.format(ano))

        for m in range(12):
            indice_mes = int(mes)-1
            if(m==indice_mes):
                
                if(indice_mes==1 and bissexto==True):
                    print('O mês de {} tem {} dias'.format(meses[m], dias_meses[indice_mes]+1))
                else:
                    print('O mês de {} tem {} dias'.format(meses[m], dias_meses[indice_mes]))
    else:
        print("**** Só é possivel digitar ano com numero inteiro.")


out=False
while(not out):
    
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**********************************************************************************")
    print("********************************** EXERCICIO 05 **********************************")
    print("**********************************************************************************")

    mes=input("\nDigite o mes: ")
    ano=input("Digite o ano com 4 digitos: ")
    
    quantos_dias(mes, ano)

    opcao=input("\nPressione Enter para digitar mes e ano novamente ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True







""" 	
"1   Janeiro	    31 dias
2	Fevereiro	28 dias 
3	Março	    31 dias
4	Abril	    30 dias
5	Maio	    31 dias
6	Junho	    30 dias
7	Julho	    1 dias
8	Agosto	    31 dias
9	Setembro	30 dias
10	Outubro	    31 dias
11	Novembro	30 dias
12	Dezembro    31 dias
 


Escreva uma função que determina quantos dias há em um
determinado mês. Sua função terá dois parâmetros: o mês como
um número inteiro entre 1 e 12 e o ano como um número inteiro de
quatro dígitos. Certifique-se de que sua função informe o número
correto de dias em fevereiro para os anos bissextos. Utilizar a
função implementada no exercício 4.

"""