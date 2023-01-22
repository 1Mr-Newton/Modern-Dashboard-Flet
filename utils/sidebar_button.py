from flet import *
import back
class SidebarButton(UserControl):
  def __init__(self,image):
    super().__init__()
    self.icon = image

  def build(self):
    return Column(
      controls=[
        Container(
          border=border.only(right=border.BorderSide(width=2,color='black')),
          padding=padding.only(left=25,),
          alignment=alignment.center,
          content=Row(
            alignment='spaceBetween',
            controls=[
              Image(
                src=f'assets/icons/{self.icon}.png',
                scale=0.7
              ),
            ]
          )
        )
       
      ]
    )