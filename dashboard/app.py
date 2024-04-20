import pandas as pd
import seaborn as sns
import plotly.express as px
import math

from shiny import reactive, render
from shiny.express import input, ui
from shinyswatch import theme
from shinywidgets import render_plotly

theme.darkly()

diamonds_df = pd.DataFrame(sns.load_dataset('diamonds'))

# Estimated Volume of a diamond using the cone formula.
pi = math.pi
diamonds_df['rough_volume'] = round(pi * (((diamonds_df['x'] + diamonds_df['y']).mean()) / 2)**2 * (diamonds_df['z'] / 3), 2)

ui.page_opts(title="Diamonds Dataset")

with ui.sidebar():
    ui.h3('Select Characteristics')
    ui.input_checkbox_group(
        'color',
        'Color',
        {
            'J': 'J',
            'I': 'I',
            'H': 'H',
            'G': 'G',
            'F': 'F',
            'E': 'E',
            'D': 'D',
        },
        selected=['J'],
        inline=True
    )
    ui.input_checkbox_group(
        'clarity',
        'Clarity',
        {
            'I1': 'I1',
            'SI2': 'SI2',
            'SI1': 'SI1',
            'VS2': 'VS2',
            'VS1': 'VS1',
            'VVS2': 'VVS2',
            'VVS1': 'VVS1',
            'IF': 'IF',
        },
        selected=['I1'],
        inline=True
    )

with ui.layout_columns():
    with ui.card():
        @render.data_frame
        def diamonds_datatable():
            return render.DataTable(filtered_data(), height='150px')

with ui.layout_columns():
    with ui.navset_card_tab(title='Price Graphs'):
        with ui.nav_panel('Estimated Volume'):
            @render_plotly
            def volume_scatter():
                price_volume_scatter = px.scatter(
                    filtered_data(),
                    x='price',
                    y='rough_volume',
                    color='cut',
                    title='Price vs. Estimated Volume',
                    labels={'price': 'Price ($)',
                            'rough_volume': 'Volume Estimated (mm^3)'}
                )
                return price_volume_scatter

        with ui.nav_panel('Carat'):
            @render_plotly
            def carat_scatter():
                price_carat_scatter = px.scatter(
                    filtered_data(),
                    x='price',
                    y='carat',
                    color='cut',
                    title='Price vs. Carat',
                    labels={'price': 'Price ($)',
                            'carat': 'Carat'}
                )
                return price_carat_scatter

    with ui.navset_card_tab(title='Histograms'):
        with ui.nav_panel('Price'):
            @render_plotly
            def price_hist():
                price_histogram = px.histogram(
                    filtered_data(),
                    x='price',
                    nbins=30,
                    title='Price by Chacteristics',
                    labels={'price': 'Price ($)'}
                )
                return price_histogram
        
        with ui.nav_panel('Estemated Volume'):
            @render_plotly
            def volume_hist():
                volume_histogram = px.histogram(
                    filtered_data(),
                    x='rough_volume',
                    nbins=30,
                    title='Estimated Volume by Chacteristics',
                    labels={'rough_volume': 'Estimated Volume (mm^3)'}
                )
                return volume_histogram

        with ui.nav_panel('Carat'):
            @render_plotly
            def carat_hist():
                carat_histogram = px.histogram(
                    filtered_data(),
                    x='carat',
                    nbins=30,
                    title='Carats by Chacteristics',
                    labels={'carat': 'Carats'}
                )
                return carat_histogram

@reactive.calc
def filtered_data():
    
    filtered_first = diamonds_df[diamonds_df['color'].isin(input.color())]
    filtered_second = filtered_first[filtered_first['clarity'].isin(input.clarity())]
    return filtered_second