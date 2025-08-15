import pandas as pd

def del_outliers(series):
    d = series.sort_values()
    nplus= d.shape[0] + 1
    q1_loc = nplus // 4 - 1
    q1 = d.iloc[q1_loc] + (nplus / 4 - nplus//4) * d.iloc[q1_loc+1]
    # q2 = np.median(d)
    q3_loc = 3 * (q1_loc+1)
    q3 = d.iloc[q3_loc]
    IQR = q3 - q1
    out_m = 1.5 * IQR
    series = series[series > q1-out_m]
    return series[series < out_m + q3]

DF = pd.read_csv("appointments.csv")

# ----- checking neighbourhood integrity -----
# print(DF.Neighbourhood.unique())
def check_dtype():
    # print(DF.info())
    DF.PatientId = DF.PatientId.astype(str)
    DF.AppointmentID = DF.AppointmentID.astype(str)
    DF.ScheduledDay  = pd.to_datetime(DF.ScheduledDay,format="%Y-%m-%dT%H:%M:%SZ", utc=True)
    DF.AppointmentDay  = pd.to_datetime(DF.AppointmentDay,format="%Y-%m-%dT%H:%M:%SZ", utc=True)
    DF[DF.columns[7:13]] = DF[DF.columns[7:13]].astype(bool)
    # print(DF.info())

def transform_no_show():
    """
    Editing the no-show to be show, and changing dtype to be bool
    """
    DF['No-show'] = DF["No-show"].apply(lambda x: 0 if x == "Yes" else 1)
    DF.rename(columns = {"No-show": "Showed"}, inplace = True)
    DF.Showed = DF.Showed.astype(bool)
    # print(DF.Showed.value_counts())

def age_grouping():
    # print(DF.describe()['Age'])
    # print(DF.Age.unique())
    # print(DF[DF.Age < 0].shape) #: 1
    # print(DF[DF.Age < 0].index[0]) #: 99832
    DF.drop(index = DF[DF.Age < 0].index, inplace=True)

    DF['Age_group'] = DF.Age.apply(lambda age: (
        "Child" if age < 13 else
        "Teen" if age < 20 else
        "Young Adult" if age < 40 else
        "Middle-Aged" if age < 60 else
        "Senior"
    ))
    # print(DF.Age_group.value_counts())

def appoint_delay_feature():
    DF["Delay"] = (DF.AppointmentDay - DF.ScheduledDay).dt.days
    # print(DF[DF.AppointmentDay > DF.ScheduledDay].iloc[:, 3:5])

def lead_feature():
    DF["Lead"] = DF.PatientId.duplicated(keep = False)
    # print(DF.Lead.value_counts())

check_dtype()
transform_no_show()
age_grouping()
appoint_delay_feature()
lead_feature()