from flet import *
from utils.extras import AppSize, Colors
from pages.left_sidebar import LeftSidebar

class BasePage(UserControl):
  def __init__(self,pg, content=None):
    super().__init__()
    self.content = content
    self.pg = pg
    self.pg.on_resize = self.resize_handler
    self.sizes = AppSize()
    self.colors = Colors()
    self.body = Container(
          # expand=True,
          height=self.pg.window_height,#-30,
          bgcolor=self.colors.main_bg,
          content=Row(
            spacing=0,
            alignment='spaceBetween',
            controls=[
              
              
            ]
          )
          
        )
    # self.mainbody = MainBody()
    # self.left_side = LeftSidebar()


    # self.left_side_bar = Container(
    #   width=self.sizes.sidebar_width,
    #   bgcolor=self.colors.grey300,
    #   content=LeftSidebar()

    # )
    # self.right_side_bar = Container(
    #   width=self.sizes.sidebar_width,
    #   bgcolor=self.colors.grey300,
    #   content=LeftSidebar()

    # )
    # self.main_body = Container(
    #   width=self.sizes.sidebar_width,
    #   bgcolor=self.colors.grey300,
    #   content=LeftSidebar()

    # )


  def resize_handler(self,e):
    self.body.height = float(e.data.split(',')[1])
    self.body.update()
    

  def build(self):
    return Column(
      spacing=0,
      controls=[
        # Container(
        #   height=40,
        #   bgcolor='white',
        #   content=Row(
        #     spacing=0,
        #     controls=[
        #         Container(
        #           padding=10,
        #           width=100,
        #           height=40,
        #           content=Row(
        #             # alignment='spaceAround',
        #             controls=[
        #               Container(
        #                 on_click=lambda _: self.pg.window_close(),
        #                 bgcolor='orange',
        #                 height=15,
        #                 width=15,
        #                 border_radius=15
        #               ),
        #               Container(
        #                 # on_click=lambda _: self.pg.window_close(),
        #                 bgcolor='green',
        #                 height=15,
        #                 width=15,
        #                 border_radius=15
        #               ),
        #               Container(
        #                 # on_click=lambda _: self.pg.window_close(),
        #                 bgcolor='red',
        #                 height=15,
        #                 width=15,
        #                 border_radius=15
        #               ),
        #             ]
        #           )
        #         ),
        #         WindowDragArea(
                  
        #           Container(
        #               padding=10), 
        #             expand=True,
        #           ),
        #     ]
        # ),

        # ),
        
        self.body
      ]
    )