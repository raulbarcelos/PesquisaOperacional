

from questao import numero_questao
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")


quant_pao_dormido=1.2 

out=False
while(not out):
    
        
    numero_questao(3)
    
    colecao = []
    aux=0
    maximo=0
    count=0
    for x in range(100):
        result = random.randrange(1,100, 1)
        colecao.append(result)
        if(result>aux and x!=0):
            print('{} -> (atualizado)'.format(result))
            maximo+=1
            aux=result
        else:
            print(result)

    for x in colecao:
        if aux==x:
            count+=1

    print('O valor máximo encontrado foi: {}'.format(aux))
    print('O número máximo de vezes que o maior valor foi atualizado foi: {}'.format(maximo))
    print('O numero de vezes que o numero [{}] apareceu foi: {}'.format(aux, count))

    opcao=input("\nPressione Enter para gerar novos números aleatórios ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True





