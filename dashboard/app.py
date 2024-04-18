import pandas as pd
import seaborn as sns
import plotly.express as px

from shiny import reactive, render
from shiny.express import input, ui
from shinyswatch import theme
from shinywidgets import render_plotly

theme.darkly()

diamonds_df = pd.DataFrame(sns.load_dataset('diamonds'))

ui.page_opts(title="Diamonds Dataset")

with ui.sidebar():
    ui.h3('Select Characteristics')
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
        selected=['D'],
        inline=True
    )
    ui.input_checkbox_group(
        'clarity',
        'Clarity',
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
        selected=['SI2'],
        inline=True
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
        @render_plotly
        def depth_table_plot():
            fig_1 = px.scatter(
                filtered_data(),
                x='table',
                y='depth',
                color='cut',
                title="Depth vs. Table",
                labels={'depth': "Depth (mm)",
                        'table': 'Table sidth (mm)'}
            )
            return fig_1

with ui.layout_columns():
    with ui.card():
        @render.plot(alt="Seaborn histogram of price")
        def price_plot():
            ax = sns.histplot(
                data=filtered_data(),
                x='price',
                bins=30
            )

    with ui.card():
        @render_plotly
        def altair_plot():
            fig_2 = px.histogram(
                filtered_data(),
                x='price',
                nbins=30,
                title='Price by Chacteristics',
                labels={'price': 'Price ($)'}
            )
            return fig_2

@reactive.calc
def filtered_data():
    carat_bounds = list(input.carat())
    
    filtered_first = diamonds_df[diamonds_df['color'].isin(input.color())]
    filtered_second = filtered_first[filtered_first['clarity'].isin(input.clarity())]
    filtered_final = filtered_second[(filtered_second['carat'] >= carat_bounds[0]) & (filtered_second['carat'] <= carat_bounds[1])]
    return filtered_final