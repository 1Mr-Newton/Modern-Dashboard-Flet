from flet import * 
from utils.extras import Size, Colors
from pages.left_sidebar import LeftSidebar
from pages.dashboard import Dashboard

def main(page: Page):
  def helper():
    page.fonts = {
      "SF Pro Bold":"fonts/SFProText-Bold.ttf",
      "SF Pro Heavy":"fonts/SFProText-Heavy.ttf",
      "SF Pro HeavyItalic":"fonts/SFProText-HeavyItalic.ttf",
      "SF Pro Light":"fonts/SFProText-Light.ttf",
      "SF Pro Medium":"fonts/SFProText-Medium.ttf",
      "SF Pro Regular":"fonts/SFProText-Regular.ttf",
      "SF Pro Semibold":"fonts/SFProText-Semibold.ttf",
      "SF Pro SemiboldItalic":"fonts/SFProText-SemiboldItalic.ttf",
    }
    

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.window_min_width = sizes.main_width
    page.window_min_height = sizes.main_height

    page.window_height = sizes.main_height
    page.window_width = sizes.main_width

  def click_handler(e: Event):
    print('clicked')

  dashboard = Dashboard()
  left_sidebar = LeftSidebar()
  sizes = Size()
  custom_colors = Colors()
  helper()





  left_sidebar = Container(
    padding=padding.only(top=20),
    bgcolor=custom_colors.grey300,
    width=80,
    content=Column(
      spacing=10,
      controls=[
        left_sidebar
      ]
    )
  )
  main_body = Container(
    bgcolor=custom_colors.main_bg,
    expand=True,
    content=Column(
      controls=[
        WindowDragArea(
          content=Container(
            height=30,
            expand=True,
          ),
        ),
        Stack(
          controls=[
            dashboard,
          ]
        )
      
      ]
    )
  )
  right_sidebar = Container(
    width=250,
    bgcolor=custom_colors.grey300,
  )

  page.add(
      Container(
        # padding=25,
        bgcolor=custom_colors.white,
        expand=True,
        content=Row(
          alignment='spaceBetween',
          spacing=0,
          controls=[
            left_sidebar,
            main_body,
            right_sidebar
          ]
        )
      )
  )


app(target=main,assets_dir='assets')