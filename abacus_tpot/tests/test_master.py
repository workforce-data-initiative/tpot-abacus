#!/usr/bin/env python
import unittest
from unittest import TestCase
import pandas as pd
import numpy as np

from abacus_tpot.outcomes.wioa import median_wage_n_quarters_after_exit,\
    employed_n_quarters_after_exit


class TestMedianWage(TestCase):
    def setUp(self):
        self.wage_table = pd.DataFrame(
            {'participant_id': range(1, 21),
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
        s = employed_n_quarters_after_exit(self.wage_table, range(1, 21), 1)
        self.assertEqual(s, 10)


if __name__ == '__main__':
    unittest.main()
