from math import floor
import plotly.express as px
from preproccessing import DF
import pandas as pd
from urllib.request import urlopen
import json
with urlopen(
        'https://gis.vitoria.es.gov.br/arcgis/rest/services/DevMapaBaseImobiliario/MapServer/8/query?where=codBairroIBGE%20LIKE%20%273205309%%27&outFields=*&outSR=4326&f=geojson') as response:
    neighbours = json.load(response)
# Filtering with id 273205309% of Vitória

def filter_data(age_group:list = None, med_cond:list = None, area:list = None):
    """
    Filteres data according to user wants:
    by ORing what's in the lists
    n.d. if a choice is none or empty the filter ignores it and returns all possible values
    """
    filtered_df = DF
    if age_group and len(age_group)!=0:
        filtered_df = filtered_df[DF.Age_group.isin(age_group)]
    if med_cond and len(med_cond)!=0:
        # filtered_df = filtered_df[
        #     ((DF.Hipertenstion) if "Hipertenstion" in med_cond else False) |
        #     ((DF.Diabetes) if "Diabetes" in med_cond else False) |
        #     ((DF.Alcholism) if "Alcholism" in med_cond else False) |
        #     ((DF.Handcap) if "Handcap" in med_cond else False)
        #     ]
        mask = pd.Series(False, index=filtered_df.index)
        for cond in med_cond:
            mask |= filtered_df[cond]
        filtered_df = filtered_df[mask]
    if area and len(area)!=0:
        filtered_df = filtered_df[filtered_df.Neighbourhood.isin(area)]
    return filtered_df

def no_show_card(age_group:list = None, med_cond:list=None, area:list=None, format:str="Value"):
    filtered_df = filter_data(age_group, med_cond, area)

    num_absence = filtered_df.shape[0] - filtered_df.Showed.sum()
    if format == "Value":
        return f"{num_absence:,}"
    return  f"{(num_absence*100 / filtered_df.shape[0]):.2f}%"

def recived_sms_card(age_group:list = None, med_cond:list=None, area:list=None):
    filtered_df = filter_data(age_group, med_cond, area)

    filtered_df = filtered_df[ ~ filtered_df.Showed]
    num_SMS = filtered_df.SMS_received.sum()
    return f"{(num_SMS*100 / filtered_df.shape[0]):.2f}%"

def avg_appoint_delay(age_group:list=None, med_cond:list = None, area:list = None):
    filtered_df = filter_data(age_group, med_cond, area)
    return f"{floor(filtered_df.Delay.median())} Days"

def with_scholarship(age_group:list=None, med_cond:list=None, area:list=None):
    filtered_df = filter_data(age_group, med_cond, area)

    filtered_df = filtered_df[~filtered_df.Showed]
    num_scholars = filtered_df.Scholarship.sum()
    return f"{(num_scholars * 100 / filtered_df.shape[0]):.2f}%"

def age_gender_dist():
    age_group = DF[~DF.Showed].groupby(["Age_group", "Gender"]).size()
    age_group = age_group.reset_index(name = "Count")
    age_group['total'] = age_group.groupby("Age_group")["Count"].transform("sum")
    age_group.sort_values("total", ascending = False, inplace = True)

    # print(age_group.columns)
    g = px.bar(age_group,  "Age_group", "Count", color = "Gender",
               color_discrete_map={
                   "M": "lightblue",
                   "F": "pink"
               })

    g.update_layout(dict(
        title="No-Shows Distribution by Age Group & Gender",
        xaxis_title="Age Groups",
        yaxis_title="Count", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))

    return g

def appoint_delay_hist(age_group:list, med_cond:list, area:list):
    filtered_df = filter_data(age_group, med_cond, area)
    filtered_df = filtered_df[~ filtered_df.Showed]
    filtered_df = filtered_df[filtered_df.Delay>=0]
    g = px.histogram(filtered_df, x= "Delay", nbins=20, color_discrete_sequence=["#009e73"])

    g.update_layout(dict(
        title="Delay by Days Between Schedule and Appointment",
        xaxis_title="Delay (Days)",
        yaxis_title="Count", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))
    g.update_xaxes(nticks=20, tickangle = -30)
    return g

