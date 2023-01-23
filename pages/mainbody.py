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
                      Text(
                        value='Dashboard',
                        color=self.custom_colors.grey800,
                        size=20,
                        font_family='SF Pro Heavy'
                      ),
                      Text(
                        value='Payments updates',
                        color=self.custom_colors.grey400,
                        size=12,
                        font_family='SF Pro Regular'
                      ),
                    ]
                  ),
                  Container(
                    alignment=alignment.center,
                    bgcolor=self.custom_colors.white,
                    height=35,
                    width=250,
                    border_radius=20,
                    padding=padding.only(left=10),
                    content=Row(
                      controls=[
                        Container(
                          content=Icon(icons.SEARCH_OUTLINED,color=self.custom_colors.grey800),
                        ),
                        TextField(
                          width=200,
                          bgcolor=None,
                          border=InputBorder.NONE,
                          color=self.custom_colors.grey800,
                          hint_text='Search',
                          hint_style=TextStyle(color=self.custom_colors.grey400,),
                        )
                      ]
                    )
                  )
                ]
              ),

              Row(
                scroll='auto',
                alignment='spaceBetween',
                controls=[
                  Container(),

                ]
              )
            ]
          )
        )
      ]
    )