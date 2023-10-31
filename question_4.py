def calculate_exp_lifetime(avg_retention_rates_per_month: list) -> list:
    active_probs = calc_active_probs(avg_retention_rates_per_month)
    probs_of_surviving_exactly_i_months = calc_probs_of_surviving_exactly_i_months(
        active_probs,
        avg_retention_rates_per_month
    )

    expected_lifetime = 0
    for i in range(12):
        expected_lifetime += (i+1) * probs_of_surviving_exactly_i_months[i]

    return expected_lifetime

def calc_active_probs(avg_retention_rates_per_month: list) -> list:
    active_probabilities = [1]
    for period in range(1, 12):
        active_probabilities.append(
            avg_retention_rates_per_month[period] * active_probabilities[period - 1]
    )
        
    return active_probabilities

def calc_probs_of_surviving_exactly_i_months(active_probs: list, avg_retention_rates_per_month: list) -> list:
    probs_of_surviving_exactly_i_months = []
    for period in range(11):
        probs_of_surviving_exactly_i_months.append(
            active_probs[period] * (1 - avg_retention_rates_per_month[period + 1])
    )
        
    #special case as there is no period after the 11th
    probs_of_surviving_exactly_i_months.append(
        active_probs[11]
    )      
        
    return probs_of_surviving_exactly_i_months

