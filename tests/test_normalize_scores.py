import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from examples.normalize_scores import normalize_scores

class TestNormalizeScores(unittest.TestCase):
    def test_normalizes(self): self.assertEqual(normalize_scores([1.,2.,3.]), [1/6,2/6,3/6])
    def test_zero(self): self.assertEqual(normalize_scores([0.,0.]), [0.,0.])
    def test_negative(self):
        with self.assertRaises(ValueError): normalize_scores([-1.,2.])

if __name__=='__main__':unittest.main()
