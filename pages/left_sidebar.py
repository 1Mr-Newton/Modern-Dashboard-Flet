from flet import *
import back
from utils.sidebar_button import SidebarButton
class LeftSidebar(UserControl):
  def __init__(self):
    super().__init__()
    # self.pg = pg
    self.sidebar_btn = SidebarButton

  def change_page(self):
    self.page.go('')  
  def switch_screen(self,route):
    self.page.go(route)  
    back.back_ = '/events'
  def build(self):
    return Column(
      controls=[
        Container(height=50),
        self.sidebar_btn('home1'),
        # self.sidebar_btn,
        # self.sidebar_btn,
       
      ]
    )