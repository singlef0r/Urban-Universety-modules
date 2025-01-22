import runner
import unittest
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        oRuner = runner.Runner('one')
        for _ in range(10):
            oRuner.walk()
        self.assertEqual(oRuner.distance, 50)

    def test_run(self):
        oRuner = runner.Runner('two')
        for _ in range(10):
            oRuner.run()
        self.assertEqual(oRuner.distance, 100)

    def test_challenge(self):
        oRuner1, oRuner2 = runner.Runner('free'), runner.Runner('four')
        for _ in range(10):
            oRuner1.run()
            oRuner2.walk()
        self.assertNotEqual(oRuner1.distance, oRuner2.distance)


if __name__ == '__main__':
    unittest.main()