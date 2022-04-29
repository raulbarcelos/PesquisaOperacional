
import os

print("**********************************************************************************")
print("********************************** EXERCICIO 01 **********************************")
print("**********************************************************************************")
print("|\tA padaria do Pão & Pão vende seus pães por R$ 4,60 cada. \n|\tO pão do dia anterior (pão dormido) tem um desconto de 60%. \n|\tImplemente um programa que leia o número de pães dormidos que o usuário \n|\testá comprando e exiba o preço normal do pão, o desconto e o preço total. \n|\tTodos os valores devem ser exibidos usando duas casas decimais, \n|\te as casas decimais em todos os números devem ser alinhadas.")
print("**********************************************************************************")
input("\nPressione Enter para iniciar... ")


quant_pao_dormido=1.2 

out=False
while(not out):
    
    valor_pao = 4.60
    valor_desconto = valor_pao*0.6
    valor_pao_dormido=valor_pao-valor_desconto
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("**********************************************************************************")
    print("********************************** EXERCICIO 01 **********************************")
    print("**********************************************************************************")
    
    print('\nValor pão unid.: \t{:.2f}'.format(valor_pao))
    print('Valor do desconto: \t{:.2f} -> ({})%'.format(valor_desconto, int(valor_desconto*100/valor_pao)))
    print('Valor pão dormido: \t{:.2f}'.format(valor_pao_dormido))
    
    quant_pao_dormido=input("\nDigite a quantidade de pães dormidos ou 0 para sair: ")

    if not quant_pao_dormido.isdigit():
        print("**** Só é possivel digitar a quantidade em numero inteiro.")
        input("\nPressione Enter para digitar novamente... ")
        continue
    
    quant_pao_dormido=float(quant_pao_dormido)

    if not (quant_pao_dormido%1 == 0) and quant_pao_dormido != 0:
        print("**** Só é possivel comprar pães inteiros.")
        input("\nPressione Enter para digitar novamente... ")
        continue

    if(quant_pao_dormido==0):
        out=True
        print("------ SAINDO DO PROGRAMA! ------")
        continue

    total_pao_normal=quant_pao_dormido*valor_pao
    total_desconto=quant_pao_dormido*valor_desconto
    total_pao_dormido=total_pao_normal-total_desconto

    
    
    print('\nTotal de pães dormido: \t{}'.format(int(quant_pao_dormido)))

    print('\nO valor total (pães normais) é: \t{:9.2f}'.format(total_pao_normal))
    print('O valor total do desconto é de: \t{:9.2f}'.format(total_desconto))
    print('O valor total dos pães dormidos é: \t{:9.2f}'.format(total_pao_dormido))

    input("\nPressione Enter para digitar novamente... ")





