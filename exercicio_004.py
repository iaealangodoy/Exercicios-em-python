print('Digite 3 valores para saber se eles formam um triângulo.')

try:
    comprimento_1 = float(input('Digite o primeiro comprimento: '))
    comprimento_2 = float(input('Digite o segundo comprimento: '))
    comprimento_3 = float(input('Digite o terceiro comprimento: '))

    if comprimento_1 + comprimento_2 > comprimento_3 and comprimento_2 + comprimento_3 > comprimento_1 and comprimento_3 + comprimento_1 > comprimento_2:

        if comprimento_1 == comprimento_2 == comprimento_3:
            print('Os valores que você digitou FORMAM um triângulo EQUILÁTERO!')
        
        elif comprimento_1 == comprimento_2 or comprimento_2 == comprimento_3 or comprimento_3 == comprimento_1:
            print('Os valores que você digitou FORMAM um triângulo ISÓSCELES!')
        
        else:
            print('Os valores que você digitou FORMAM um triângulo ESCALENO!')
    
    else:
        print('Os valores que você digitou NÃO FORMAM um triângulo')

except ValueError:
    print('Você precisa digitar um valor válido!')
