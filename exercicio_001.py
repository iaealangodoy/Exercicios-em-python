import os

def calculo(numero_1, numero_2):
      return numero_1 + numero_2


try:
    while True:
        print('Vamos somar dois números?') 
        try:   
            numero_1 = int(input('Digite o primeiro número: '))
            numero_2 = int(input('Digite o segundo número: '))

        except ValueError:
            print('Entrada inválida! Por favor, digite números inteiros.')
            continue


        resultado = calculo(numero_1, numero_2)
        print(f'A soma entre {numero_1} + {numero_2}= {resultado}')

        sair = input('Você pode encerrar o programa digitando [S]air ou [C]ontinuar: ').strip().lower()

        if sair == 's':
              print('Encerrando o programa, Até logo!')
              break       
        
        else:
             os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
        print('Programa encerrado pelo usuário')