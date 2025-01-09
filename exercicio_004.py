import os

def verificador_triangulo(comprimento_1, comprimento_2, comprimento_3):
    if comprimento_1 + comprimento_2 > comprimento_3 and comprimento_2 + comprimento_3 > comprimento_1 and comprimento_3 + comprimento_1 > comprimento_2:

        if comprimento_1 == comprimento_2 == comprimento_3:
            return 'Os valores que você digitou FORMAM um triângulo EQUILÁTERO!'
                
        elif comprimento_1 == comprimento_2 or comprimento_2 == comprimento_3 or comprimento_3 == comprimento_1:
            return 'Os valores que você digitou FORMAM um triângulo ISÓSCELES!'
                
        else:
            return 'Os valores que você digitou FORMAM um triângulo ESCALENO!'
            
    else:
        return 'Os valores que você digitou NÃO FORMAM um triângulo'


try:
    while True:
        print('Verificador de Triângulo')
        print('Digite 3 valores para saber se eles formam um triângulo.')
        try:
            comprimento_1 = float(input('Digite o primeiro comprimento: '))
            comprimento_2 = float(input('Digite o segundo comprimento: '))
            comprimento_3 = float(input('Digite o terceiro comprimento: '))

        except ValueError:
            print('Você precisa digitar um valor válido!')
            continue

        resultado = verificador_triangulo(comprimento_1, comprimento_2, comprimento_3)
        print(resultado)

        sair = input('Digite [S] para sair ou [C] para continuar: ').strip().lower()

        if sair == 's':
            print('Encerrando o programa! Até logo...')
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    print('O usuário interrompeu o programa!')
