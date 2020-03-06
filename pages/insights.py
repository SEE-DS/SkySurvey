# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## But what about the modeling???
            
            The efforts to effectively classify these objects may not be groundbreaking science, but they can be valuable and informative. 
            In my estimation, going through the process to differentiate these objects from one another with the available photometric data available is a great way to reverse-engineer the procedures undertaken that resulted in the discovery, defining, and study of quasi-stellar objects. 
            When combined with an appreciation that our ability to capture higher redshift has grown over time, it paints a picture of the gradual uncovering of phenomena that are still not widely understood and appreciated. 
            """),
    ],
    md=3
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            Based on all the feature-importance evidence between classes and individual predictions, redshift is far and away the most predictive feature of any given observation. 
            
            The Shapley value force plot for the prediction that the object observed below is a galaxy shows that other factors may come into play as well, demonstrating that estimating the significance of a feature in terms of an entire dataset (the importance of redshift) doesn't necessarily reflect the weight of it's impact on individual predictions. 
            """
        ),
        html.Img(src='assets/galaxy true.png', className='img-fluid'),
        html.Img(src='assets/star true.png', className='img-fluid'),
        html.Img(src='assets/quasar true.png', className='img-fluid'),
    ],
    md=6
)
column3 = dbc.Col(
    
    [
        dcc.Markdown(
            """ 
            ### No seriously, your grade depends on modeling and evaluation.
            
              Well, if you must know...
                
              A baseline score for predicting quasars was 89.42%, and even a simple linear model achieved 99% accuracy.
            
              The baseline score for predicting galaxies however, is 48.35%... a much more interesting problem.
            
              Using a simple logistic regression, classification accuracy for predicting galaxies was 90.76% accurate against the validation subset. 
            
              By applying an ensemble method and harnessing the power of it's distribution and scope, the accuracy achievable was enhanced to 99.02% agaist a validation subset and 99.14% with the model refit and scored against the test set.
            """
        ),

    ],
)

layout = dbc.Row([column1, column2, column3])
