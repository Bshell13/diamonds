import pandas as pd
import seaborn as sns

data = sns.load_dataset('diamonds')

df = pd.DataFrame(data)

print(data.dtypes)
print(df.dtypes)