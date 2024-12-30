try:
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    nota_3 = float(input('Digite a terceira nota: '))

except ValueError:
    print('Você precisa digitar um número válido.')

else:
    media = (nota_1 + nota_2 + nota_3) / 3

    if media < 7:
        print(f'A média foi {media:.2f}, o aluno foi REPROVADO.')
    else:
        print(f'A média foi {media:.2f}, o aluno foi APROVADO!')
