def verificar_divisibilidad_residuo_y_division(numero):
    try:
        if numero <= 0 or numero > 100:  # numero menor o igal a cero o numero mayor a cien
            raise ValueError("El número debe ser positivo, mayor que 0 y menor o igual a 100.")
        
        if numero % 2 == 0:  # si el modulo entre dos es igual cero
            print(f"{numero} es divisible por 2.")
            residuo = numero % 2
            division = numero / 2
            print(f"El residuo al dividir {numero} por 2 es: {residuo}")
            print(f"El resultado de dividir {numero} por 2 es: {division}")
        else:
            print(f"{numero} no es divisible por 2.")
    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo de uso
try:
    numero_ingresado = int(input("Ingresa un número: "))
    verificar_divisibilidad_residuo_y_division(numero_ingresado)
except ValueError:
    print("Error: Ingresa un número entero válido.")
except Exception as e:
    print(f"Error inesperado: {e}")
