from flet import *
from utils.extras import Colors
class MainBody(UserControl):
  def __init__(self):
    super().__init__()
    self.custom_colors = Colors()


  def build(self):
    return Column(
      controls=[
        Container(
          padding=padding.only(top=35,left=30,bottom=2,right=30),
          content=Column(
            controls=[
              Row(
                alignment='spaceBetween',
                controls=[
                  Column(
                    spacing = 0,
                    controls=[
                      Text('Dashboard',color='black'),
                      Text('Payments updates',color='black'),
                    ]
                  ),
                  Container(
                    alignment=alignment.center,
                    bgcolor=self.custom_colors.white,
                    height=35,
                    width=250,
                    border_radius=20,
                    content=Row(
                      controls=[
                        Icon(icons.SEARCH_OUTLINED),
                        TextField(
                          width=200,
                          bgcolor=None,
                          border=None
                        )
                      ]
                    )
                  )
                ]
              )
            ]
          )
        )
      ]
    )