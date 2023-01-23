import plotly.express as px
import flet as ft
from flet.plotly_chart import PlotlyChart
import pandas as pd, numpy as np, plotly.express as px



def main(page: ft.Page):
    x = np.random.random(50)
    y = np.random.random(50)
    fig = px.scatter(x,y)
    # df = px.data.gapminder().query("continent == 'Oceania'")
    # fig = px.bar(
    #     df,
    #     x="year",
    #     y="pop",
    #     hover_data=["lifeExp", "gdpPercap"],
    #     color="country",
    #     labels={"pop": "population of Canada"},
    #     height=400,
    # )

    px.scatter(x,y)
    page.add(
        ft.Container(
            bgcolor='green',
            height=800,
            width=800,
            content=PlotlyChart(fig,)

        ),
        )

ft.app(target=main)



# import pandas as pd, numpy as np, plotly.express as px

# x = np.random.random(50)
# y = np.random.random(50)
# fig = px.scatter(x,y)
# fig.show()
