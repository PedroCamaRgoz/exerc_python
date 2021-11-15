def Menu():
    print(" Conversor de Temperatura ")
    print("1 -  Converter de Celsius para Fahrenheit ")
    print("2 -  Converter de Fahrenheit para Celsius ")

def cel_fahr():
    c = float( input (" Digite a temperatura em Celsius:  "))
    f = (c * 1.8) + 32
    print(" Valor em Fahrenheit: {0} ºF".format(f))


def fahr_cel():
    f = float( input (" Digite a temperatura em Fahrenheit:  "))
    c = ( f - 32) * 0.55
    print(" Valor em Celsius : {0} ºC".format(c))

if __name__ == '__main__':                                 # sem bibliotecas externas
    Menu()
    escolha = input("Escolha o tipo de conversão:  ")

    if escolha == '1':
         cel_fahr()
    if escolha == '2': 
         fahr_cel()