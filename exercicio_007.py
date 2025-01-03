import os
try:
    while True:
        print('Calculadora de IMC (Índice de Massa Corporal)')

        try:

            peso = float(input('Digite o peso em quilogramas(kg): '))
            altura = float(input('Digite a altura em metros(m): '))

            if altura <= 0:
                print('A altura deve ser maior que zero.')
                continue

            imc = peso / (altura * altura)

            print(f'O IMC é {imc:.2f}.')

            if imc < 18.5:
                print('Abaixo do peso.')
            
            elif imc >= 18.5 and imc <= 24.9:
                print('Peso normal.')
            
            elif imc >= 25 and imc <= 29.9:
                print('Sobrepeso.')
            
            elif imc >= 30 and imc <= 34.9:
                print('Obesidade grau 1.')
            
            elif imc >= 35 and imc <= 39.9:
                print('Obesidade grau 2.')
            
            else:
                print('Obesidade grau 3')

        except ValueError:
            print('Você digitou um número inválido.')
            continue

        saida = input('Você quer executar um novo calculo?[S]im [N]ão: ').lower().strip()
    
        if saida == 'n':
            print('Muito Obrigado, finalizando o programa.')
            break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

        
except IndentationError:
    print('Erro não identificado')