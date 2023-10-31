import pandas as pd
from datetime import datetime

class CohortDateMapper:

    def __init__(self, df: pd.DataFrame):
        date_df = df[['time_year', 'time_month']].drop_duplicates()
        dates = list(date_df.to_records(index=False))
        dates = sorted(dates, key= (lambda x : datetime(int(x[0]), int(x[1]), 1)))

        self.date_cohort_mapping = {cohort: date for (cohort, date) in zip(range(12), dates)}
