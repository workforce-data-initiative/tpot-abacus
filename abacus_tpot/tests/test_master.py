from unittest import TestCase
import pandas as pd
import numpy as np

from outcomes.median_wage import median_wage, median_wage_after_exit_date
from input_db.participants import filter_participants


class TestParticipantList(TestCase):
    def setUp(self):
        self.participant_table = pd.DataFrame(
            {
              'participantid': range(1, 21),
              'programid':     np.append(np.ones(10), np.ones(10) * 2),
              'exittypeid':    np.append(np.ones(16), np.zeros(4)),
              'entrydate':     np.append(np.repeat(pd.to_datetime('1/1/2016'), 17),
                                         np.repeat(pd.to_datetime('7/1/2016'), 3)),
              'exitdate':      np.append(np.repeat(pd.to_datetime('6/30/2016'), 18),
                                         np.repeat(pd.to_datetime('12/31/2016'), 2)),
              'enrolled':      np.append(np.ones(15), np.zeros(5))
            })

    def test_programid_filter(self):
        s = filter_participants(self.participant_table, program_id=1)
        self.assertEqual(len(s), 10)

    def test_enrolled_filter(self):
        s = filter_participants(self.participant_table, enrolled=1)
        self.assertEqual(len(s), 15)

    def test_exittype_filter(self):
        s = filter_participants(self.participant_table, exit_type_id=1)
        self.assertEqual(len(s), 16)

    def test_min_entry_date_filter(self):
        s = filter_participants(self.participant_table, min_entry_date='6/1/2016')
        self.assertEqual(len(s), 3)

    def test_min_exit_date_filter(self):
        s = filter_participants(self.participant_table, min_exit_date='7/1/2016')
        self.assertEqual(len(s), 2)

    def test_max_entry_date_filter(self):
        s = filter_participants(self.participant_table, max_entry_date='6/1/2016')
        self.assertEqual(len(s), 17)

    def test_max_exit_date_filter(self):
        s = filter_participants(self.participant_table, max_exit_date='7/1/2016')
        self.assertEqual(len(s), 18)


class TestMedianWage(TestCase):
    def setUp(self):
        self.wage_table = pd.DataFrame(
            { 'participantid': range(1, 21),
              'programid':     np.ones(20),
              'exittypeid':    np.ones(20),
              'entrydate':     np.repeat(pd.to_datetime('1/1/2016'), 20),
              'exitdate':      np.append(np.repeat(pd.to_datetime('12/31/2016'), 10),
                                         np.repeat(pd.to_datetime('1/31/2017'), 10)),
              'enrolled':      np.ones(20),
              'wageamt':       np.append(np.ones(10) * 1000.0, np.ones(10) * 2000.0),
              'wagestartdate': np.append(np.repeat(pd.to_datetime('1/1/2017'), 10),
                                         np.repeat(pd.to_datetime('2/1/2017'), 10)),
              'wageenddate':   np.append(np.repeat(pd.to_datetime('1/31/2017'), 10),
                                         np.repeat(pd.to_datetime('2/28/2017'), 10)),
              'wioaparticipant':    np.ones(20),
              'wioaitaparticipant': np.ones(20)
            })

    def test_onemonth_wages(self):
        s = median_wage(self.wage_table, range(1, 21), '1/1/2017', '1/31/2017')
        self.assertEqual(s, 1000.0)

    def test_onemonth_post_wages(self):
        s = median_wage_after_exit_date(self.wage_table, range(1, 21), '0 days', '31 days')
        self.assertEqual(s, 1500.0)
