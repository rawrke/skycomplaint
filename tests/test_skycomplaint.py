import unittest

from skycomplaint import skycomplaint

class TestSkyComplaint(unittest.TestCase):
    def test_empty(self):
        skycomplaint()
