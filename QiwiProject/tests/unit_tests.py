import unittest

from main import currency_rates


class CurrencyRatesTest(unittest.TestCase):
    """
    Класс тестирования командной утилиты currency_rates.

    """

    # TODO автор не успел...
    def test_example(self):
        res = str(currency_rates())
        self.assertEqual(res, 'USD (Доллар США): 61,2475')
