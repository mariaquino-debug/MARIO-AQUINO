paciente=[]
def mostrar_menu():
    print("\n====MENU====")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes")
    print("6. Salir")
    print("*******************")
def leer_opcion():
    while True:
        try:
            opcion=int(input("seleccione una opcion entre 1 y 6"))
            if 1 <= opcion <=6:
                return opcion
            print("ERROR:el numero ingresado debe estar entre 1 y 6")
        except ValueError:
            print("ERROR: debe ser un numero entero")
def validacion_de_nombre(nombre):
    return len(nombre.strip())>0
def validacion_de_edad(edad_sss):
    try:
        edad = int(edad_sss)
        return edad > 0
    except ValueError:
        return False
def validacion_de_temperatura(temperatura_sss):
    try:
        temperatura = float(temperatura_sss)
        return 35.0 <= temperatura <= 42
    except ValueError:
        return False
def agregar_paciente(lista_pacientes):
    print("\n =====AGREGAR PACIENTE=====")
    nombre_AAA =input("ingrese el nombre completo del paciente a registrar")
    if not validacion_de_nombre(nombre_AAA):
        print("ERROR:no puedo registrar el nombre del paciente por que: no puede estar vacío ni ser solo espacios en blanco.")
        return
    edad_AAA = input("ingresar la edad del paciente")
    if not validacion_de_edad(edad_AAA):
        print("ERROR:La edad del paciente debe ser un número entero mayor que cero.")
        return
    temperatura_AAA = input("ingrese la temperatura del paciente esta debe estar entre 35.0 y 42.0")
    if not validacion_de_temperatura(temperatura_AAA):
        print("ERROR:•	La temperatura debe ser un número decimal entre 35.0 y 42.0.")
        return
    nuevo_paciente ={
            "nombre":nombre_AAA.strip(),
            "edad":int(edad_AAA),
            "temperatura":float(temperatura_AAA),
            "atendid@":False
    }
    lista_pacientes.append(nuevo_paciente)
    print("se agrego con exito el paciente")
def buscar_paciente(lista_pacientes,nombre_buscar):
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i] ["nombre"] == nombre_buscar:
            return i
        return -1
def eliminar_pacientes(lista_pacientes):
    nombre_eliminar = input("ingrese el nombre del paciente que desea eliminar")
    posicion = buscar_paciente(lista_pacientes,nombre_eliminar)
    if posicion !=-1:
        lista_pacientes.pop(posicion)
        print("paciente eliminado correctamente")
    else:
        print(f"el paciente {nombre_eliminar}que desea eliminar bo se encuentra en la lista")                
def actualizar_estado(lista_pacientes):
    for paciente in lista_pacientes:
        if paciente["temperatura"] <= 37:
            paciente["atenddido"]=True
        else:
            paciente["atenddido"]= False
def mostrar_pacientes(lista_pacientes):
    actualizar_estado(lista_pacientes)
    print("\n=====LISTA DE PACIENTES=====")
    if len(lista_pacientes) == 0:
        print ("no ahi pacientes registrados en el sistema")
        return
    for paciente in lista_pacientes:
     estado=("ATENDIDO" if paciente["atendido"] else "REQUIERE ATENCION")
    print(f"nombre{paciente["nombre"]}")
    print(f"edad:{paciente["edad"]}")
    print(f"temperatura:{paciente["temperatura"]}")
    print(f"estado:{estado}")
    print("============================")
    while True:
        mostrar_menu()
        opcion=leer_opcion()
        if opcion == 1:
            agregar_paciente(paciente)
        elif opcion == 2:
            print("\n=====BUSCAR PACIENTE=====")
            nombre_a_buscar=input("ingrese el nombre que desea buscar")
            posicion=buscar_paciente(paciente,nombre_a_buscar)
            if posicion !=-1:
                paciente=paciente[posicion]
            estado=("ATENDIDO" if paciente["atendido"] else "REQUIERE ATENCION")
            print(f"\n[paciente encontrado en la posicion{posicion}")
            print(f"nombre:{paciente["nombre"]}")
            print(f"edad:{paciente["edad"]}")
            print(f"temperatura:{paciente["temperatura"]}")
            print(f"estado:{estado}")
        else:
            print("ERROR:paciente no encontrado")
        if opcion == 3:
            eliminar_pacientes(paciente)
        elif opcion ==4:
            actualizar_estado(paciente)
            print("estado de todos los pacientes actualizados")
        elif opcion == 5:
            mostrar_pacientes(paciente)
        elif opcion == 6:
            print("gracias por usar el sistema vuelva pronto")
            break