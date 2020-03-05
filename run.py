# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, process, insights # predictions, insights, process, pagename

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Look! Up in the sky! It\'s a bird! It\'s a plane! It\'s... Wait - what is it?',
    brand_href='/', 
    children=[
        #dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
        #dbc.NavItem(dcc.Link('Page Name', href='/pagename', className='nav-link'))
    ],
    sticky='top',
    color='dark', 
    light=False, # text
    dark=True
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('C Stump', className='mr-4 name'), 
                    html.A(html.I(className='fas fa-envelope-square mr-3'), href='mailto:lambdadatasciencelearning@gmail.com'), 
                    html.A(html.I(className='fab fa-github-square mr-3'), href='https://github.com/arewelearningyet/u2b'), 
                    #html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/<you>/'), 
                    html.A(html.I(className='fab fa-twitter-square mr-3'), href='https://twitter.com/CSLSDS'),
                    html.A(html.I(className='fab fa-superpowers mr-3'), href='https://www.sdss.org/'),
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    #elif pathname == '/predictions':
    #    return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    #elif pathname == '/pagename':
    #    return pagename.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)