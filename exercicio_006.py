import os

print('Conversor de temperatura.')
print('Aqui você pode converter a temperatura utilizando Celsius, Fahrenheit e Kelvin.')

try:
    while True:
        conversao_1 = input('Escreva de qual temperatura você quer converter (Celsius, Fahrenheit, Kelvin): ').strip().lower()
        conversao_2 = input('Escreva para qual temperatua o programa deve converter (Celsius, Fahrenheit, Kelvin): ').strip().lower()
        temperatura = float(input('Qual o valor da temperatura que você quer converter? '))
        
        if conversao_1[0] not in ['c', 'f', 'k'] or conversao_2[0] not in ['c', 'f', 'k']:
            print('Você digitou uma unidade de temperatura inválida. Use Celsius, Fahrenheit ou Kelvin.')
            continue

        indice_conversao_1 = conversao_1[0]
        indice_conversao_2 = conversao_2[0]

        if indice_conversao_1 == 'c' and indice_conversao_2 == 'f':
            resultado = temperatura * (9 / 5) + 32
            print(f'A conversão de {temperatura:.2f}C é {resultado:.2f}F.')
        
        elif indice_conversao_1 == 'c' and indice_conversao_2 == 'k':
            resultado = temperatura + 273.15
            print(f'A conversão de {temperatura:.2f}C é {resultado:.2f}K.')
        
        elif indice_conversao_1 == 'f' and indice_conversao_2 == 'c':
            resultado = (temperatura - 32) * (5 / 9)
            print(f'A conversão de {temperatura:.2f}F é {resultado:.2f}C.')
        
        elif indice_conversao_1 == 'f' and indice_conversao_2 == 'k':
            resultado = (temperatura - 32) * (5 / 9) + 273.15
            print(f'A conversão de {temperatura:.2f}F é {resultado:.2f}K.')
        
        elif indice_conversao_1 == 'k' and indice_conversao_2 == 'c':
            resultado = temperatura - 273.15
            print(f'A conversão de {temperatura:.2f}K é {resultado:.2f}C.')
        
        elif indice_conversao_1 == 'k' and indice_conversao_2 == 'F':
            resultado = (temperatura - 273.15) * (9 / 5) + 32
            print(f'A conversão de {temperatura:.2f}K é {resultado:.2f}f.')
        
        else:
            print('Você digitou algo de errado, verifique ao digitar.')
            continue
        
        
        saida = input('Você deseja fazer uma nova conversão? [S]im ou [N]ão:').strip().lower()
        indice_sair = saida[0]

        if indice_sair == 'n':
            print('Muito Obrigado, finalizando o programa.')
            break

        else:
            os.system('cls')
            

except ValueError:
    print('Você precisa digitar um valor válido')