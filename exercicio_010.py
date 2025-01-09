import re
import os


try:
        while True:
            print('Verificador de Palíndromos')
            frase = input('Digite uma frase para descobrir se ela é um palíndromo ou não: ').lower().strip()
            frase_tratada = re.sub(r'[^aàáâãeèéêiìíîoóòôõuúùû]', '', frase)
            frase_invertida = frase_tratada[::-1]

            print(frase_tratada)
            print(frase_invertida)

            if len(frase_tratada) == 0:
                print('Você precisa digitar uma frase.')

            if frase_tratada == frase_invertida:
                print('É um palindromo')

            else:
                print('não é um palindromos')


            sair = input('Para encerrar o programa digite [S]im ou [N]ão: ').lower().strip()

            if sair == 's':
                print('Finalizando o programa.')
                break
                    
            else:
                os.system('cls' if os.name == 'nt' else 'clear' )

except ValueError:
    print('Erro inesperado')


