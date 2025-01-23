import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        oRuner = runner.Runner('one')
        for _ in range(10):
            oRuner.walk()
        self.assertEqual(oRuner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        oRuner = runner.Runner('two')
        for _ in range(10):
            oRuner.run()
        self.assertEqual(oRuner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        oRuner1, oRuner2 = runner.Runner('free'), runner.Runner('four')
        for _ in range(10):
            oRuner1.run()
            oRuner2.walk()
        self.assertNotEqual(oRuner1.distance, oRuner2.distance)

import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def setUp(self):
        self.Runner_Ysain = Runner('Усэйн', 10)
        self.Runner_Andrey = Runner('Андрей', 9)
        self.Runner_Nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run1(self):
        oTournament = Tournament(90, self.Runner_Ysain, self.Runner_Nik)
        self.all_results['1'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run2(self):
        oTournament = Tournament(90, self.Runner_Andrey, self.Runner_Nik)
        self.all_results['2'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run3(self):
        oTournament = Tournament(90, self.Runner_Ysain, self.Runner_Andrey, self.Runner_Nik)
        self.all_results['3'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())



if __name__ == '__main__':
    unittest.main()
