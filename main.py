from API.coneccion_api import get_api_data
from processing.calculate_medians import calculate_medians
from processing.filter_data import filter_results
from UI.input_user_data import get_user_data
from UI.output_data import show_results

def main():
    # Obtener datos de la API
    results_df = get_api_data()

    
    departamento, municipio, cultivo, limit = get_user_data()

   
    filtered_results = filter_results(results_df, departamento, municipio, cultivo, limit)

    if filtered_results.empty:
        print("No se encontraron resultados para los criterios especificados.")
        return

    
    medians = calculate_medians(filtered_results)

    # Mostrar resultados
    show_results(departamento, municipio, cultivo, limit, medians)

if __name__ == "__main__":
    main()