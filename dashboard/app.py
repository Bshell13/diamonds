import pandas as pd
import seaborn as sns

from shiny import reactive, render
from shiny.express import input, ui
from shinyswatch import theme

data = sns.load_dataset('diamonds')
df = pd.DataFrame(data)

ui.page_opts(title="Diamonds Dataset")

with ui.sidebar():
    ui.input_checkbox_group(
        'cut',
        'Cut',
        {
            'Ideal': 'Ideal',
            'Premium': 'Premium',
            'Very Good': 'Very Good',
            'Good': 'Good',
            'Fair': 'Fair'
        },
    )
    ui.input_checkbox_group(
        'color',
        'Color',
        {
            'D': 'D',
            'E': 'E',
            'F': 'F',
            'G': 'G',
            'H': 'H',
            'I': 'I',
            'J': 'J'
        },
    )
    ui.input_checkbox_group(
        'clarity',
        'clarity',
        {
            'SI2': 'SI2',
            'SI1': 'SI1',
            'VS2': 'VS2',
            'VS1': 'VS1',
            'VVS2': 'VVS2',
            'VVS1': 'VVS1',
            'IF': 'IF',
            'FL': 'FL'
        },
    )
    ui.input_slider(
        'carat',
        'Carat',
        min=df['carat'].min(),
        max=df['carat'].max(),
        value=[0.5, 2.0],
        step=0.01
    )

with ui.card():
    @render.data_frame
    def diamonds_datatable():
        return render.DataTable(filtered_data())

@reactive.calc
def filtered_data():
    filtered = df[df['cut'].isin(input.cut())]
    filtered = df[df['color'].isin(input.color())]
    filtered = df[df['clarity'].isin(input.clarity())]
    filtered = df[df['carat'].isin(input.carat())]
    return filtered