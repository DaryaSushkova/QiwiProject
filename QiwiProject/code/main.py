import click

from parser import parser_currency


@click.command()
@click.option('--code', default='USD', help='Код валюты в формате ISO 4217.')
@click.option('--date', default='2022-10-08', help='Дата в формате YYYY-MM-DD.')
def currency_rates(code: str, date: str):
    """
    Инструмент командной строки, используемый для получения курса валют.

    :param code: Код валюты.
    :param date: Дата курса.
    :return: Искомый курс.
    """

    click.echo(parser_currency(code, date))


# Базовый запуск через обычную консоль.
if __name__ == '__main__':
    currency_rates()
