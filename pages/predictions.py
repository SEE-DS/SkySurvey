# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
from joblib import load
import shap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import xgboost

# Imports from this application
from app import app

pipeline = load('model/xgbqso.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('#### ra'), 
        dcc.Slider(
            id='ra', 
            min=0, 
            max=360, 
            step=1, 
            value=180, 
            marks={n: str(n) for n in range(0,360,10)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### dec'), 
        dcc.Slider(
            id='dec', 
            min=-20, 
            max=85, 
            step=1, 
            value=50, 
            marks={n: str(n) for n in range(-20,50,5)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### redshift'), 
        dcc.Slider(
            id='redshift', 
            min=0, 
            max=7, 
            step=0.1, 
            value=.1, 
            marks={n: str(n) for n in range(0,7,1)}, 
            className='mb-5', 
        )
    ],
    md=6,
)

column3 = dbc.Col(
    [
        html.H2('Predicted Loan Risk', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        html.Button('Explain Prediction', id='explain-btn'),
        html.Div([html.Img(id='shap-img', height=200, width=1000)])
    ]
)

layout = html.Div(
    [
        dbc.Row(column1),
        dbc.Row(column3)
    ]
)

def fig_to_uri(in_fig, close_all=True, **save_args):
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('ra', 'value'), 
     Input('dec', 'value'),
     Input('redshift', 'value')]
)
def predict(ra, dec, redshift):   
    # Convert input to dataframe
    df = pd.DataFrame(
        data=[[ra, dec, redshift]],
        columns=['ra', 'dec', 'redshift']
    )

    # Make predictions (includes predicted probability)
    pred_proba = pipeline.predict_proba(df)[0, 1]
    pred_proba *= 100

    # Show predictiion & probability
    return (f'The model predicts {pred_proba:.0f}% probability .')

@app.callback(
    Output('shap-img', 'src'),
    [Input('explain-btn','n_clicks')],
    [State('ra', 'value'), 
     State('dec', 'value'),
     State('redshift', 'value')]
)
def explain_png(n_clicks, ra, dec, redshift):
    
    # Convert input to dataframe
    df = pd.DataFrame(
        data=[[ra, dec, redshift]],
        columns=['ra', 'dec', 'redshift']
    )

    # Get steps from pipeline and transform
    model = pipeline.named_steps['xgbclassifier']

    
    # Get shapley additive explanations
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    # Plot shapley and save matplotlib plot to base64 encoded buffer for rendering
    fig = shap.force_plot(
        base_value=explainer.expected_value, 
        shap_values=shap_values, 
        features=df, 
        show=False,
        matplotlib=True)
    
    out_url = fig_to_uri(fig)

    # Return image
    return out_url