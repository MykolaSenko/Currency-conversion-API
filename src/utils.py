import requests
import pandas as pd


def request():
    '''
    making an API request to get current currencies rates
    '''
    try:
        with open('api_key.txt', 'r') as f:
            api_key = f.readline().strip()
    except Exception as f:
        raise Exception(f"Error reading token from file: {f}")
    print(api_key)
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    return requests.get(url)

def preprocessing(r):
    '''
    Preprocessing data. Printing currencies rates in Pandas dataframe.
    @return er: Pandas dataframe.
    '''
    data = r.json()
    return pd.DataFrame.from_dict({"rates": data["rates"]}, orient="index")

def calculation(currency, amount, currency_rec, er):
    """
    Performs the currency conversion.
    @param currency: The currency being converted from.
    @param amount: The amount being converted.
    @param currency_rec: The currency being converted to.
    @param er: The Pandas DataFrame containing the exchange rates.
    @return: The converted amount.
    """
    amount_in_usd = float(amount) / er.at['rates', currency.upper()]
    amount_rec = amount_in_usd * er.loc['rates', currency_rec.upper()]
    return round(amount_rec, 2)