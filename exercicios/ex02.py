
# numero_inteiro = input('Digite um número inteiro: ')

# if numero_inteiro.isdigit():
#     numero_inteiro = int(numero_inteiro)
#
#     if numero_inteiro % 2 == 0:
#         print(f'{numero_inteiro} é par')
#     else:
#         print(f'{numero_inteiro} é impar')
# else:
#     print('Isso não é um número inteiro')

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t).split(':')

current_time = input('input number: ')

current_time = [current_time]

if current_time[0] <= '11':
    print('Bom dia')
elif current_time[0] <= '17':
    print('Boa Tarde')
else:
    print('Boa Noite')
