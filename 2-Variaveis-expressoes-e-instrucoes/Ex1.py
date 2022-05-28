# Repetindo o meu conselho do capítulo anterior, sempre que você aprender um recurso novo, você deve testá-lo no modo interativo e fazer erros de propósito para ver o que acontece.

# Vimos que n = 42 é legal. E 42 = n?
# 42 = n
# print(n)
# -> SyntaxError: cannot assign to literal

# Ou x = y = 1?
# x = y = 1
# print(f'x: {x}\ny: {y}')

# Em algumas linguagens, cada instrução termina em um ponto e vírgula ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução no Python?
# num1 = 7;
# num2 = 3;
# print(f'Soma de {num1} + {num2} = {num1+num2}');
# Não acontece nada

# E se puser um ponto no fim de uma instrução?
num1 = 7
num2 = 3
# print(f'Soma de {num1} + {num2} = {num1+num2}').
# -> SyntaxError: invalid syntax

# Em notação matemática é possível multiplicar x e y desta forma: xy. O que acontece se você tentar fazer o mesmo no Python?
#print(f'{num1num2}')
# NameError: name 'num1num2' is not defined
