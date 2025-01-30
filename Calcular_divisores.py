def obtener_numero_natural():
    while True:
        try:
            num = int(input("Ingrese un número natural: "))
            if num <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            return num
        except ValueError as e:
            print(f"Error: {e}. Inténtelo nuevamente.")

def calcular_divisores(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def main():
    numero = obtener_numero_natural()
    divisores = calcular_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")

if __name__ == "__main__":
    main()
