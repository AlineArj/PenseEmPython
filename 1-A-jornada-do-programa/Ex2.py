# Inicialize o interpretador do Python e use-o como uma calculadora.

# Quantos segundos há em 42 minutos e 42 segundos?
min = 42
seg = 42
seg_total = (min * 60) + seg
print(f'{seg_total} segundos')

# Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
km = 10
milha = km / 1.61
print(f'{milha:.2f} milhas')

# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
passo_medio_segundos = seg_total / milha

passo_medio_min = passo_medio_segundos // 60
passo_medio_seg = passo_medio_segundos % 60
print(f'Passo médio: Uma milha a cada {passo_medio_min} minutos e {passo_medio_seg:.1f} segundos ')

horas = seg_total / 3600
velocidade_media = milha / horas
print(f'A velocidade média é de {velocidade_media:.2f} milhas por hora')