def new_lead_donut(age_group:list = None, med_cond:list = None, area:list = None):
    filtered_df = filter_data(age_group, med_cond, area)
    filtered_df = filtered_df[~ filtered_df.Showed]
    cat = filtered_df.Lead.value_counts().reset_index(name = "Count")
    cat.Lead = cat.Lead.apply(lambda x: "Lead Customer" if x else "New Customer")

    g= px.pie(cat, "Lead", "Count", hole=0.3, color_discrete_sequence=["#009e73"])
    g.update_layout(dict(
        title="New VS Lead Customers No-Shows",paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))
    g.update_traces(textinfo="label+percent")

    return g

def medical_cond_donut(age_group:list = None, area:list = None):
    filtered_data = filter_data(age_group, area =  area)

    conditions_count = [0, 0, 0, 0]
    conditions_count[0] = dict(cond="Hipertension", Count= filtered_data.Hipertension.sum())
    conditions_count[1] = dict(cond="Diabetes", Count=filtered_data.Diabetes.sum())
    conditions_count[2] = dict(cond="Alcoholism", Count=filtered_data.Alcoholism.sum())
    conditions_count[3] = dict(cond="Handcap", Count=filtered_data.Handcap.sum())

    conditions_count = pd.DataFrame(conditions_count)
    g= px.pie(conditions_count, "cond", "Count", hole=0.3, color_discrete_sequence=px.colors.sequential.Aggrnyl)
    g.update_layout(dict(
        title="No-shows by Medical Condition", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))
    g.update_traces(textinfo="label+percent")

    return g

def appoint_gantt(age_group:list = None, med_cond:list = None, area:list = None):
    filtered_data = filter_data(age_group, med_cond, area)
    filtered_data = filtered_data[(~filtered_data.Showed ) & (filtered_data.Delay>0)]
    df_sorted_first20 = (
        filtered_data.sort_values(["Delay", "AppointmentDay"], ascending=[True, False])
        .groupby("Delay", group_keys=False)
        .head(40)
    )

    g = px.timeline(df_sorted_first20, x_start="ScheduledDay", x_end="AppointmentDay", y="Delay", color = "Age_group", color_discrete_sequence=px.colors.sequential.Aggrnyl)
    g.update_yaxes(autorange="reversed")
    g.update_layout(dict(
        title="Filtered No-Shows Timeline (Recent 40 in each Delay)",
        xaxis_title="Time",
        yaxis_title="Delay in Days", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))
    return g

def geo_map(age_group:list = None, med_cond:list = None):
    filtered_data = filter_data(age_group, med_cond)

    no_show_stats = (
        filtered_data
        .groupby("Neighbourhood")
        .agg(
            total=("Showed", "count"),
            showed=("Showed", "sum")
        )
    )
    no_show_stats["showed"] = no_show_stats["showed"] *100 / no_show_stats["total"]
    no_show_stats["not_showed"] = 100 - no_show_stats["showed"]
    no_show_stats.reset_index(inplace=True)

    g = px.choropleth_map(no_show_stats, geojson=neighbours, locations='Neighbourhood', color='not_showed',
                            map_style="carto-positron",
                            zoom=10.8, center = {"lat": -20.2779197, "lon": -40.3011542},
                            range_color=(0, 100),
                            opacity=0.8,
                            color_continuous_scale= 'Aggrnyl',
                            featureidkey="properties.nome",
                            labels={'not_showed': 'No-Shows Perc'}
                            )
    g.update_layout(dict(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        title="No-Shows Percentage by Neighbourhood",
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    ))
    return g
