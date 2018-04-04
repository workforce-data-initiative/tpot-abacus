#!/usr/bin/env python
import psycopg2
import pandas as pd
import numpy as np
from abacus_tpot import tpot_config

def get_participant_table():
    """
    Return a list of participant IDs in a given program ID
    """
    conn = psycopg2.connect(tpot_config.WAREHOUSE_URI)
    df = pd.read_sql('''
        SELECT participant_id, program_code, provider_id, exit_type, entry_date, exit_date,
               obtained_credentials, potential_credentials, funding_sources, program_name,
               service_location
            FROM program_participant
    ''', conn)
    return df

def filter_participants(df, provider_id=None,
                        program_code=None,
                        min_entry_date=None,
                        max_entry_date=None,
                        min_exit_date=None,
                        max_exit_date=None,
                        exit_type=None):
    if provider_id is not None:
        df = df[df.provider_id==provider_id]
    if program_code is not None:
        df = df[df.program_code==program_code]
    if min_entry_date is not None:
        entry_date = pd.to_datetime(min_entry_date)
        df = df[df.entry_date >= min_entry_date]
    if min_exit_date is not None:
        exit_date = pd.to_datetime(min_exit_date)
        df = df[df.exit_date >= min_exit_date]
    if max_entry_date is not None:
        entry_date = pd.to_datetime(max_entry_date)
        df = df[df.entry_date <= max_entry_date]
    if max_exit_date is not None:
        exit_date = pd.to_datetime(max_exit_date)
        df = df[df.exit_date <= max_exit_date]
    if exit_type is not None:
        df = df[df.exit_type == exit_type]

    retval = df.participant_id.unique()
    return retval
