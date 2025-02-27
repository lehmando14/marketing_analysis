import pandas as pd
from datetime import datetime

class CohortDateMapper:

    def __init__(self, df: pd.DataFrame):
        date_df = df[['time_year', 'time_month']].drop_duplicates()
        dates = list(date_df.to_records(index=False))
        dates = sorted(dates, key= (lambda x : datetime(int(x[0]), int(x[1]), 1)))

        self.date_cohort_mapping = {cohort: date for (cohort, date) in zip(range(12), dates)}

    def periods_to_months(self, periods: list):
        months_in_int = [self.date_cohort_mapping[period][1] for period in periods]

        def int_to_month(number: int):
            months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
            ]

            # Check if the number is within a valid range
            if 1 <= number <= 12:
                return months[number - 1]
            else:
                return "Invalid month number"
            
        return [int_to_month(number) for number in months_in_int]

