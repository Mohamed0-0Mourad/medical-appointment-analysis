from dash import Dash, dcc, html
from pandas import read_csv
import charts
from charts import avg_appoint_delay
from preproccessing import DF

def get_main_content():
    age_group_names = ["Child","Teen","Young Adult","Middle-Aged","Senior"]
    age_filter = dcc.Dropdown(age_group_names, value=[], id="age-group-filter",
                 className="text-dark p-2", clearable=True, multi=True)
    medical_cond_filter = dcc.Dropdown(["Hipertension", "Diabetes", "Alcoholism", "Handcap"], value=[], id="medical-cond-filter",
                              className="text-dark p-2", clearable=True, multi=True)
    area_filter = dcc.Dropdown(DF.Neighbourhood.unique(), value=[], id="area-filter-group",
                               className="text-dark p-2", clearable=True, multi=True)

    absence, absence_perc = charts.no_show_card()
    main_content = html.Div([        
        html.Div([
            html.Div([
                html.Div([
                    html.Div([
                        html.H6("Age Group"),
                        age_filter
                    ], className="col"),
                    html.Div([
                    html.H6("Medical Condition"),
                    medical_cond_filter
                    ], className="col")
                ], className="row"),
                html.H6("Neighbourhood"),
                area_filter
            ], className="col-6 chart-card", id = "controllers"),
            html.Div([
                dcc.Graph(id="age-gender-dist", figure=charts.age_gender_dist(), className="chart-card"),
            ], className="col-6"),
        ], className="row"),

        html.Div([
# --------------------- Cards ----------------------------------
            html.Div([
                html.Div([
                    html.H6("No-Shows",className="text-center fw-bold text-nowrap"),
                    html.Hr(style={"width": "200px", "border-top": "8px solid #009e73", "margin": "5px auto"}),
                    html.Div([
                        html.Div([
                            html.H6(f"{absence:,}", className="text-center fw-bold text-nowrap")
                        ],className="col"),
                        html.Div([
                            html.H6(f"{absence_perc:.2f}%", className="text-center fw-bold text-nowrap")
                        ], className="col"),
                    ], className="row")
                ], className="card"),

                html.Div([
                    html.H6("Recived SMS", className="text-center fw-bold text-nowrap"),
                    html.Hr(style={"width": "200px", "border-top": "8px solid #009e73", "margin": "5px auto"}),
                    html.H6(f"{charts.recived_sms_card():.2f}%", className="text-center fw-bold text-nowrap")
                ], className="card"),

                html.Div([
                    html.H6("Test")
                ], className="card"),

                html.Div([
                    html.H6("Avg Delay", className="text-center fw-bold text-nowrap"),
                    html.Hr(style={"width": "200px", "border-top": "8px solid #009e73", "margin": "5px auto"}),
                    html.H6(f"{charts.avg_appoint_delay()} Days", className="text-center fw-bold text-nowrap")
                ], className="card")
            ], className="col-2 container", id = "stats-cards"),
# --------------------- charts ----------------------------------
            html.Div([
                html.Div([
                    dcc.Graph(id="appoint-delay", className="col-6 chart-card"),
                    dcc.Graph(id="new-or-lead", className="col-6 chart-card")
                ], className="row"),

                html.Div([
                    dcc.Graph(id="geo-map", className="col-6 chart-card"),
                    dcc.Graph(id="medical-condition", className="col-6 chart-card")
                ], className="row")
            ], className="col-7", id = "middle-charts"),

            html.Div([
                dcc.Graph(id="appoint-gantt", className="chart-card"),
            ], className="col-3")
        ], className="row")

    ], style={"background-color": ""})
    return main_content

def get_layout():
    main_content = get_main_content()
    return main_content
