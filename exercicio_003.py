import os

def calculo(nota_1, nota_2, nota_3):
    media = (nota_1 + nota_2 + nota_3) / 3
    if media < 7:
        return f'A média foi {media:.2f}, o aluno foi REPROVADO.'
    else:
        return f'A média foi {media:.2f}, o aluno foi APROVADO!'

    
try:
    while True:
        try:
            print('Calculadora de média')
            nota_1 = float(input('Digite a primeira nota: '))
            nota_2 = float(input('Digite a segunda nota: '))
            nota_3 = float(input('Digite a terceira nota: '))

            if 0 < nota_1 > 10:
                print('A primeira nota está fora do intervalo permitido (0 a 10). Tente novamente.')
                continue
            if 0 < nota_2 > 10:
                print('A segunda nota está fora do intervalo permitido (0 a 10). Tente novamente.')
                continue
            if 0 < nota_3 > 10:
                print('A terceira nota está fora do intervalo permitido (0 a 10). Tente novamente.')
                continue

        except ValueError:
            print('Você precisa digitar um número válido.')
        
        resultado = calculo(nota_1, nota_2, nota_3)
        print(resultado)

        sair = input('Digite [S] para sair ou [C] para continuar: ').strip().lower()

        if sair == 's':
            print('Encerrando o programa! Até logo...')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    


except KeyboardInterrupt:
    print('Programa encerrado pelo usuário!')
