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
        SELECT ParticipantID, ProgramID, ExitTypeID, EntryDate, ExitDate, Enrolled
            FROM ParticipantProgram p
    ''', conn)
    return df

def filter_participants(df, program_id=None,
                        min_entry_date=None,
                        max_entry_date=None,
                        min_exit_date=None,
                        max_exit_date=None,
                        exit_type_id=None,
                        enrolled=None):
    if program_id is not None:
        df = df[df.programid==program_id]
    if min_entry_date is not None:
        entry_date = pd.to_datetime(min_entry_date)
        df = df[df.entrydate >= min_entry_date]
    if min_exit_date is not None:
        exit_date = pd.to_datetime(min_exit_date)
        df = df[df.exitdate >= min_exit_date]
    if max_entry_date is not None:
        entry_date = pd.to_datetime(max_entry_date)
        df = df[df.entrydate <= max_entry_date]
    if max_exit_date is not None:
        exit_date = pd.to_datetime(max_exit_date)
        df = df[df.exitdate <= max_exit_date]
    if exit_type_id is not None:
        df = df[df.exittypeid == exit_type_id]
    if enrolled is not None:
        df = df[df.enrolled == enrolled]

    retval = df.participantid.unique()
    return retval
