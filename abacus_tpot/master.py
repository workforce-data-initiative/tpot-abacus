#!/usr/bin/env python
import psycopg2
import pandas as pd
import numpy as np

ANONYMIZATION_THRESHOLD = 10
WAREHOUSE_URI = 'postgres://localhost'
conn = psycopg2.connect(WAREHOUSE_URI)
cached_participant_record = None

def get_participant_master_record():
    global cached_participant_record
    if cached_participant_record is not None:
        return cached_participant_record

    df = pd.read_sql('''
        SELECT p.ParticipantID, p.ProgramID, p.ExitTypeID, p.ExitDate, p.Enrolled,
               w.WageAmt, w.WageStartDate, w.WageEndDate,
               pa.WioaParticipant, pa.WioaItaParticipant
            FROM Wage w
                LEFT JOIN ParticipantProgram p ON w.ParticipantID=p.ParticipantID
                LEFT JOIN Participant pa ON w.ParticipantID=pa.ParticipantID
    ''', conn)

    cached_participant_record = df
    return df


def program_participants(program_id):
    df = get_participant_master_record()
    return df[df.programid==program_id].participantid.unique()


def median_wage(participants, reporting_period_start, reporting_period_end):
    if len(set(participants)) < ANONYMIZATION_THRESHOLD:
        return None

    reporting_period_start = pd.to_datetime(reporting_period_start)
    reporting_period_end = pd.to_datetime(reporting_period_end)
    df = get_participant_master_record()
    participant_wages = df[df.participantid.isin(participants)]
    monthly_wages = pd.DataFrame(
        [[participantid, wageamt, d] for
        participantid, programid, exittypeid, exitdate, enrolled,
        wageamt, wagestartdate, wageenddate, wioaparticipant, wioaitaparticipant
        in df.itertuples(index=False)
        for d in pd.date_range(wagestartdate, wageenddate, freq='MS')],
        columns=['pid', 'amt', 'date'])
    monthly_wages = monthly_wages[monthly_wages.date >= reporting_period_start]
    monthly_wages = monthly_wages[monthly_wages.date <= reporting_period_end]
    wages_by_person = monthly_wages.groupby('pid').amt.sum()
    return np.median(wages_by_person.values)


print(median_wage(program_participants(123456), '1/1/2017', '12/31/2017'))
