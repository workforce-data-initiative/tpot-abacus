#!/usr/bin/env python
import psycopg2
import pandas as pd
import numpy as np
import tpot_config

def get_wage_table():
    """
    Return a table of wage data based on the transactional DB
    """
    conn = psycopg2.connect(tpot_config.WAREHOUSE_URI)
    df = pd.read_sql('''
        SELECT p.ParticipantID, p.ProgramID, p.ExitTypeID, p.ExitDate, p.Enrolled, p.EntryDate,
               w.WageAmt, w.WageStartDate, w.WageEndDate,
               pa.WioaParticipant, pa.WioaItaParticipant
            FROM Wage w
                LEFT JOIN ParticipantProgram p ON w.ParticipantID=p.ParticipantID
                LEFT JOIN Participant pa ON w.ParticipantID=pa.ParticipantID
    ''', conn)
    return df
