import pandas as pd

from datetransform import transform


def test_add_date_features():
    df = pd.DataFrame({'dateCol': ['2019-08-09 16:39:47']})
    df = transform.add_date_features(df, 'dateCol')
    assert df.columns.tolist() == ['dateCol',
                                   'dateColYear',
                                   'dateColMonth',
                                   'dateColWeek',
                                   'dateColDay',
                                   'dateColDayOfWeek',
                                   'dateColDayOfYear',
                                   'dateColIsMonthEnd',
                                   'dateColIsMonthStart',
                                   'dateColIsQuarterEnd',
                                   'dateColIsQuarterStart',
                                   'dateColIsYearEnd',
                                   'dateColIsYearStart',
                                   'dateColHour',
                                   'dateColMinute',
                                   'dateColSecond']


def test_inplace_transform():
    df = pd.DataFrame({'dateCol': ['2019-08-09 16:39:47']})
    transform.add_date_features(df, 'dateCol', inplace=True)
    assert df.columns.tolist() == ['dateCol',
                                   'dateColYear',
                                   'dateColMonth',
                                   'dateColWeek',
                                   'dateColDay',
                                   'dateColDayOfWeek',
                                   'dateColDayOfYear',
                                   'dateColIsMonthEnd',
                                   'dateColIsMonthStart',
                                   'dateColIsQuarterEnd',
                                   'dateColIsQuarterStart',
                                   'dateColIsYearEnd',
                                   'dateColIsYearStart',
                                   'dateColHour',
                                   'dateColMinute',
                                   'dateColSecond']


def test_not_inplace_transform():
    df = pd.DataFrame({'dateCol': ['2019-08-09 16:39:47']})
    transform.add_date_features(df, 'dateCol')
    assert df.columns.tolist() == ['dateCol']