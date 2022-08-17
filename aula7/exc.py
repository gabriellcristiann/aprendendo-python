from datetime import date

nome = 'Janilson Messias'
idade = 32
altura = 1.75
e_maior = idade > 18
peso = 80.5
imc = peso / (altura ** 2)
ano_atual = date.today().year - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso:.0f}Kg.')
print(f'O IMC de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_atual}')