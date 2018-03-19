import pandas as pd
import numpy as np
from abacus_tpot import tpot_config

def median_wage(wage_table, participants, reporting_period_start, reporting_period_end):
    """
    Return the median total wage over a reporting period for a list of participants
    """

    reporting_period_start = pd.to_datetime(reporting_period_start)
    reporting_period_end = pd.to_datetime(reporting_period_end)
    wage_table = wage_table[wage_table.participant_id.isin(participants)]
    wage_table = wage_table[wage_table.end_date >= reporting_period_start]
    wage_table = wage_table[wage_table.start_date < reporting_period_end]
    wage_table['frac_wage'] = wage_table.wageamt * \
        ((wage_table.end_date.apply(lambda a: min(a, reporting_period_end)) -
        wage_table.start_date.apply(lambda a: max(a, reporting_period_start))).apply(lambda a: a.days) /
        (wage_table.end_date - wage_table.start_date).apply(lambda a: float(a.days)))

    # Compute total wages for each participant
    wages_by_person = wage_table.groupby('participant_id').frac_wage.sum()

    # Check anonymization cutoff
    if len(wages_by_person) < tpot_config.ANONYMIZATION_THRESHOLD:
        return None

    # Return the median
    return np.median(wages_by_person.values)


def median_wage_after_exit_date(wage_table, participants,
                                reporting_interval_start,
                                reporting_interval_end):
    """
    Return the median total wage over a reporting period defined versus the
    program exit date, for a list of participants
    """

    reporting_interval_start = pd.to_timedelta(reporting_interval_start)
    reporting_interval_end = pd.to_timedelta(reporting_interval_end)
    wage_table = wage_table[wage_table.participant_id.isin(participants)]
    wage_table = wage_table[wage_table.end_date >= (wage_table.exit_date + reporting_interval_start)]
    wage_table = wage_table[wage_table.start_date < (wage_table.exit_date + reporting_interval_end)]
    wage_table['frac_wage'] = wage_table.amount * \
        ((np.minimum(wage_table.end_date, wage_table.exit_date + reporting_interval_end) -
        np.maximum(wage_table.start_date, wage_table.exit_date + reporting_interval_start)).apply(lambda a: a.days) /
        (wage_table.end_date - wage_table.start_date).apply(lambda a: float(a.days)))

    # Compute total wages for each participant
    wages_by_person = wage_table.groupby('participant_id').frac_wage.sum()

    # Check anonymization cutoff
    if len(wages_by_person) < tpot_config.ANONYMIZATION_THRESHOLD:
        return None

    # Return the median
    return np.median(wages_by_person.values)
