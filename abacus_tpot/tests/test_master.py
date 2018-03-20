#!/usr/bin/env python
import unittest
from unittest import TestCase
import pandas as pd
import numpy as np

from abacus_tpot.outcomes.wioa import median_wage_n_quarters_after_exit,\
                                      employment_n_quarters_after_exit
from abacus_tpot.input_db.participants import filter_participants


class TestParticipantList(TestCase):
    def setUp(self):
        self.participant_table = pd.DataFrame(
            {
              'participant_id': range(1, 21),
              'provider_id':    np.append(np.ones(10), np.ones(10) * 2),
              'program_code':   np.append(np.ones(10), np.ones(10) * 2),
              'exit_type':      np.append(np.ones(16), np.zeros(4)),
              'entry_date':     np.append(np.repeat(pd.to_datetime('1/1/2016'), 17),
                                          np.repeat(pd.to_datetime('7/1/2016'), 3)),
              'exit_date':      np.append(np.repeat(pd.to_datetime('6/30/2016'), 18),
                                          np.repeat(pd.to_datetime('12/31/2016'), 2))
            })

    def test_programid_filter(self):
        s = filter_participants(self.participant_table, program_code=1)
        self.assertEqual(len(s), 10)

    def test_exittype_filter(self):
        s = filter_participants(self.participant_table, exit_type=1)
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
            { 'participant_id': range(1, 21),
              'provider_id':   np.ones(20),
              'program_code':  np.ones(20),
              'exit_type':     np.ones(20),
              'entry_date':    np.repeat(pd.to_datetime('1/1/2016'), 20),
              'exit_date':     np.repeat(pd.to_datetime('12/31/2016'), 20),
              'amount':        np.ones(20) * 1000.0,
              'start_date':    np.append(np.repeat(pd.to_datetime('1/1/2017'), 10),
                                         np.repeat(pd.to_datetime('4/1/2017'), 10)),
              'end_date':      np.append(np.repeat(pd.to_datetime('3/31/2017'), 10),
                                         np.repeat(pd.to_datetime('6/30/2017'), 10))
            })

    def test_onequarter_wages(self):
        s = median_wage_n_quarters_after_exit(self.wage_table, range(1, 11), 1)
        self.assertEqual(s, 1000.0)

    def test_onequarter_employment(self):
        s = employment_n_quarters_after_exit(self.wage_table, range(1, 21), 1)
        self.assertEqual(s, 50)

if __name__ == '__main__':
    unittest.main()
