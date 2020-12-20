import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base, quote,  amount):
        quote=str(quote)
        base=str(base)
        amount=str(amount)


        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        try:
            r = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_ticker}')
        except KeyError:
            raise ConvertionException(f'Фигня')
        get_=json.loads(r.content)['rates']
        total_base = get_[quote_ticker]

        return total_base