import os

def media(lista):
    soma = 0
    for numero in lista:
        soma += numero

    divisao = soma / len(lista)
    

    acima_media = []
    for num in lista:
        if num > divisao:
            acima_media += [num]

    print(f'A média é: {divisao:.2f}')
    print(f'Números acima da média: {acima_media}')
    

try:
        while True:
            print('Calculadora de Média de Números')
            numeros = input('Digite uma lista de números separados por espaço: ').split()

            if not numeros:
                print('Você precisa digitar pelo menos um número')
                continue

            try:
                lista = []
                for numero in numeros:
                    numero = float(numero)
                    lista += [numero]
            except ValueError:
                print('Digite apenas números válidos!')
                continue

            media(lista)

            sair = input('Para encerrar o programa digite [S]im ou [N]ão: ').lower().strip()

            if sair == 's':
                print('Finalizando o programa.')
                break
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear' )



except ValueError:
    print('Ocorreu um erro de valor. Certifique-se de digitar números válidos!')






    




    


