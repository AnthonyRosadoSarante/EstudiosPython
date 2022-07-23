def run():
    valor = input("coloca un numero para saber si es primo")
    valor = float
    resultado = []
    for i in range(2, valor):
        if i % 2 != 0:
            resultado.append(i**2)


if __name__ == '__main__':
    run()