def multiplicar_valores(*args):
    for valores in args:
        resultado *= valores
    return resultado

print(multiplicar_valores(5,6,7))