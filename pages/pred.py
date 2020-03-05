# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from joblib import load

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
df = pd.read_csv('assets/Skyserver_12_30_2019 4_49_58 PM.csv')

ra = sorted(df['ra'].unique())
dec = sorted(df['dec'].unique())
redshift = sorted(df['redshift'].unique())

style = {'padding': '1.5em'}

column1 = dbc.Col([
        dcc.Markdown(
            """
            ## **Make a Prediction**
            """
        ),
        html.Div([
			dcc.Markdown("###### Select ra"),
			dcc.Slider(
				id='ra-input', 
				value=''
			)
		]),
		html.Div([
			dcc.Markdown("###### Select dec"),
			dcc.Dropdown(
				id='dec-input', 
				value=''
			)
		]),
		html.Div([
			dcc.Markdown("###### Select redshift"),
			dcc.Dropdown(
				id='redshift-input', 
				value=''
			)
		])
	],
	md=3
)
column2 = dbc.Col([
		#dcc.Markdown("##### Set Approximate Year"),
		#dcc.Slider(
		#	id='year-slide',
		#	min=1940,
		#	max=2020,
		#	step=2,
		#	value=1987,
		#	marks={n: f'{n:.0f}'for n in range(1940,2040,10)}
		#),
		html.H4(id='prediction-content', style={'fontWeight':'bold'}),
		html.Div(
			dcc.Graph(id='shap-plot')
		)
		
	], 
	md=6
)
@app.callback(
	[Output('prediction-content', 'children'),
	 Output('shap-plot', 'figure')],
	[Input('ra-input', 'value'),
	 Input('dec-input', 'value'),
	 Input('redshift-input', 'value')])

def predict_and_plot(ra, dec, redshift):
	# Create prediction
	pred_df = pd.DataFrame(
		columns=['ra', 'dec', 'redshift'],
		data=[[ra, dec, redshift]]
	)
	
	pipeline = load('model/xgbqso.joblib')
	y_pred_log = pipeline.predict(pred_df)
	y_pred = np.expm1(y_pred_log)[0]
	
	pred_out = f"Current Value: ${y_pred:,.2f}"
	
	# Derive shap values from user input
	model = pipeline.named_steps['xgbclassifier']
	explainer = load('model/explainer.joblib') #this part
	shap_vals = explainer.shap_values(pred_df_encoded)
	input_names = [i for i in pred_df.iloc[0]]
	
	# Create dataframe for shap plot
	shap_df = pd.DataFrame({'feature': pred_df.columns.to_list(),
							'shap-val': shap_vals[0],
							'val-name': input_names})
	# Create list of two different colors depending on shap-val
	colors = [
	'#0063D1' if value >= 0.0 else '#E43137' for value in shap_df['shap-val']
	]
	
	#condensed_names = ['Model', 'MPN', 'Body Color', 'Brand', 
					   #'UPC Avail.', 'Material', 'Body Type', 
					   #'Year', 'Size', 'Country', 'No. Strings', 
					   #'Orientation', 'Prod. Line', 'Condition']

	
	shap_plot = {
		'data': [
			{'x': shap_df['shap-val'], 'y': condensed_names,
			'type': 'bar', 'orientation':'h', 'hovertext': shap_df['val-name'],
			'marker': {'color': colors}, 'opacity': 0.8}],
		'layout': {
			'title': 'Atrribute Impact on Prediction',
			'transition': {'duration': 250}}
	}
	
	
	
	
	
	
	return pred_out, shap_plot

layout = dbc.Row([column1, column2])