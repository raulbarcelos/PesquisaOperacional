
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")



""" 
Defina uma lista com todos os números de 2 ao limite
Defina p igual a 2
Enquanto p < limite, faça
Elimine da lista todos os múltiplos de p (exceto p)
Defina p igual ao próximo número da lista
Imprima a lista 
"""


primos = []

def criando_lista(limite):
    for i in range(int(limite)+1):
        primos.append(i)

    return primos

def crivo_de_eratostenes(limite):
    lista_primos = criando_lista(limite)
    
    p = 2
    
    #acessando cada numero da lista (começando do 2; até a metade do intervalo)
    #metade do intervalo pq não precisamos acessar o 11, 12, 13, por exemplo
    for p in range(2, int((len(lista_primos)+1)/2)):
        #laço para acessar os multiplos de 2. Vamos remover todos os 2*p 
        for multiplo in range(2*p, len(lista_primos), p):
            if lista_primos[multiplo] != False:
                lista_primos[multiplo] = False #se o numero não é primo recebe False

    #laço para imprimir lista de numeros primos
    for i in range(len(lista_primos)):
        if i >= 2:
            #imprimindo primos da lista
            if lista_primos[i] != False:
                print(lista_primos[i])
    



out=False
while(not out): 
        
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**********************************************************************************")
    print("********************************** EXERCICIO 07 **********************************")
    print("**********************************************************************************")

    limite = input("Digite o limite: ")

    if limite.isdigit() and int(limite)>=2 and float(limite)%1 == 0:
        crivo_de_eratostenes(limite)
    else:
        print("Só são aceitos numeros inteiros maiores ou igual a 2")

    opcao=input("\nPressione Enter para digitar mes e ano novamente ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True



