    # Escreva uma função que desenhe uma grade como a seguinte:

    #     + - - - - + - - - - +
    #     |         |         |
    #     |         |         |
    #     |         |         |
    #     |         |         |
    #     + - - - - + - - - - +
    #     |         |         |
    #     |         |         |
    #     |         |         |
    #     |         |         |
    #     + - - - - + - - - - +

def horizontal(tam):
    for _ in range(tam):
        print('+', end=' ')
        print('- ' * 4, end=' ')
    print('+')

def vertical(tam):
    for _ in range(4):
        for _ in range(tam+1):
            print('/', end=' ' * 10 )
        print()

def grade(tam_horizontal, tam_vertical):
    for _ in range(tam_vertical):
        horizontal(tam_horizontal)
        vertical(tam_horizontal)
    horizontal(tam_horizontal)

grade(7, 2)
