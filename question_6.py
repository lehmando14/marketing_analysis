def calc_dynamic_clv(retention_rates: list, rev_per_month_per_user: int, discount_rate: int=0.15):
    '''
    retention_rates: the list has to start with a none value and end with a zero value [None, ....., 0]
    '''
    clv = rev_per_month_per_user
    curr_active_prob = 1

    for i in range(1, len(retention_rates)):
        curr_active_prob *= retention_rates[i]
        clv += rev_per_month_per_user * curr_active_prob / (1 + discount_rate)**i

    return clv