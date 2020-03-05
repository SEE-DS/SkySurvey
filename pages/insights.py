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
        )
df=pd.read_csv('https://github.com/arewelearningyet/dashtemplate/blob/master/assets/Skyserver_12_30_2019 4_49_58 PM.csv?raw=true')
fig = px.scatter_3d(df, 
                    x='ra', 
                    y='dec', 
                    z='redshift', 
                    color='class', 
                    hover_data=['class'])
fig.update_traces(
#mode = 'markers',
                    marker = dict(
                        symbol = 'diamond',
        ))
#fig.update_layout(scene_zaxis_type="log")

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
column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])