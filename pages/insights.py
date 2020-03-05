# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Ey

            """
        ),
        html.Hr(),
        dcc.Markdown(
            """
            ## 
            ### Q?
            A: 
            """
        )
    ],
    md=12,
)

df = pd.read_csv('https://github.com/arewelearningyet/dashtemplate/blob/master/assets/Skyserver_12_30_2019%204_49_58%20PM.csv?raw=true')
df_alpha = df
df['galaxy'] = df['class']=='GALAXY'
df['star'] = df['class']=='STAR'
df['quasar'] = df['class']=='QSO'
df=df.drop(columns='class')

class_distribution = df_alpha['class'].value_counts(normalize=True).reset_index()
naive = [('{0:.2f}%'.format(df.galaxy.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.star.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.quasar.value_counts(normalize=True)[0]*100))]
class_distribution['naivebaseline'] = naive
class_distribution['class'] = pd.Series(['{0:.2f}%'.format(val*100) for val in class_distribution['class']], index=class_distribution.index)
colors = ['gold', 'mediumturquoise', 'darkorange']
fig = px.pie(class_distribution, values='class', names='index',
             title='Sky Object Classification Distribution',
             hover_data=['naivebaseline'], labels={'index':'object',
                                                   'naivebaseline':'naive class baseline'})
#fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=20,
#                  marker=dict(colors=colors, line=dict(color='#000000', width=2,)))



column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])