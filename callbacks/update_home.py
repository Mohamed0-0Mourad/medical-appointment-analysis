from dash import Input, Output
import charts

def register_callbacks(app):
    @app.callback(Output("appoint-delay", "figure"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_hist(age_group:list, med_cond:list, area:list):
        return charts.appoint_delay_hist(age_group, med_cond, area)

    @app.callback(Output("new-or-lead", "figure"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_donut(age_group:list, med_cond:list, area:list):
        return charts.new_lead_donut(age_group, med_cond, area)

    @app.callback(Output("medical-condition", "figure"), [
        Input("age-group-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_cond_donut(age_group: list, area: list):
        return charts.medical_cond_donut(age_group, area = area)

    @app.callback(Output("appoint-gantt", "figure"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_gantt(age_group: list, med_cond: list, area: list):
        return charts.appoint_gantt(age_group, med_cond, area)
