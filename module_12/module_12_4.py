import logging
import unittest
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        try:
            oRuner = rt_with_exceptions.Runner('one', -7)
            for _ in range(10):
                oRuner.walk()
            self.assertEqual(oRuner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        try:
            oRuner = rt_with_exceptions.Runner(['Farr'])
            for _ in range(10):
                oRuner.run()
            self.assertEqual(oRuner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        oRuner1, oRuner2 = rt_with_exceptions.Runner('free'), rt_with_exceptions.Runner('four')
        for _ in range(10):
            oRuner1.run()
            oRuner2.walk()
        self.assertNotEqual(oRuner1.distance, oRuner2.distance)


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w',
                    format="%(asctime)s | %(levelname)s | %(message)s", encoding='utf-8')
