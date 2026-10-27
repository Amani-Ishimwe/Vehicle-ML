import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go
import pandas as pd

def frequency_table(df):
    # Simple counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']
 
    # Convert to HTML using the correct method name: .to_html()
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm", 
        float_format='%.2f',
        justify='center'
    )
    return table_html

def cars_above_5000(df):
    # Filter cars where selling price is above 5000
    filtered_df = df[df['selling_price'] > 5000]

    # Convert to HTML
    table_html = filtered_df.to_html(
        classes="table table-bordered table-striped table-sm align-middle", 
        float_format='%.2f',
        justify='center',
        index=False
    )
    return table_html

def total_price_by_manufacturer(df):
   
    total_price = df.groupby('manufacturer')['selling_price'].sum().reset_index()
    total_price.columns = ['Manufacturer', 'Total Price']

    table_html = total_price.to_html(
        classes="table table-bordered table-striped table-sm align-middle",
        float_format='%.2f',
        justify='center',
        index=False
    )
    return table_html

def total_price_by_manufacturer(df):
    # Group by manufacturer and calculate total selling price
    total_price = df.groupby('manufacturer')['selling_price'].sum().reset_index()
    total_price.columns = ['Manufacturer', 'Total Price']

    # Convert to HTML
    table_html = total_price.to_html(
        classes="table table-bordered table-striped table-sm align-middle",
        float_format='%.2f',
        justify='center',
        index=False
    )
    return table_html

