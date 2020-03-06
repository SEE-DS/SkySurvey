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
            
            In my estimation, going through the process to differentiate these objects from one another with the photometric data available is a great way to reverse-engineer the procedures undertaken that resulted in the discovery, defining, and study of quasi-stellar objects. 
            
            When combined with an appreciation that our ability to capture higher redshift has grown over time, it paints a picture of the gradual uncovering of phenomena that are still not widely understood and appreciated. 
            """),
         html.Img(src='assets/galaxy ugriz v redshift.png', className='img-fluid'),       
    ],
    md=3
)
column2 = dbc.Col(
    [
        
        html.Img(src='assets/galaxy confusion matrix.png', className='img-fluid'),
        dcc.Markdown(
            """
            Based on all the feature-importance evidence between classes and individual predictions, **redshift** is far and away the most predictive feature of any given observation. 
            
            The Shapley value force plot for the prediction that the object observed below is a galaxy shows that __other factors may come into play as well__, demonstrating that estimating the significance of a feature in terms of an entire dataset (the importance of redshift) doesn't necessarily reflect the weight of it's impact on individual predictions. 
            """
        ),
        html.Img(src='assets/galaxy true.png', className='img-fluid'),
        html.Img(src='assets/star true.png', className='img-fluid'),
        html.Img(src='assets/quasar true.png', className='img-fluid'),
        dcc.Markdown("""
            ## Further Exploration!
            With such a clear distinction between these classes, I would be interested to explore the task of differentiating between the tougher cases, and could imagine subsetting the data to classify only those cases that are more ambiguous, in order to bring more to light the other factors that enter into the differentiation between stars, galaxies, and quasi-stellar objects (who often are surrounded by galaxies that are hard to make out against the glare of QSOs)
            """),
        html.Img(src='assets/the higher the redshift, the less likely an object is a galaxy.png', className='img-fluid'),  
        dcc.Markdown("""(As seen above, the higher the redshift, the less likely an object is a galaxy)
        
        """),        
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
            
              By applying an ensemble method ([extreme gradient boosting](https://en.wikipedia.org/wiki/XGBoost)) and harnessing the power of it's distribution and scope, the accuracy achievable was enhanced to 99.22% agaist a validation subset and 99.26% with the model refit and scored against the test set.
            """
        ),
        html.Img(src='assets/galaxy xgb eli5 permutation importance.png'),        
    ],
)

layout = dbc.Row([column1, column2, column3])
