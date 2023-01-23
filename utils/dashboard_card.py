from flet import *
from utils.extras import Colors
class DashboardCard(UserControl):
  def __init__(self,icon,text,cash):
    super().__init__()
    self.icon = icon
    self.text = text
    self.cash = cash
    self.custom_colors = Colors()


  def build(self):
    return Column(
      controls=[
        Container(
          border_radius=25,
          height=150,
          width=150,
          bgcolor=self.custom_colors.white,
          padding=padding.only(top=20,left=20,right=20,bottom=10),
          content=Column(
            alignment='spaceBetween',
            controls=[
              Row(
                alignment='spaceBetween',
                controls=[
                  Icon(self.icon,color='black'),
                  Container(
                    content=Column(
                      alignment='center',
                      spacing=3,
                      controls=[
                        Container(
                          height=4,
                          width=4,
                          border_radius=10,
                          bgcolor=self.custom_colors.grey400,
                        ),
                        Container(
                          height=4,
                          width=4,
                          border_radius=10,
                          bgcolor=self.custom_colors.grey400,
                        ),
                      ]
                    )
                  )
                ]
              ),
              Container(
                content=Text(
                  value=self.text,
                  color='black'
                ),
              ),
              Container(
                content=Text(
                  value='$'+self.cash,
                  color='black',
                  size=17,
                  font_family='SF Pro Heavy',
                  

                ),
              ),
            ]
          )
        ),
      ]
    )