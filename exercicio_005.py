import os

def calculadora(numero_1, numero_2, operador):
        
            if operador == '+':
                adicao = numero_1 + numero_2
                return f'{numero_1} + {numero_2} = {adicao}'
            
            elif operador == '-':
                subtracao = numero_1 - numero_2
                return f'{numero_1} - {numero_2} = {subtracao}'
            
            elif operador == 'x':
                multiplicacao = numero_1 * numero_2
                return f'{numero_1} x {numero_2} = {multiplicacao}'
            
            elif operador == '/':
                if numero_2 == 0:
                    return 'Você não pode fazer divisão por 0'

            else:
                divisao = numero_1 / numero_2
                return f'{numero_1} / {numero_2} = {divisao}'


try:
    while True: 
        print('Calculadora Simples')  
        try:
            numero_1 = float(input('Digite o primeiro número para calcular: '))
            numero_2 = float(input('Digite o segundo número para calcular: '))
            operador = input('Digite um dos 4 operadores [+, -, x ou /]: ').strip()

            if operador not in ['+', '-', 'x', '/']:
                print('Você precisa digitar um operador válido [+, -, x ou /].')
                continue
        
        except ValueError:
            print('Você precisa digitar um valor válido!')
            continue
            
        resultado = calculadora(numero_1, numero_2, operador)
        print(resultado)

        sair = input('Digite [S] para sair ou [C] para continuar: ').strip().lower()

        if sair == 's':
            print('Encerrando o programa! Até logo...')
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')



except KeyboardInterrupt:
        print('O usuário interrompeu o programa!')