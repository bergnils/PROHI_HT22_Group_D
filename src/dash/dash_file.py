
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import dash_bootstrap_components as dbc
import numpy as np

import pandas as pd
import pickle

app = Dash(__name__)

filename = './RF_model.pkl'
infile = open(filename,'rb')
model = pickle.load(infile)
infile.close()

app.layout = html.Div([
            dcc.Dropdown(
                options=[
                    {'label': '< 120 mg/dl', 'value': 0},
                    {'label': '> 120 mg/dl', 'value': 1}],
                placeholder='Fasting blood sugar',
                id='fasting_bs'
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'No', 'value': 0},
                    {'label': 'Yes', 'value': 1}],
                placeholder='Exercise induced angina?',
                id='exercise_angina'
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'Typical angina', 'value': 'typical_angina'},
                    {'label': 'Atypical angina', 'value': 'atypical_angina'},
                    {'label': 'Non anginal pain', 'value': 'non_angingal_pain'},
                    {'label': 'Asymptomatic', 'value': 'asymptomatic'}],
                placeholder='Chest pain type',
                id='chest_pain'
            ),
            dcc.Dropdown(
                options=[
                    {'label': 'Normal', 'value': 0},
                    {'label': 'Abnormal', 'value': 1}],
                placeholder='Resting electrocardiographic results',
                id='restingecgstt_abnormal'
            ),
    dbc.Row([dbc.Button('Submit', id='submit-val', n_clicks=0, color="primary")]),
    html.Br(),
    dbc.Row([html.Div(id='prediction output')])])

@app.callback(
    Output('prediction output', 'children'),
    Input('submit-val', 'n_clicks'),
    State('fasting_bs', 'value'),
    State('exercise_angina', 'value'),
    State('chest_pain', 'value'),
    State('restingecgstt_abnormal', 'value')
)

def update_output(n_clicks, bs_value, angina_value, pain_value, abnormal_value):
    print(bs_value)
    if pain_value=='typical_angina':
        x = [[float(bs_value), float(angina_value), 1,0,0, float(abnormal_value)]]
    elif pain_value=='atypical_angina':
        x = [[float(bs_value), float(angina_value), 0, 1, 0, float(abnormal_value)]]
    elif pain_value=='non_anginal_pain':
        x = [[float(bs_value), float(angina_value), 0, 0, 1, float(abnormal_value)]]
    else:
        x = [[float(bs_value), float(angina_value), 0, 0, 0, float(abnormal_value)]]
    prediction = model.predict(x)
    if prediction == 0:
        output = 'No risk for heart disease'
    elif prediction == 1:
        output = 'There is a risk for heart disease'
    return output



if __name__ == '__main__':
    app.run_server()



