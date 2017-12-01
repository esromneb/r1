import unittest
from singlepoleiir import *
import numpy as np

class working(unittest.TestCase):
    def testMembers(self):
        for i in range(1,10):
            dut = SinglePoleIIR(i)
            dut.update(i)
            self.assertEqual(dut.get(), i, "first value input not right")
        dut = SinglePoleIIR(7)
        dut.update(2)
        self.assertEqual(dut.get(),2)
        dut = SinglePoleIIR(10)
        self.assertEqual(dut.update_get(2),2)
        self.assertAlmostEqual(dut.update_get(4),2.2)
        self.assertAlmostEqual(dut.update_get(0),1.98)

    def testUpdate(self):
        dut = SinglePoleIIR(100)
        bump = 0
        actual = []
        expected = [0.0,0.207708,0.320143864692,0.537742854658,0.93291425644,1.59609431676,2.52433090461]
        for i in range(100):
            dut.update((99-i)%9)
            if i % (3+bump) == 0:
                bump += i
                actual.append(dut.get())
        self.assertTrue(np.allclose(expected,actual))

if __name__ == '__main__':
    unittest.main()



