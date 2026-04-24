import os
from time import sleep

historico = []
sair = 0

while True:
    if sair == 1: break
    else: pass
    while True:
        #Vamos embelezar esse codigo agora Denis
        print('=-'*15)
        print("Bem vindo!".center(30))
        print('=-'*15)
        try:
            #Primeiro obtemos os valores de cada lado do triangulo
            v1 = float(input('Digite o primeiro valor: '))
            v2 = float(input('Digite o segundo valor: '))
            v3 = float(input('Digite o terceiro valor: '))
            break
        except ValueError:
            print("\033[31mDigite um número válido!\033[0m")
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

    #Faremos a verificação para decobrir se o triangulo é possivel
    if (v1+v2 > v3) and (v2+v3 > v1) and (v1+v3 > v2):
        res = 'POSSÍVEL'
        print(f"\033[32mÉ {res} formar um triangulo\033[0m")
    else:
        res = 'IPOSSÍVEL'
        print(f"\033[31mE {res} formar um triangulo\033[0m")

    historico.append(f'Lados: ({v1}, {v2}, {v3}) = Resultado: {res}')
    print('=-'*15)
    #Apos a verificação perguntamos se o usuario gostaria de tentar novamente
    while True:
        novamente = str(input("Deseja tentar novamente? \n[1] Sim\n[2] Não\nDigite sua respota:  ")).lower().strip()
        if novamente == '1' or novamente == 's':
            print("Boa consulta!")
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        elif novamente == '2' or novamente =='n':
            print("\n" + "="*30)
            print("HISTÓRICO DE CONSULTAS:")
            for item in historico:
                print(item)
            print("="*30)
            print("Obrigado por usar nosso sitema de verificação de triangulos. Até a próxima terraqueo.")
            sleep(2)
            sair = 1
            break
        
        else:
            print('\033[31mOpção INVALIDA tente novamente.\033[0m')
            sleep(2)



