import pandas as pd
import seaborn as sns

data = sns.load_dataset('diamonds')

diamonds_df = pd.DataFrame(data)

carat_max = diamonds_df['carat'].max()
carat_min = diamonds_df['carat'].min()

carat_bounds = (carat_min, carat_max)
def filtered_data(carat_min, carat_max):
   
    filtered = diamonds_df[diamonds_df['cut'].isin('Good')]
    filtered = diamonds_df[diamonds_df['color'].isin('E')]
    filtered = diamonds_df[diamonds_df['clarity'].isin('SI2')]
    filtered = diamonds_df[(diamonds_df['carat'] >= carat_min) & (diamonds_df['carat'] <= carat_max)]
    return filtered

filtered = filtered_data(carat_min, carat_max)

print(filtered.head())
