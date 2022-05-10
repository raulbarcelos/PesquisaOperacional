

from questao import numero_questao
import os

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")


quant_pao_dormido=1.2 

out=False
while(not out):
    
        
    numero_questao(4)

    ano=input("\nDigite o ano para descobrir se é bissexto: ")
    if (not ano.isdigit()) or (not float(ano)%1 == 0):
        print("**** Só é possivel digitar ano com numero inteiro.")
    elif int(ano)==0:
        print("**** Não é possivel digitar o valor 0 para o ano.")
    else:
        if(float(ano)%400==0):
            print('O ano {} é bissexto.'.format(ano))
        elif(float(ano)%100==0):
            print('O ano {} NÃO é bissexto.'.format(ano))
        elif(float(ano)%4==0):
            print('O ano {} é bissexto.'.format(ano))
        else:
            print('O ano {} NÃO é bissexto.'.format(ano))


    opcao=input("\nPressione Enter para digitar um novo ano ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True





