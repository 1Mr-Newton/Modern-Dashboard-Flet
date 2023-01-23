from flet import *
from utils.extras import Colors
from utils.bar import Bar

class Chart(UserControl):
  def __init__(self):
    super().__init__()
    self.container = Bar


  def build(self):
    return Column(
      controls=[
        Container(
          height=200,
          # width=200,
          bgcolor='white',
          content=Row(
            controls=[
              Column(
                  alignment='spaceBetween',
                  controls=[
                  Container(
                    expand=True,
                    width=50,
                    content=Column(
                      alignment='spaceBetween',
                      controls=[
                        Text('100K',color='black'),
                        Text('50K',color='black'),
                        Text('10K',color='black'),
                        Text('0',color='black'),
                      ]
                    ),
                  ),
                  
                  Container(
                    height=30,
                    width=50,
                  ),
                ]
              ),

              Container(
                width=600,
                content=Stack(
                  controls=[
                    Container(
                      opacity=0.1,
                      padding=padding.only(bottom=35),
                      # bgcolor='red',
                      content=Column(
                        alignment='spaceBetween',
                        controls=[
                          Divider(color='black'),
                          Divider(color='black'),
                          Divider(color='black'),
                          Divider(color='black'),
                          Divider(color='black'),
                        ]
                      )
                    ),

                    Container(
                      padding=padding.only(top=8),
                      content=Row(
                        spacing = 40,
                        scroll='auto',
                        controls=[
                        self.container(100,'Jan'),
                        self.container(30,'Feb'),
                        self.container(130,'Mar'),
                        self.container(80,'Apr'),
                        self.container(74,'May'),
                        self.container(18,'Jun'),
                        self.container(90,'Jul'),
                        self.container(143,'Aug'),
                        self.container(87,'Sep'),
                        self.container(69,'Oct'),
                        self.container(10,'Nov'),
                        self.container(148,'Dec'),
                      
                      ]
                    )
                    )

                  ]
                )
              ),
            
              
            
            
            
            ]
          )
      ),]
    )