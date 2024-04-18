import pandas as pd
import seaborn as sns

from shiny import reactive, render
from shiny.express import input, ui
from shinyswatch import theme

diamonds_df = pd.DataFrame(sns.load_dataset('diamonds'))

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
        min=diamonds_df['carat'].min(),
        max=diamonds_df['carat'].max(),
        value=[0.5, 2.0],
        step=0.01
    )

with ui.layout_columns():
    with ui.card():
        @render.data_frame
        def diamonds_datatable():
            return render.DataTable(filtered_data())
    
    with ui.card():
        @render.plot(alt="Seaborn scatterplot of depth vs. table")
        def depth_table_plot():
            ax = sns.scatterplot(
                data=filtered_data(),
                x='depth',
                y='table'
            )

@reactive.calc
def filtered_data():
    carat_bounds = list(input.carat())
    
    filtered_first = diamonds_df[diamonds_df['cut'].isin(input.cut())]
    filtered_second = filtered_first[filtered_first['color'].isin(input.color())]
    filtered_third = filtered_second[filtered_second['clarity'].isin(input.clarity())]
    filtered_final = filtered_third[(filtered_third['carat'] >= carat_bounds[0]) & (filtered_third['carat'] <= carat_bounds[1])]
    return filtered_final