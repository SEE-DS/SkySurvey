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
            #### Sloan Digital Sky Survey
            
            ## So... what are we looking at?

            A starry night is more than it seems.

            How can we identify one tiny dot within the vastness of space?
            
            """
        ),
        dcc.Link(dbc.Button('What is it?', color='secondary'), href='/predictions')
    ],
    md=3
)

df = pd.read_csv('assets/Skyserver_12_30_2019 4_49_58 PM.csv')
df['galaxy']=df['class']=='GALAXY'
df['star'] = df['class']=='STAR'
df['quasar'] = df['class']=='QSO'
"""
df=df.drop(columns='class')

class_distribution = df_alpha['class'].value_counts(normalize=True).reset_index()
qnaive = [('{0:.2f}%'.format(df.galaxy.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.star.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.quasar.value_counts(normalize=True)[0]*100))]
class_distribution['naivebaseline'] = qnaive
class_distribution['class'] = pd.Series(['{0:.2f}%'.format(val*100) for val in class_distribution['class']], index=class_distribution.index)
print(class_distribution)
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
fig = px.pie(class_distribution, values='class', names='index',
             title='Sky Object Classification Distribution',
             hover_data=['naivebaseline'], labels={'index':'object',
                                                   'naivebaseline':'naive class baseline'})
fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2,)))
 """

fig = (px.scatter_3d(df, 
                    x='ra', 
                    y='dec', 
                    z='redshift', 
                    color='redshift',
                    hover_data=['class'],
                    symbol='class',
                    symbol_sequence=['square', 'circle', 'x'],
                    width=825,
                    height=900))
fig.update_traces(marker=dict(size=5,
                              line=dict(width=0)),
                  selector=dict(mode='markers'),
                  showlegend=True)

img_width=1600
img_height=1200

fig.update_xaxes(showgrid=False,
        visible=False,
        range=[0, img_height],
        scaleanchor='x'
        )
fig.update_yaxes(showgrid=False,
        visible=False,
        range=[0, img_height],
        scaleanchor='x'
        )
fig.update_layout(title_text="",
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
                      bgcolor='rgba(0,0,0,0)',
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
fig.add_layout_image(
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
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
