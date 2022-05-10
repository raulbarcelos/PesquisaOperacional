
from questao import numero_questao
import os

os.system('cls' if os.name == 'nt' else 'clear')
input("\nPressione Enter para iniciar... ")



""" 
1 ponto A, E, I, L, N, O, R, S, T, U
2 pontos D, G
3 pontos B, C, M, P
4 pontos F, H, V, W, Y
5 pontos K
8 pontos J, X
10 pontos Q, Z
"""

ponto1 = ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']
ponto2 = ['D', 'G']
ponto3 = ['B', 'C', 'M', 'P']
ponto4 = ['F', 'H', 'V', 'W', 'Y']
ponto5 = ['K']
ponto8 = ['J', 'X']
ponto10 = ['Q', 'Z']

def scrabble(palavra):
    print("Dentro do scrabble")
    pontuacao = 0
    palavra_parcial=''
    for letra in palavra:
        palavra_parcial = palavra_parcial+letra
        if ponto1.count(letra.upper()) != 0:
            pontuacao=pontuacao+1
        elif ponto2.count(letra.upper()) != 0:
            pontuacao=pontuacao+2
        elif ponto3.count(letra.upper()) != 0:
            pontuacao=pontuacao+3
        elif ponto4.count(letra.upper()) != 0:
            pontuacao=pontuacao+4
        elif ponto5.count(letra.upper()) != 0:
            pontuacao=pontuacao+5
        elif ponto8.count(letra.upper()) != 0:
            pontuacao=pontuacao+8
        elif ponto10.count(letra.upper()) != 0:
            pontuacao=pontuacao+10
        print('{} = {}'.format(palavra_parcial, pontuacao))

    print('Pontuação total: {}'.format(pontuacao))

out=False
while(not out): 
        
    numero_questao(8)

    palavra = input("Digite uma palavra (A-Z): ")

    #if not palavra.isdigit():
    #verifica se o input é texto
    if palavra.isalpha():
        scrabble(palavra)
    else:
        print("Só são aceitos palavras sem espaços, números e caracteres especiais")

    opcao=input("\nPressione Enter para digitar a palavra novamente ou 0 para sair: ")
    if(opcao == 0 or opcao=='0'):
        print("------ SAINDO DO PROGRAMA! ------")
        out=True



