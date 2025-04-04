def selectprog():
    programa = int(input(
    """
    Secuencia de Fibonacci - Selecciona una opcion:
    1- Encuentra el enesimo termino
    2- Calcula el termino mayor o igual al introducido
    """))


def secuencia(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci[-1])

secuencia(11)

def secuenciados():
    n = int(input("Escribe un numero: "))
    if n <= 1:
        print("Por favor introduce un numero mayor que 1.")
        return
    

    fibonacci = [0, 1]
    while (fibonacci[-1]) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        print(fibonacci)
    print("El primer numero mayor o igual que el introducido es: ", fibonacci[-1])

selectprog()
secuencia(11)   
secuenciados()


