import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from rank_candidates import score,rank
class TestRanking(unittest.TestCase):
    def test_weighted_score(self):
        self.assertEqual(score({'scores':{'breakthrough':100,'interestingness':100,'technicalDepth':100,'reproducibility':100,'credibility':100}}),100)
    def test_demo_never_published(self):
        c={'id':'x','title':'fake','scores':{'breakthrough':100,'interestingness':100,'technicalDepth':100,'reproducibility':100,'credibility':100},'eligibility':'eligible'}
        self.assertFalse(rank({'date':'2026-10-16','demo':True,'candidates':[c]})['publicationAllowed'])
    def test_unverified_rejected(self):
        c={'id':'x','title':'fake','scores':{'breakthrough':100,'interestingness':100,'technicalDepth':100,'reproducibility':100,'credibility':100},'eligibility':'rejected'}
        self.assertIsNone(rank({'date':'2026-10-16','demo':False,'candidates':[c]})['proposedCandidateId'])
if __name__=='__main__':unittest.main()
