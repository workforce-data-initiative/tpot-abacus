import pandas as pd
import numpy as np
from abacus_tpot import tpot_config

def median_wage_n_quarters_after_exit(wage_table, participants,
                                      n_quarters):
    """
    Return the median total wage for the Nth quarter after the
    program exit date, for a list of participants.
    """
    wage_table = wage_table[wage_table.participant_id.isin(participants)]
    pd.options.mode.chained_assignment = None
    wage_table['exit_quarter'] = pd.to_datetime(wage_table.exit_date.values).year * 4 +\
                                 pd.to_datetime(wage_table.exit_date.values).quarter
    wage_table['quarter'] = pd.to_datetime(wage_table.start_date.values).year * 4 +\
                            pd.to_datetime(wage_table.start_date.values).quarter
    pd.options.mode.chained_assignment = 'warn'
    wage_table = wage_table[wage_table.quarter == (wage_table.exit_quarter + n_quarters)]
    wages_by_person = wage_table.groupby('participant_id').amount.sum()

    # Check anonymization cutoff
    if len(wages_by_person) < tpot_config.ANONYMIZATION_THRESHOLD:
        return None

    # Return the median
    return np.median(wages_by_person.values)


def employment_n_quarters_after_exit(wage_table, participants,
                                     n_quarters):
    """
    Return the percent employed for the Nth quarter after the
    program exit date, for a list of participants.
    """
    wage_table = wage_table[wage_table.participant_id.isin(participants)]
    pd.options.mode.chained_assignment = None
    wage_table['exit_quarter'] = pd.to_datetime(wage_table.exit_date.values).year * 4 +\
                                 pd.to_datetime(wage_table.exit_date.values).quarter
    wage_table['quarter'] = pd.to_datetime(wage_table.start_date.values).year * 4 +\
                            pd.to_datetime(wage_table.start_date.values).quarter
    pd.options.mode.chained_assignment = 'warn'
    wage_table = wage_table[wage_table.quarter == (wage_table.exit_quarter + n_quarters)]
    wages_by_person = wage_table.groupby('participant_id').amount.sum()

    # Check anonymization cutoff
    if len(wages_by_person) < tpot_config.ANONYMIZATION_THRESHOLD:
        return None

    # Return the median
    return 100 * len(wages_by_person.values[wages_by_person.values > 0]) / float(len(participants))
