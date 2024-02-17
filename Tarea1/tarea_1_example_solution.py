def numero_primo(base):
    if isinstance(base, bool):  # verifica si base es un booleano
        return -64, None  # retorna error
    elif isinstance(base, int) and base >= 0:  # verifica base es número entero
        if base <= 100:  # verifica base es número entero menor o igual a 100
            cont = 2  # declara variable cont
            listaPrimos = []  # declara arreglo listaPrimos
            while cont <= base:  # mientras cont sea menor o igual a base
                esPrimo = True  # declara esPrimo verdadero
                for i in range(2, cont):  # para rango de numeros de 2 a cont
                    if (cont % i) == 0:  # cont no es divisible entre el numero
                        esPrimo = False  # de ser divisible se pone en falso
                        break
                if esPrimo:
                    listaPrimos += [cont]  # listaPrimos registra a cont
                cont += 1  # se incrementa en uno cont
            return 0, listaPrimos  # retorna listaPrimos
        else:
            return -80, None  # se retorna error
    else:
        return -64, None  # se retorna error


def invert_case(Cadena):
    if isinstance(Cadena, str):  # verificar que Cadena sea tipo string
        if Cadena != '':  # verificar que Cadena sea diferente a string vacio
            if Cadena.isalpha():  # verifica tener carácteres del abecedario
                stringInverso = ''  # se declara stringInverso
                for i in Cadena:  # se recorre cada carácter de Cadena
                    if i.isupper():  # valida si la letra está en mayúscula
                        stringInverso += i.lower()  # almacena en minúscula
                    else:
                        stringInverso += i.upper()  # almacena en mayúscula
                return 0, stringInverso  # se retorna stringInverso
            else:
                return -32, None  # se retorna el error
        else:
            return -48, None  # se retorna el error
    else:
        return -16, None  # se retorna error
