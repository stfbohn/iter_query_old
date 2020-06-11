import unittest
from iter_query import Qi

class ListEmptyTests(unittest.TestCase):

    def test_to_list(self):
        test_list = []
        res = Qi(test_list) \
                    .to_list()
        assert res == []

    def test_map(self):
        test_list = []
        res = Qi(test_list) \
                .map(lambda e: e**2) \
                .to_list()
        assert res == []

    def test_filter(self):
        test_list = []
        res = Qi(test_list) \
                .filter(lambda e: e >= 2) \
                .to_list()
        assert res == []

    def test_first(self):
        test_list = []
        with self.assertRaises(StopIteration) as context:
            res = Qi(test_list).first()
        
    def test_take(self):
        test_list = []
        res = Qi(test_list) \
                .take(3) \
                .to_list()
        assert res == []

    def test_count_contains(self):
        test_list = []
        assert Qi(test_list).count() == 0
        assert Qi(test_list).contains(2) == False
        
    def test_min_max(self):
        test_list = []
        with self.assertRaises(ValueError) as context:
            res = Qi(test_list).min() == 1
        with self.assertRaises(ValueError) as context:
            res = Qi(test_list).max() == 1
        with self.assertRaises(ValueError) as context:
            res = Qi(test_list).max(key = lambda e: -(e-2)**2) 
        with self.assertRaises(ValueError) as context:
            res = Qi(test_list).min(key = lambda e: (e-2)**2) 

    def test_distinct(self):
        test_list = []
        res = Qi(test_list).distinct().to_list()
        assert res == []

    def test_sort(self):
        test_list = []
        res = Qi(test_list).sort().to_list()
        assert res == []


if __name__ == '__main__':
    unittest.main()
