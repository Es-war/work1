import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ans = '''Total: 7
Line1: <小孩> 小    孩
Line2: <小孩> xiao&^$#%$*)h
Line3: <小孩> 肖13573孩
Line3: <奶奶> nai_&^$%  女乃
Line5: <奶奶> 奶&*……7女乃
Line7: <操心> 扌喿&&&%……￥%心
Line8: <interesting> inT%%%&96ere  stIn1234G'''

        org = "./org1.txt"
        org_add = "./org_add1.txt"
        file_ans = "./ans.txt"

        main.init_map()
        checker = main.Check()
        checker.read_words(org)
        checker.read_org_add(org_add)
        self.assertEqual(checker.output(file_ans), ans)  # add assertion here


if __name__ == '__main__':
    unittest.main()
