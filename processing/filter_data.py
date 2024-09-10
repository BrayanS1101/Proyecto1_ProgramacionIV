def filter_results(results_df, departamento, municipio, cultivo, limit):
    filtered_results = results_df[
        (results_df['departamento'].str.lower() == departamento.lower()) &
        (results_df['municipio'].str.lower() == municipio.lower()) &
        (results_df['cultivo'].str.lower() == cultivo.lower())
    ].head(limit)
    
    return filtered_results