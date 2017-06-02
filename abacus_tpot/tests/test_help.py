from unittest import TestCase

import abacus_tpot


class TestHelp(TestCase):
    def setUp(self):
        self.s = abacus_tpot.help()

    def test_is_string(self):
        self.assertTrue(isinstance(self.s, str))

    def test_text_in_string(self):
        self.assertIn("ready", self.s)
