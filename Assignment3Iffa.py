from dash import Dash, dcc, html, Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
]

cases_data = "https://raw.githubusercontent.com/iffaxoo/MCM7003/data/cases.csv"
patient_data = "https://raw.githubusercontent.com/iffaxoo/MCM7003/data/patient.csv"

dfCases = pd.read_csv(cases_data, encoding="latin")
dfCases.dropna(inplace=True)

dfPatient = pd.read_csv(patient_data, encoding="latin")
patient_data_clean = dfPatient.loc[:, ["gender", "age", "current_state"]].dropna()

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Iffa Assignment 3"


def create_covid_cases_figure():
    fig = px.line(
        dfCases,
        x=dfCases.index,
        y=["new_released", "new_deceased", "acc_released", "acc_deceased"],
        labels={"value": "Number of Cases", "variable": "Case Type"},
        title="COVID-19 Cases in Indonesia",
    )
    return fig


def create_age_distribution_figure():
    fig = px.histogram(
        patient_data_clean,
        x="age",
        nbins=20,
        title="Distribution of Covid-19 Patient in Indonesia by Age",
    )
    return fig


def create_gender_pie_chart_figure():
    gender_counts = patient_data_clean["gender"].value_counts()

    fig = px.pie(
        values=gender_counts.values,
        names=gender_counts.index,
        title="Percentage of Covid-19 Patient in Indonesia by Gender",
        labels={"gender": "Gender"},
    )

    fig.update_traces(textinfo="percent+label")
    fig.update_layout(showlegend=True)

    return fig


app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.H1(
                    "Data Visualization Assignment 3 Iffa",
                    className="display-4 mt-3 mb-4 text-center text-white",
                ),
                html.H2(
                    "Dashboard showing graphs", className="mb-4 text-center text-white"
                ),
            ],
            className="container bg",
            style={"padding": "2rem"},
        ),
        html.Div(
            [
                dcc.Graph(
                    id="covid_cases_fig",
                    figure=create_covid_cases_figure(),
                    className="mb-4",
                ),
                dcc.Graph(
                    id="age_dist_fig",
                    figure=create_age_distribution_figure(),
                    className="mb-4",
                ),
                dcc.Graph(
                    id="gender_pie_chart_fig",
                    figure=create_gender_pie_chart_figure(),
                    className="mb-4",
                ),
            ],
            className="container bg",
            style={"padding": "2rem"},
        ),
    ],
    style={"background-color": "#152238"},
)


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
