# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from joblib import load

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
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
        dcc.Link(dbc.Button('What is it?', color='primary'), href='/predictions')
    ],
    md=4,
)

pipeline_isgalaxyrf = load('assets/isgalaxyrf.joblib')

import pandas as pd

df = pd.read_csv('https://github.com/arewelearningyet/dashtemplate/blob/master/assets/Skyserver_12_30_2019%204_49_58%20PM.csv?raw=true')
df_alpha = df.copy() # creating backup copy
df = df.drop(columns='specobjid')
df['galaxy']=df['class']=='GALAXY'
df['star'] = df['class']=='STAR'
df['quasar'] = df['class']=='QSO'
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

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])