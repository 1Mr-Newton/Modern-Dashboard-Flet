import matplotlib
import matplotlib.pyplot as plt

import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")


def main(page: ft.Page):
  fig, ax = plt.subplots()
  fruits = ["apple", "blueberry", "cherry", "orange"]
  counts = [40, 100, 30, 55]
  ax.bar(fruits, counts)

 
  page.add(
    ft.Container(
      MatplotlibChart(fig)
    )
  )


ft.app(target=main)