import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        peshehod = Runner('Пешеход')
        # for i in range(9):   # проверка неуспешного теста (вывод ниже)
        for i in range(10):
            peshehod.walk()
        self.assertEqual(peshehod.distance, 50)

    def test_run(self):
        begun = Runner('Бегун')
        for i in range(10):
            begun.run()
        self.assertEqual(begun.distance, 100)

    def test_challenge(self):
        peshehod = Runner('Пешеход')
        begun = Runner('Бегун')
        for i in range(10):
            peshehod.walk()
            begun.run()
        self.assertNotEqual(peshehod.distance, begun.distance)


if __name__ == '__main__':
    unittest.main()


'''
..F
======================================================================
FAIL: test_walk (__main__.RunnerTest.test_walk)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests_12_1.py", line 10, in test_walk
    self.assertEqual(peshehod.distance, 50)
AssertionError: 45 != 50

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=1)
'''
