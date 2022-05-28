# É uma boa ideia ler este livro em frente a um computador para testar os exemplos durante a leitura.
# Sempre que estiver testando um novo recurso, você deve tentar fazer erros. Por exemplo, no programa “Hello, World!”, o que acontece se omitir uma das aspas? E se omitir ambas? E se você soletrar a instrução print de forma errada?

# Este tipo de experimento ajuda a lembrar o que foi lido; também ajuda quando você estiver programando, porque assim conhecerá o significado das mensagens de erro. É melhor fazer erros agora e de propósito que depois e acidentalmente.

# a. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
# print'Olá, mundo!'
# -> SyntaxError: invalid syntax

# b. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
# string = 'Olá, mundo
# print(string)
# -> SyntaxError: EOL while scanning string literal

# c. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
# num = +2
# print(num)
# print(2+num)
# print(2++2)

# d. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
# num = 02
# print(num)
# -> SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# e. O que acontece se você tiver dois valores sem nenhum operador entre eles?
#print(3 4)
# -> SyntaxError: invalid syntax

# num1 = 3
# num2 = 4
# print(num1 num2)
# -> SyntaxError: invalid syntax
