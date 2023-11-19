def calculate_exp_lifetime(avg_retention_rates_per_month: list) -> list:
    active_probs = calc_active_probs(avg_retention_rates_per_month)
    probs_of_surviving_exactly_i_months = calc_probs_of_surviving_exactly_i_months(
        active_probs,
        avg_retention_rates_per_month
    )

    expected_lifetime = 0
    for i, survival_prob_month_i in enumerate(probs_of_surviving_exactly_i_months):
        expected_lifetime += i * survival_prob_month_i

    return expected_lifetime

def calc_active_probs(retention_rates_per_month: list) -> list:
    '''currently only works for cohort 0 because of range 1, 12'''
    active_probabilities = [1]
    for period in range(1, 12):

        if retention_rates_per_month[period] == None: 
            return active_probabilities
        
        active_probabilities.append(
            retention_rates_per_month[period] * active_probabilities[period - 1]
        )

    return active_probabilities

def calc_probs_of_surviving_exactly_i_months(active_probs: list, retention_rates_per_month: list) -> list:
    '''currently only works for cohort 0 because of indexing'''
    probs_of_surviving_exactly_i_months = []
    for period in range(11):
        if retention_rates_per_month[period + 1] == None:
            return probs_of_surviving_exactly_i_months + [active_probs[period]]

        probs_of_surviving_exactly_i_months.append(
            active_probs[period] * (1 - retention_rates_per_month[period + 1])
    )
                
    return probs_of_surviving_exactly_i_months

