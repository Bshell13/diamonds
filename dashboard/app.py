import pandas as pd
import seaborn as sns

from shiny import ractive, render
from shinyswatch import theme

df = sns.load_dataset('diamonds')

print(df.head())