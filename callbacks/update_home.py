from dash import Input, Output
import charts

def register_callbacks(app):
    @app.callback(Output("avg_delay", "children"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_card_avg_appoint(age_group:list, med_cond:list, area:list):
        return charts.avg_appoint_delay(age_group, med_cond, area)

    @app.callback(Output("sms_recieved", "children"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_sms_recieved(age_group:list, med_cond:list, area:list):
        return charts.recived_sms_card(age_group, med_cond, area)

    @app.callback(Output("scholarship_recieved", "children"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_scholarship_recieved(age_group:list, med_cond:list, area:list):
        return charts.with_scholarship(age_group, med_cond, area)

    @app.callback(Output("No-Shows-Value", "children"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_no_show_value(age_group:list, med_cond:list, area:list):
        return charts.no_show_card(age_group, med_cond, area)

    @app.callback(Output("No-Shows-Perc", "children"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
        Input("area-filter-group", "value")
    ])
    def update_no_show_perc(age_group: list, med_cond: list, area: list):
        return charts.no_show_card(age_group, med_cond, area, "Percentage")

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

    @app.callback(Output("geo-map", "figure"), [
        Input("age-group-filter", "value"),
        Input("medical-cond-filter", "value"),
    ])
    def update_map(age_group: list, med_cond: list):
        return charts.geo_map(age_group, med_cond)
