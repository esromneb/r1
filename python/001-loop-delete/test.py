import unittest
import random
from util import *

class working(unittest.TestCase):
    def testaReturn(self):
        ret = Util.delete_squares([5])
        self.assertEqual(ret, None, "delete_squares() should not return anything")


    def testRandom(self):
        for _ in range(100):
            out = [x*x for x in [random.randint(0,9000) for r in xrange(99)]]
            Util.delete_squares(out)
            self.assertEqual(len(out), 0)

    def testSimple(self):
        ll = [3,7,4,9,3]
        ipt = list(ll)
        out = list(ll)
        Util.delete_squares(out)
        self.assertEqual([3,7,3], out)

if __name__ == '__main__':
    unittest.main()



