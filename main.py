def selectprog():
    programa = int(input(
    """
    Secuencia de Fibonacci - Selecciona una opcion(0 para salir):
    1- Encuentra el enesimo termino
    2- Calcula el termino mayor o igual al introducido
    """))
    if programa == 1:
        n = int(input("Introduce un termino a encontrar: "))
        resultado = secuencia(n)
        print("El numero con el término", n, "es:", resultado)
        exit("Programa finalizado...")

    elif programa == 2:
        secuenciados()

    else:
        exit("Saliendo del programa...")


def secuencia(n):
    if n <= 0:
        exit("Necesito que n sea positivo")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-1]

def secuenciados():
    n = int(input("Escribe un numero: "))
    if n <= 1:
        print("Por favor introduce un numero mayor que 1.")
        return
    

    fibonacci = [0, 1]
    while (fibonacci[-1]) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print("El primer numero mayor o igual que el introducido es: ", fibonacci[-1])
    exit("Programa finalizado...")

if __name__ == "__main__":

    selectprog()
  
    secuenciados()
