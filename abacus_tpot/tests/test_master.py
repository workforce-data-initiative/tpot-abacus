from unittest import TestCase

import abacus_tpot


class TestParticipantMasterRecordCreate(TestCase):
    def setUp(self):
        self.s = abacus_tpot.master.participant_master_record_create()

    def test_is_nonetype(self):
        # The method is an empty block for now
        self.assertEqual(self.s, None)


class TestProgramOutcomes(TestCase):
    def setUp(self):
        self.s = abacus_tpot.master.program_outcomes()

    def test_is_nonetype(self):
        # The method is an empty block for now
        self.assertEqual(self.s, None)


class TestProgramOutcomesTableAnonymizationCheck(TestCase):
    def setUp(self):
        self.s = abacus_tpot.master.program_outcomes_table_anonymization_check()

    def test_is_nonetype(self):
        # The method is an empty block for now
        self.assertEqual(self.s, None)
