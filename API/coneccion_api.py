import pandas as pd
from sodapy import Socrata

def get_api_data():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", limit=2000)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df

results = get_api_data()
print(results)


