
def ejer1PedirNombreUser():
    nombre = input("Ingrese su nombre: ")
    cantRepetir= input("Cuantas veces se repetira: ")
    print((nombre+"\n")*int(cantRepetir))

if __name__ == '__main__':
    ejer1PedirNombreUser()