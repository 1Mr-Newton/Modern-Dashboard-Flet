from flet import *
from utils.sidebar_button import SidebarButton

class LeftSidebar(UserControl):
  def __init__(self):
    super().__init__()
    self.sidebar_btn = SidebarButton

  def build(self):
    return Column(
      controls=[
        Container(
          margin=margin.only(bottom=40),
          height=50,
          content=Row(
            spacing=5,
            alignment='center',
            vertical_alignment='center',
            controls=[
              Container(
                height=11,
                width=11,
                bgcolor='red',
                border_radius=10
              ),
              Container(
                height=11,
                width=11,
                bgcolor='orange',
                border_radius=10
              ),
              Container(
                height=11,
                width=11,
                bgcolor='green',
                border_radius=10
              ),
            ]
          )  
        ),
        self.sidebar_btn('home1'),
       
      ]
    )