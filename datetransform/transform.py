import numpy as np
import pandas as pd

def add_date_features(df: pd.DataFrame, date_field_name: str, time=True):
    make_date(df, date_field_name)
    field = df[date_field_name]
    attr = ['Year', 'Month', 'Week', 'Day', 'DayOfWeek', 'DayOfYear', 'Is_Month_End', 'Is_Month_Start',
            'Is_Quarter_End', 'Is_Quarter_Start', 'Is_Year_End', 'Is_Year_Start']
    if time:
        attr = attr + ['Hour', 'Minute', 'Second']
    for n in attr:
        df[date_field_name + n.replace('_', '')] = getattr(field.dt, n.lower())
    return df


def make_date(df: pd.DataFrame, date_field_name: str):
    "Make sure `df[field_name]` is of the right date type."
    field_dtype = df[date_field_name].dtype
    if isinstance(field_dtype, pd.core.dtypes.dtypes.DatetimeTZDtype):
        field_dtype = np.datetime64
    if not np.issubdtype(field_dtype, np.datetime64):
        df[date_field_name] = pd.to_datetime(df[date_field_name], infer_datetime_format=True)
