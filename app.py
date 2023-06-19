#include dash , dash-core-components , dash-html-components , dash-bootstrap-components

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from dash.dependencies import Output,Input

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY])
poverty_data = pd.read_csv('Data/PovStatsData.csv')


app.layout = html.Div([
    html.H1('Poverty and Equity Database',
            style={'color': 'blue',
                   'fontSize': '40px'}),
    html.H2('The World Bank'),
    dcc.Dropdown(id='country',options= [{'label':country,'value':country }
                                        for country in poverty_data['Country Name'].unique()]),
    html.Br(),
    html.Div(id='result'),
    html.Br(),
    dbc.Tabs([
       dbc.Tab([
           html.Ul([
               html.Br(),
               html.Li('Number of Economies: 170'),
               html.Li('Temporal Coverage: 1974 - 2019'),
               html.Li('Update Frequency: Quarterly'),
               html.Li('Last Updated: March 18, 2020'),
               html.Li([
                   'Source: ',
                   html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                          href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
               ])
           ])

       ], label='Key Facts'),
        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                         html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                                href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                         ])
            ])
        ], label='Project Info')
    ]),
])

@app.callback(Output('result','children'),
              Input('country','value'))
def display_country_report(country):
    if country is None:
        return ''

    filtered_df = poverty_data[(poverty_data['Country Name']==country) &
                               (poverty_data['Indicator Name']=='Population, total')]
    population = filtered_df.loc[:, '2010'].values[0]

    return [html.H3(country),
            f'The population of {country} in 2010 was {population:,.0f}.']


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8060)

