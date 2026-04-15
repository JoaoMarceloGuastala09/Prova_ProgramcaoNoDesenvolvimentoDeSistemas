import os
from time import sleep
while True:
    while True:
        #Vamos embelezar esse codigo agora Denis
        print('=-'*15)
        print("Bem vindo!".center(30))
        print('=-'*15)
        try:
            #Primeiro obtemos os valores de cada lado do traingulo
            v1 = int(input('Digite o primeiro valor: '))
            v2 = int(input('Digite o segundo valor: '))
            v3 = int(input('Digite o terceiro valor: '))
            break
        except ValueError:
            print("\033[31mDigite um número válido!\033[0m")
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

    #Faremos a verificação para decobrir se o triangulo é possivel
    if (v1+v2 > v3) and (v2+v3 > v1) and (v1+v3 > v2):
        print("\033[32mÉ posivel formar um triangulo\033[0m")
    else:
        print("\033[31mNão é posivel formar um triangulo\033[0m")
    print('=-'*15)
    #Apos a verificação perguntamos se o usuario gostaria de tentar novamente
    novamente = str(input("Deseja tentar novamente? \n[1] Sim\n[2] Não\nDigite sua respota:  ")).lower().strip()
    if novamente == '1' or novamente == 's':
        print("Boa consulta!")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif novamente == '2' or novamente =='n':
        print("Obrigado por usar nosso sitema de verificação de triangulos. Até a próxima terraqueo.")
        sleep(2)
        break
