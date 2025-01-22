import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Runner_Ysain = Runner('Усэйн', 10)
        self.Runner_Andrey = Runner('Андрей', 9)
        self.Runner_Nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    def test_run1(self):
        oTournament = Tournament(90, self.Runner_Ysain, self.Runner_Nik)
        self.all_results['1'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())

    def test_run2(self):
        oTournament = Tournament(90, self.Runner_Andrey, self.Runner_Nik)
        self.all_results['2'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())

    def test_run3(self):
        oTournament = Tournament(90, self.Runner_Ysain, self.Runner_Andrey, self.Runner_Nik)
        self.all_results['3'] = {num: runner.__str__() for num, runner in oTournament.start().items()}
        self.assertTrue(self.all_results[max(self.all_results.keys())], self.Runner_Nik.__str__())


if __name__ == '__main__':
    unittest.main()
