while True:   
    try:
        numero_1 = float(input('Digite o primeiro número para calcular: '))
        numero_2 = float(input('Digite o segundo número para calcular: '))
        operador = input('Digite um dos 4 operadores [+, -, x ou /]: ').strip()

        

        if operador not in ['+', '-', 'x', '/']:
            print('Você precisa digitar um operador válido [+, -, x ou /].')
            continue

        if operador == '+':
            adicao = numero_1 + numero_2
            print(f'{numero_1} + {numero_2} = {adicao}')
        
        elif operador == '-':
            subtracao = numero_1 - numero_2
            print(f'{numero_1} - {numero_2} = {subtracao}')
        
        elif operador == 'x':
            multiplicacao = numero_1 * numero_2
            print(f'{numero_1} x {numero_2} = {multiplicacao}')
        
        elif operador == '/':
            if numero_2 == 0:
                print('Você não pode fazer divisão por 0')

            else:
                divisao = numero_1 / numero_2
                print(f'{numero_1} / {numero_2} = {divisao}')
            
        continuar = input('Você deseja fazer um novo calculo? [S]im ou [N]ão: ').lower().strip()

        if continuar == 'n':
            print('Finalizando a calculadora!')
            break



    except ValueError:
        print('Você precisa digitar um valor válido!')
        continue