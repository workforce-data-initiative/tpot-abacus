#!/usr/bin/env python
import psycopg2
import pandas as pd
import numpy as np
from abacus_tpot import tpot_config


def get_wages(ids):
    if len(ids) == 0:
        return None
    conn = psycopg2.connect(tpot_config.WAGE_RECORD_URI)
    df = pd.read_sql('''
        SELECT id, year, q1_wage, q2_wage, q3_wage, q4_wage
        FROM wage WHERE id IN %s
    ''', conn, params=(tuple(ids),))
    df = pd.melt(df, id_vars=['id', 'year'],
                 value_vars=['q1_wage', 'q2_wage', 'q3_wage', 'q4_wage'])
    df['start_date'] = pd.to_datetime(
        pd.Series([str(i) for i in df.year.values]) + 'Q' +
        pd.Series([i[1] for i in df.variable.values]))
    df['end_date'] = df.start_date + pd.offsets.QuarterEnd()
    df['amount'] = df['value']
    del(df['variable'])
    del(df['value'])
    return df


def get_wage_table(ids):
    """
    Return a table of wage data based on the transactional DB
    """
    if len(ids) == 0:
        return None
    wages = get_wages(ids)
    conn = psycopg2.connect(tpot_config.WAREHOUSE_URI)
    df = pd.read_sql('''
        SELECT p.participant_id, o.program_code, p.provider_id,
               p.program_id, p.exit_type, p.exit_date, p.entry_date
            FROM program_participant p JOIN program o ON p.program_id=o.id
            WHERE participant_id IN %s
    ''', conn, params=(tuple(ids),))
    retval = pd.merge(wages, df, how='left', left_on='id',
                      right_on='participant_id')
    return retval
