def show_results(departamento, municipio, cultivo, limit, medians):
    
    print(f"Resultados para {cultivo} en {municipio}, {departamento}:")
    print("     ")
    print(f"Numero de registros consultados: {limit}")
    print("Media de variables :")
    for variable, median in medians.items():
        print(f"{variable}: {median:.2f}")