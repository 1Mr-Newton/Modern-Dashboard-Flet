from flet import *
from utils.extras import AppSize, Colors
from pages.left_sidebar import LeftSidebar
from pages.mainbody import MainBody

class BasePage(UserControl):
  def __init__(self, content=None):
    super().__init__()
    self.content = content
    self.sizes = AppSize()
    self.colors = Colors()
    self.mainbody = MainBody()
  def build(self):
    return Column(
      controls=[
        Container(
          height=self.sizes.main_height,
          width=self.sizes.main_width,
          bgcolor=self.colors.main_bg,
          content=Row(
            spacing=0,
            alignment='spaceBetween',
            controls=[
              Container(
                width=self.sizes.sidebar_width,
                bgcolor=self.colors.grey300,
                content=LeftSidebar()
              ),
              Container(
                width=self.sizes.main_width-self.sizes.sidebar_width-self.sizes.right_sidebar_width,
                bgcolor=self.colors.main_bg,
                content=self.mainbody
              ),
              Container(
                width=300,
                bgcolor=self.colors.grey300,
                content=LeftSidebar()
              ),
            ]
          )
          
        )
      ]
    )