#!/usr/bin/env python
import psycopg2
import pandas as pd
import numpy as np
from abacus_tpot import tpot_config

def get_wage_table():
    """
    Return a table of wage data based on the transactional DB
    """
    conn = psycopg2.connect(tpot_config.WAREHOUSE_URI)
    df = pd.read_sql('''
        SELECT p.participant_id, p.program_code, p.provider_id, 
               p.exit_type, p.exit_date, p.entry_date,
               w.amount, w.start_date, w.end_date
            FROM wage w
                LEFT JOIN participant_program p ON w.participant_id=p.participant_id
    ''', conn)
    return df
