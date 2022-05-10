
from questao import numero_questao
import random

input("\nPressione Enter para iniciar... ")


quant_pao_dormido=1.2 

out=False
while(not out):
    
        
    numero_questao(2)
    
    itens_verdes=[0, 100]
    itens_vermelhos=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    itens_pretos = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    roleta=[]

    for x in itens_verdes:
        roleta.append(x)
    for x in itens_vermelhos:
        roleta.append(x)
    for x in itens_pretos:
        roleta.append(x)
    
    result = random.choice(roleta)

    if result == 100:
        print('O resultado da rodada é: 00')
        print('Pagar 00')
    else:
        print('O resultado da rodada é: {}'.format(result), end="\n\n")
        print('Pagar {}'.format(result))
    

    if(result!=0 and result!=100):
        if(result in itens_vermelhos):
            print("Pagar vermelho")
        else:
            print("Pagar preto")

        if(result%2 == 0):
            print("Pagar par")
        else:
            print("Pagar impar")

        if(result<=18):
            print("Pagar 1 a 18")
        else:
            print("Pagar 19 a 36")
    else:
        print("Pagar verde")   


    opcao=input("\nPressione Enter para sortear novamente ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True





