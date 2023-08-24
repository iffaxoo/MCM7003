from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

cases_data = "https://raw.githubusercontent.com/iffaxoo/MCM7003/data/cases.csv"
patient_data = "https://raw.githubusercontent.com/iffaxoo/MCM7003/data/patient.csv"

dfCases = pd.read_csv(cases_data, encoding="latin")
dfCases.dropna(inplace=True)

dfPatient = pd.read_csv(patient_data, encoding="latin")
dfPatient.dropna(inplace=True)

app = Dash(__name__)

app.layout = html.Div ([
    html.H1("Data Visualization Assignment 3"),
    html.H2("Dashboard showing graphs"),
    dcc.Graph(id='covid-cases-graph'),
    dcc.Graph(id='age-distribution-graph'),
    dcc.Graph(id='gender-pie-chart-graph')

])

def create_covid_cases_figure():
    fig = px.line(dfCases, x=dfCases.index, y=['new_released', 'new_deceased', 'acc_released', 'acc_deceased'],
                  labels={'value': 'Number of Cases', 'variable': 'Case Type'},
                  title="COVID-19 Cases in Indonesia")
    return fig

def create_age_distribution_figure():
    fig = px.histogram(dfPatient, x='age', nbins=20, title="Distribution of Covid-19 Patient in Indonesia by Age")
    return fig

def create_gender_pie_chart_figure():
    gender_counts = dfPatient['gender'].value_counts()
    fig = px.pie(gender_counts, labels=gender_counts.index, values=gender_counts.values,
                 title="Percentage of Covid-19 Patient in Indonesia by Gender")
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
