def get_user_data():
    departamento = input("Ingrese el Departamento: ")
    municipio = input("Ingrese el Municipio: ")
    cultivo = input("Ingrese el cultivo: ")
    
    while True:
        try:
            limit = int(input("Ingrese la cantidad de registros a consultar: "))
            if limit > 0:
                break
            else:
                print("Debe ser mayor a CERO.")
        except ValueError:
            print("Intente de nuevo")
    
    return departamento, municipio, cultivo, limit