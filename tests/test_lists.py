import unittest
from iter_query import Qi

class ListTests(unittest.TestCase):

    def test_to_list(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list) \
                    .to_list()
        assert res == [1, 3, 2, 2, -1, 4]

    def test_map(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list) \
                .map(lambda e: e**2) \
                .to_list()
        assert res == [1, 9, 4, 4, 1, 16]

    def test_filter(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list) \
                .filter(lambda e: e >= 2) \
                .to_list()
        assert res == [3, 2, 2, 4]

    def test_first(self):
        test_list = [1, 3, 2, 2, -1, 4]
        assert Qi(test_list).first() == 1
        
    def test_take(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list) \
                .take(3) \
                .to_list()
        assert res == [1, 3, 2]

    def test_count_contains(self):
        test_list = [1, 3, 2, 2, -1, 4]
        assert Qi(test_list).count() == 6
        assert Qi(test_list).contains(2) == True
        assert Qi(test_list).contains(13) == False
        
    def test_min_max(self):
        test_list = [1, 3, 2, 2, -1, 4]
        assert Qi(test_list).min() == -1
        assert Qi(test_list).max() == 4
        assert Qi(test_list).max(key = lambda e: -(e-2)**2) == 2
        assert Qi(test_list).min(key = lambda e: (e-2)**2)  

    def test_distinct(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list).distinct().to_list()
        assert res == [1, 3, 2, -1, 4] # second 2 is dropped

    def test_sort(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list).sort().to_list()
        assert res == [-1, 1, 2, 2, 3, 4]
        res = Qi(test_list).sort(key=lambda e: -e).to_list()
        assert res == [4, 3, 2, 2, 1, -1]
        res = Qi(test_list).sort(reverse=True).to_list()
        assert res == [4, 3, 2, 2, 1, -1]
        
    def enumerate(self):
        test_list = [1, 3, 2, 2, -1, 4]
        res = Qi(test_list).enumerate().to_list()
        assert res == [(0, 1), (1, 3), (2, 2), (3, 2), (4, -1), (5, 4)]
        test_list = list('hello')
        res = Qi(test_list).enumerate().to_list()
        assert res == [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
        
       
if __name__ == '__main__':
    unittest.main()