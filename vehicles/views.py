import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table, cars_above_5000, total_price_by_manufacturer

def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_data_1000.csv")
    df = pd.DataFrame(queryset)

    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "cars_above_5000": cars_above_5000(df),
        "total_price_by_manufacturer": total_price_by_manufacturer(df),
    })
