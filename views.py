from flet import *
from pages.home import HomeScreen


def views_handler(page):
  return {

    '/home':View(
        route='/home',
        controls=[
          HomeScreen(page)
        ]
      ),
  }