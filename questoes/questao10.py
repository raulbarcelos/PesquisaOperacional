
from questao import numero_questao
import os

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")


""" 
Leia duas strings s e t
Se tamanho de s é 0, então
    Retorne o tamanho de t
Senão Se o tamanho t for 0, então
    Retorna o comprimento de s
Senão
    Custo = 0
    Se o último caractere em s não for igual ao último caractere em t, então
        Custo = 1
    Defina d1 igual à distância de edição entre todos os caracteres, exceto o último em s, e todos os caracteres em t, mais 1
    Defina d2 igual à distância de edição entre todos os caracteres em s, e todos caracteres exceto o último em t, mais 1
    Defina d3 igual à distância de edição entre todos os caracteres, exceto o último em s, e todos os caracteres, exceto o último em t, mais custo
    Retorne o mínimo de d1, d2 e d3
 """ 

out=False
while(not out): 
        
    numero_questao(10)

    print()

    s = input("Digite a primeira palavra: ")
    t = input("Digite a segunda palavra: ")

    if len(s) == 0:
        print(len(t))
    elif len(t) == 0:
        print(len(s))
    else:
        custo = 0
        if s[len(s)-1] == t[len(t)-1]:
            custo = 1
            print(custo)


    #ler_arquivo(arquivo1)

    opcao=input("\nDigite 0 para confirmar saida ou qualquer outra tela para voltar para a questão: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True



