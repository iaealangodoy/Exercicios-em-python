import os

def par_impar(numero):
    eh_par = numero % 2 == 0
    return 'PAR' if eh_par else 'IMPAR'


try:
    while True:
        try:
            numero = int(input('Digite um número para saber se ele é PAR ou IMPAR: '))
        
        except ValueError:
            print('Você precisa digitar um número! Vamos continuar...')
            continue
        
        resultado = par_impar(numero)
        print(f'O número {numero} é {resultado}!')

        sair = input('Você pode digitar [S]air ou [C]ontinuar.').strip().lower()

        if sair == 's':
            print('Encerrando o programa! Até logo...')
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')

except KeyboardInterrupt:
    print('Programa encerrado pelo usuário!')