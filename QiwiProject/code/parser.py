import pandas as pd

from datetime import datetime


def parser_currency(code: str, date: str):
    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return 'Введенная дата некорректна, используйте формат YYYY-MM-DD и убедитесь, что дата валидна.'
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_object.strftime("%d/%m/%Y")}'
    try:
        df = pd.read_xml(url, encoding='cp1251')
    except ValueError:
        return 'Для указанной даты отсутствуют данные по курсу.'
    try:
        value = df.loc[df['CharCode'] == code]['Value'].item()  # Искомый курс.
        name = df.loc[df['CharCode'] == code]['Name'].item()  # Наименование валюты.
    except ValueError:
        valid_list = ' '.join(df.CharCode.unique())
        return f'Код валюты некорректен. Возможны следующие значения:\n{valid_list}'
    return f'{code} ({name}): {value}'
