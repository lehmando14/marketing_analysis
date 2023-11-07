import matplotlib.pyplot as plt
import pandas as pd

from utilities import CohortDateMapper


#---------------------------------main functions -------------------------------------------------------------------------------

def calculate_retention_rates_of_cohort_i(customer_df: pd.DataFrame, cohort: int, cdm: CohortDateMapper) -> dict:
    observation_per_period = _count_observations_of_cohort_i_per_period(customer_df, cohort, cdm)
    retention_rates = _calculate_retention_rates(observation_per_period, cohort)
    return retention_rates

def calculate_avg_retention_rate(retention_rates: dict) -> int:
    retention_rates_without_none = _remove_none_from_dict(retention_rates)
    retention_rates_l = list(retention_rates_without_none.values())
    avg_retention_rate = sum(retention_rates_l) / len(retention_rates_l)
    return avg_retention_rate
    
def plot_retention_rate_of_cohort_i(retention_rates: dict, cohort: int):
    retention_rates_without_none = _remove_none_from_dict(retention_rates)
    times, retention_rates = zip(*list(retention_rates_without_none.items()))

    plt.bar(times, retention_rates)

    plt.xlabel('Time')
    plt.ylabel('Retention Rate')
    plt.title(f'Retention Rate of Cohort ({cohort}) Users in each Period')
    plt.show()

#-------------------------------------helper functions----------------------------------------------------------------------------

def _count_observations_of_cohort_i_per_period(customer_df: pd.DataFrame, cohort: int, cdm: CohortDateMapper) -> dict:
    observations_per_period = dict()

    for time in range(0, 12):
        year, month = cdm.date_cohort_mapping[time]
        date_index = (customer_df['time_year'] == year) & (customer_df['time_month'] == month)
        users_at_time_df = customer_df[date_index]

        cohort_users_at_time_df = users_at_time_df[
            users_at_time_df['cohort'] == cohort
        ]

        number_of_users = len(cohort_users_at_time_df['user'].drop_duplicates())
        observations_per_period[time] = number_of_users

    return observations_per_period

def _calculate_retention_rates(observed_amount: dict, cohort: int) -> dict:
    '''Outputs retention rates of each period based in input observations per period'''
    retention_rates = dict()

    retention_rates[cohort] = None

    for time in range(cohort + 1, 12):

        try:
            retention_rates[time] = (
                observed_amount[time] / 
                observed_amount[time - 1]
            )

        except ZeroDivisionError:
            retention_rates[time] = None

    return retention_rates

def _remove_none_from_dict(d: dict):
    '''removes all none value items from the dictionary'''
    filtered_dict = {key: value for key, value in d.items() if value is not None}
    return filtered_dict