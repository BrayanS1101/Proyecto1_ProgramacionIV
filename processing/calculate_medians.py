import pandas as pd
import numpy as np

def calculate_medians(data):
    # Verifica si hay valores "ND" en las columnas
    print("Datos con valores 'ND':")
    print(data[data.isin(["ND"]).any(axis=1)])

    numeric_cols = data.select_dtypes(include=[np.number, 'float64', 'int64']).columns
    df = data.copy()

    for col in numeric_cols:
        df[col] = df[col].replace("ND", np.nan).astype(float)

    medians = {}

    if 'ph' in df.columns:
        medians['pH'] = df['ph'].median(skipna=True)
    if 'fosforo_p' in df.columns:
        medians['Fósforo'] = df['fosforo_p'].median(skipna=True)
    if 'potasio_k' in df.columns:
        medians['Potasio'] = df['potasio_k'].median(skipna=True)
    
    return medians
