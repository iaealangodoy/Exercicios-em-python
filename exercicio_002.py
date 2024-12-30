try:
    numero = int(input('Digite um número para saber se ele é PAR ou IMPAR: '))
    
    calculo = numero % 2

    if calculo == 0:
        print(f'O número {numero} é PAR.')
    else:
        print(f'O número {numero} é IMPAR.')

except ValueError:
    print('Você precisa digitar um número válido.')