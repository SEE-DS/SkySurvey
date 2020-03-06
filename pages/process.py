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
        
            ## The Data
               Originally published by the Sloan Digital Sky Survey, this dataset contains observations of objects in space. 
                 
               There are 10,000 observations in the dataset used in this exploration.
                 
               Most of the features are photometric information, mostly broken up or 'binned' into wavelengths of light or radiation.
            """
        )
    ],
    md=2
)
column2 = dbc.Col(
    [    
        dcc.Markdown(
            """
            ## The Target
                 
               Of the available features of these observations, one is a clear target for classification:
            an object is defined to be a star, a galaxy, or a quasar (also known as a "quasi-stellar object").
                 
               Rather than explore this as a multi-class classification problem, in modeling I deconstructed this feature into binary classification for each type of object.
                 
               I was initially interested in classifying quasars, as they are dynamic and less-understood phenomena, but found the difficulty in classifying/differentiating galaxies from both stars and quasars to be an interesting challenge as well.
                 
               This difficulty gave me a clearer picture of the nature of classification, especially in terms of multi-class classification in the case of imbalanced classes.
                 
               The pie chart shown here displays the proportion of each class, as well as displaying the naive majority baseline upon hovering over the chart sections. (A 'naive majority baseline' accuracy is a measure of how accurate we would be if we guessed that every object belonged only to the class in question.) 
                 
               The rarer class (quasars) is easiest to differentiate, while the most common (galaxies) is the most difficult.             
            """
        )
    ],
    md=6,
)

df = pd.read_csv('assets/Skyserver_12_30_2019 4_49_58 PM.csv')
df_alpha = df.copy()
df['galaxy']=df['class']=='GALAXY'
df['star'] = df['class']=='STAR'
df['quasar'] = df['class']=='QSO'

class_distribution = df_alpha['class'].value_counts(normalize=True).reset_index()
qnaive = [('{0:.2f}%'.format(df.galaxy.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.star.value_counts(normalize=True)[0]*100)),
          ('{0:.2f}%'.format(df.quasar.value_counts(normalize=True)[0]*100))]
class_distribution['naivebaseline'] = qnaive
class_distribution['string'] = pd.Series(['{0:.2f}%'.format(val*100) for val in class_distribution['class']], index=class_distribution.index)
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
pie = px.pie(data_frame=class_distribution, values='class', names='index',
             title='Sky Object Classification Distribution',
             hover_data=['naivebaseline'], 
             labels={'index':'object',
                     'naivebaseline':'naive class baseline',
                     'class':'normalized class frequency'},
             width=500
)
pie.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
#fig.update_traces(hoverinfo='value', textinfo='label+percent', textfont_size=20,
#                  marker=dict(colors=colors, line=dict(color='#000000', width=2,)))



column3 = dbc.Col(
    [
        dcc.Markdown("""
            ( [The Sloan Digital Sky Survey or SDSS is a major multi-spectral imaging and spectroscopic redshift survey using a dedicated 2.5-m wide-angle optical telescope at Apache Point Observatory in New Mexico, United States. -Wikipedia](https://en.wikipedia.org/wiki/Sloan_Digital_Sky_Survey) )
            """),
        
        dcc.Graph(figure=pie),
        
        dcc.Markdown(
            """
                        
            ## The Metric
            Accuracy is an appropriate metric in evaluating the performance of a model built to classify these objects, as a large part of the motivation for this modeling is to explore the information it can reveal about the definitions and discovery of such objects.

            """
        )
    ],
    md=4
)

layout = dbc.Row([column1, column2, column3])
