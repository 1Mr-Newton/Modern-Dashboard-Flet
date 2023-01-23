from flet import *
from utils.extras import Colors
from utils.dashboard_card import DashboardCard
from utils.chart import Chart

class Dashboard(UserControl):
  def __init__(self):
    super().__init__()
    self.dashboard_card = DashboardCard
    self.custom_colors = Colors()


  def build(self):
    

    return Column(
      # scroll='auto',
      controls=[
        Container(
          padding=padding.only(top=1,left=30,bottom=2,right=30),
          content=Column(
            scroll='auto',
            controls=[
              Container(
                height=300,
                content=Column(
                  controls=[
                    Container(
                      # padding=padding.only(bo)
                      margin=margin.only(bottom=20),
                      content=Row(
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
                    
                    ),
                    
                    Container(
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          self.dashboard_card(icons.CARD_GIFTCARD,'Transfer via card number','1200'),
                          self.dashboard_card(icons.SHARE_OUTLINED,'Transfer to outside country','150'),
                          self.dashboard_card(icons.HOME_OUTLINED,'Transfer same Bank','1500'),
                          self.dashboard_card(icons.FOOD_BANK,'Transfer to other Bank','1358'),
                          
                        ]
                      ),
                    )
                  ]
                )
              ),

              Container(
                height=300,
                content=Column(
                  controls=[
                    Container(
                      content=Row(
                        alignment='spaceBetween',
                        controls=[
                          Column(
                            spacing = 0,
                            controls=[
                              Text(
                                value='Balance',
                                color=self.custom_colors.grey400,
                                size=12,
                                font_family='SF Pro Regular'
                              ),
                              Text(
                                value='$1500',
                                color=self.custom_colors.grey800,
                                size=20,
                                font_family='SF Pro Heavy'
                              ),
                            ]
                          ),
                          Container(
                            content=Text(
                                value='First 30 Days',
                                color=self.custom_colors.grey400,
                                size=12,
                                font_family='SF Pro Regular'
                              ),
                          ),
                        ]
                      ),
                    
                    ),
                    
                    Container(
                      
                      Chart()
                    ),
                  ]
                )
              ),

              Container(
                height=300,
                content=Column(
                  controls=[
                    Container(
                      # padding=padding.only(bo)
                      margin=margin.only(bottom=20),
                      content=Row(
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
                          value='Transaction history of last 6 months',
                          color=self.custom_colors.grey400,
                          size=12,
                          font_family='SF Pro Regular'
                        ),
                      ]
                    ),
                    
                  ]
                ),
                    
                    ),
                    
                    Container(
                      height=500,
                      content=Column(
                        spacing=20,
                        # height=600,
                        alignment='spaceBetween',
                        scroll='auto',
                        controls=[
                          Container(
                            padding=padding.only(left=15,right=15,top=5,bottom=5),
                            border_radius=20,
                            width=700,
                            height=65,
                            content=Row(
                              alignment='spaceBetween',
                              controls=[
                                CircleAvatar(radius=15),
                                Text('Car Insurance',color='black'),
                                Text('10:42 AM',color='black'),
                                Text('$350.00',color='black'),
                                Text('Completed',color='black'),
                              ]
                            )
                          ),
                          
                          
                          Container(
                            padding=padding.only(left=15,right=15,top=5,bottom=5),
                            border_radius=20,
                            width=700,
                            height=65,
                            bgcolor='white',
                            content=Row(
                              alignment='spaceBetween',
                              controls=[
                                CircleAvatar(radius=15),
                                Text('Car Insurance',color='black'),
                                Text('10:42 AM',color='black'),
                                Text('$350.00',color='black'),
                                Text('Completed',color='black'),
                              ]
                            )
                          ),

                          
                          
                        ]
                      ),
                    )
                  ]
                )
              ),



            ]
          )
        )
      ]
    )