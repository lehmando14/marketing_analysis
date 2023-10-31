from itertools import zip_longest

from utilities import CohortDateMapper
from question_3af import *

def calculate_avg_retention_rates_across_cohorts(customer_df: pd.DataFrame, cdm: CohortDateMapper):
    retention_rates = _get_all_retention_rates_as_lists(customer_df, cdm)
    retention_rates_per_period = []

    for retention_rates_in_period_i in zip_longest(*retention_rates):
        retention_rates_per_period.append(
            _get_avg_retention_rate_in_period(retention_rates_in_period_i)
        )

    return  retention_rates_per_period

def calculate_avg_retention_rates_across_months(customer_df: pd.DataFrame, cdm: CohortDateMapper):
    retention_rates = _get_all_retention_rates_as_lists(customer_df, cdm)
    padded_retention_rates = [[None]*cohort_i + retention_rates_of_cohort_i
                              for cohort_i, retention_rates_of_cohort_i
                              in zip(range(12), retention_rates)]
    retention_rates_per_month = []

    for retention_rates_in_month_i in zip(*padded_retention_rates):
        retention_rates_per_month.append(
            _get_avg_retention_rate_in_period(retention_rates_in_month_i)
        )

    return retention_rates_per_month


#-----------------------------------helper functions------------------------------------------------------------------------------------------

def _get_all_retention_rates_as_lists(customer_df: pd.DataFrame, cdm: CohortDateMapper):
    '''
    1. first creates a list out of all dicts with retention rates
    2. converts all the dicts to lists sorted on the keys
    3. removes the key and creates lists where the value for index i corresponds to retention after i time periods
    '''
    retention_rates_per_cohort = [calculate_retention_rates_of_cohort_i(customer_df, cohort, cdm) 
                                  for cohort in range(12)
    ]
    retention_rates_as_lists = [sorted(retention_rates_cohort_i.items(), key= lambda x: x[0])
                                for retention_rates_cohort_i
                                in retention_rates_per_cohort
    ]
    retention_rates_without_period = [list(map(lambda x: x[1], retention_rates_cohort_i))
                                      for retention_rates_cohort_i
                                      in retention_rates_as_lists]

    return retention_rates_without_period

def _get_avg_retention_rate_in_period(retention_rates: tuple):
    sum = 0
    elements = 0
    for retention_rate in retention_rates:
        if retention_rate != None:
            elements += 1
            sum += retention_rate

    return sum / elements