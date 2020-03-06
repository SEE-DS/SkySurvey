# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 3/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        html.Img(src='assets/sdsslogowhite.png', className='img-fluid'),
        dcc.Markdown(
            """
            ## Sloan Digital Sky Survey 
            
            #### So... what are we looking at?

            A starry night is more than it seems.

            How can we identify one tiny dot within the vastness of space?
            
            ### The Graph
            
            Shown here are radiant space objects, representing three types.
            
            __The most telling part of this graph is how difficult it is to find and differentiate galaxies from stars and quasars.__
            
            The __color and the z-axis__ represent each objects' [**__redshift__**](https://en.wikipedia.org/wiki/Redshift#Observations_in_astronomy).
            
            """
        ),
        #dcc.Link(dbc.Button('What is it?', color='secondary'), href='/predictions')
           
        dcc.Markdown(
            """
            The __x and y planes__ represent astronomical coordinates [**right ascension**](https://en.wikipedia.org/wiki/Right_ascension) and [**declination**](https://en.wikipedia.org/wiki/Declination), respectively. 
            
            
            [(see animation for a visual explanation)](https://en.wikipedia.org/wiki/Equatorial_coordinate_system)
            """
        ),
        html.Img(src='assets/Ra_and_dec_demo_animation_small.gif', className='img-fluid')       
    ],
    md=5
)

df = pd.read_csv('assets/Skyserver_12_30_2019 4_49_58 PM.csv')

scatter = (px.scatter_3d(df, 
                    x='ra', 
                    y='dec', 
                    z='redshift', 
                    color='redshift',
                    hover_data=['class'],
                    symbol='class',
                    symbol_sequence=['square', 'circle', 'x'],
                    width=800,
                    height=900))

scatter.update_traces(marker=dict(size=5,
                              line=dict(width=0)),
                  selector=dict(mode='markers'),
                  showlegend=True)

img_width=1600
img_height=1200

scatter.update_xaxes(showgrid=False,
        visible=False,
        range=[0, img_height],
        scaleanchor='x'
        )
scatter.update_yaxes(showgrid=False,
        visible=False,
        range=[0, img_height],
        scaleanchor='x'
        )
scatter.update_layout(title_text="",
                  title_font_size=30,
                  legend=dict(
                      bgcolor='yellow',
                      bordercolor='black',
                      itemsizing='constant',
                      itemclick='toggleothers',
                      borderwidth=3,
                      x=.4, 
                      y=0,
                      font=dict(
                          color='black',
                          size=14
                          )
                      ),
                  coloraxis=dict(
                      colorbar=dict(
                          tickcolor='yellow',
                          tickfont=dict(
                              color='yellow'),
                          title=dict(
                              font=dict(
                                  color='yellow')
                              )
                          )
                      ),
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  scene=dict(
                      dragmode='turntable',
                      bgcolor='rgba(0,0,0,0)',
                      camera=dict(
                        center=dict(
                            z=-.20,
                            y=.05,
                            x=.5
                        ),
                        eye=dict(
                            z=-0.5
                        ),
                      ),
                      xaxis=dict(
                          visible=False,
                          showbackground=False,
                          color='yellow'),
                      yaxis=dict(
                          visible=False,
                          showbackground=False,
                          color='yellow'),
                      zaxis=dict(
                          visible=False,
                          showbackground=False,
                          linecolor='yellow',
                          tickcolor='yellow',
                          title=dict(
                              font=dict(
                                  color='yellow')
                              )
                          )
                      )
                  )
scatter.add_layout_image(
        dict(
            source='https://raw.githubusercontent.com/arewelearningyet/dashtemplate/master/assets/fieldvoorwerp-big.jpg',
            x=0,
            sizex=img_width,
            y=img_height,
            sizey=img_height,
            xref='x',
            yref='y',
            opacity=1.0,
            layer='below',
            sizing='stretch',
            )
        )

# fig.update_traces(
# #mode = 'markers',
#                     marker = dict(
#                         symbol = 'diamond',
#         ))
# #fig.update_layout(scene_zaxis_type="log")

column2 = dbc.Col(
    [
        dcc.Graph(figure=scatter),
        dcc.Markdown("""(you can toggle the legend items to view one class at a time, but the color representation will shift to reflect the spread of redshift within that class alone)""")
    ],
    md=7
)

layout = dbc.Row([column1, column2])
