from flet import *
from utils.extras import Colors

class Bar(UserControl):
  def __init__(self,h,t):
    super().__init__()
    self.h = h
    self.t = t
    


  def build(self):
    return Column(
      alignment='spaceBetween',
      horizontal_alignment='center',
      controls=[
        Container(
          padding=padding.only(top=self.h),
          bgcolor='#1A000000',
          expand=True,
          width=45,
          content=Container(
            expand=True,
            width=45,
            bgcolor='black'
          )
        ),
        
        Container(height=13),
        Text(self.t,size=20,color='#888888')
      ]
    )