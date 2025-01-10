import re
import os

def maior_menor(lista):
        
        maior = lista[0]
        menor = lista[0]
        for numero in lista:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        return maior, menor

def soma(lista):
        return sum(lista)

def par_impar(numero):        
        return 'PAR' if numero % 2 ==0 else 'IMPAR'


try:
    while True:
        numeros = input('Digite uma lista de números inteiros para o programa calcular: ').split()

        if not numeros:
             print('A lista não pode estar vazia')
             continue

        lista = []
        try:
            for numero in numeros:
                numero = int(numero)
                lista.append(numero)


        except ValueError:
            print('A lista deve conter apenas números separados por espaço.')
            continue
        
        maior, menor = maior_menor(lista)
        print(f'O maior número da lista é {maior}, já o menor número é {menor}')
        print(f'A soma dos números na lista é {soma(lista)}')
        print(f'O maior número é {par_impar(maior)}')

        
        sair = input('Digite [S] para sair ou [C] para continuar: ').strip().lower()

        if sair == 's':
            print('Encerrando o programa! Até logo...')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

except ValueError:
    print('Erro inesperado.')
