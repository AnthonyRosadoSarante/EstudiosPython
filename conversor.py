menu = """Este es un Convensor de monedas

1 - pesos dominicanos
2 - pesos colombianos
3 - pesos argentinos
4 - pesos mexicanos

------------------------>:"""
opcion = int(input(menu))
def opciones(valor_dolar, tipo_pesos):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    if dolares >= 1000000:
        millonario = 1
    else:
        millonario = 0
    dolares = str (dolares)
    print("tienes $" + dolares + " dolares")
    if millonario == 1:
        print("Eres millonario")
    else:
        print("Aun no eres millonario")


if opcion == 1:
    opciones(54, "dominicanos")
elif opcion == 2:
    opciones(3875, "colombianos")
elif opcion == 3:
    opciones(65, "argentinos")
elif opcion == 4:
    opciones(24, "mexicanos")
else :
    print("Ingresa un valor correcto por favor")