from flet import *
import back
from utils.selectable_container import SelectableContainer
from utils.navigation_bar import CustomNavigationBar
from utils.base import BasePage as BP
class HomeScreen(UserControl):
  def __init__(self, pg):
    super().__init__()
    self.pg = pg

  def change_page(self):
    self.page.go('')  
  def switch_screen(self,route):
    self.page.go(route)  
    back.back_ = '/events'
  def build(self):
    return Column(
      controls=[
        BP(),
      ]
    )