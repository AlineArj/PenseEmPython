# Pratique o uso do interpretador do Python como uma calculadora:

# O volume de uma esfera com raio r é 4/3 * pi * r³. Qual é o volume de uma esfera com raio 5?
import math


r = 5
volume = (4 * math.pi * r ) /3
print(f'O volume da esfera de raio {r} u.m. é igual a {volume:.3f} u.v.')

# Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
preco_livro = 24.95
desconto = 0.4
transporte = 3
adicional = 0.75
copias = 60

custo_transporte = transporte + ((copias - 1) * adicional)
custo_livros = copias * (preco_livro * desconto)
custo_total = custo_transporte + custo_livros

print(f'O custo total é de R$ {custo_total:.2f}.')

# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?
from datetime import datetime, time, timedelta


hora_saida = datetime(1, 1, 1, 6, 52, 0)
quilometros_devagar = 2
quilometros_rapido = 3
print(f'Saída de casa às {hora_saida.time()}')

temp_devagar = timedelta(minutes=8, seconds=15) * quilometros_devagar
temp_rapido = timedelta(minutes=7, seconds=12) * quilometros_rapido

temp_corrida = temp_devagar + temp_rapido
hora_chegada = (hora_saida + temp_corrida).time()
print(f'Você chegará às {hora_chegada}')



