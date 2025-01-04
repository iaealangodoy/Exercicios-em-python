import re
import os

while True:
    print('Contador de Vogais')
    frase = input('Digite uma frase: ').strip().lower()

    if not frase:
        print('Você precisa digitar uma frase!')
        continue
   
    vogais = len(re.sub(r'[^aàáâãeèéêiìíîoóòôõuúùû]', '', frase))
    
    print(f'Você digitou {vogais} vogais incluido os acentos')

    sair = input('Para encerrar o programa digite [S]im ou [N]ão: ').lower().strip()

    if sair == 's':
        print('Finalizando o programa.')
        break
    
    else:
        os.system('cls' if os.name == 'nt' else 'clear' )




