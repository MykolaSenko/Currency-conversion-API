import requests
import pandas as pd


def request():
    '''
    making an API request to get current currencies rates
    '''
    api_key = "6641341fcdf34fb7989f2e682ec6b5c0"
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    r = requests.get(url)
    return r

def preprocessing(r):
    '''
    Preprocessing data. Printing currencies rates in Pandas dataframe.
    @return er: Pandas dataframe.
    '''
    data = r.json()
    er = pd.DataFrame.from_dict({"rates": data["rates"]}, orient="index")
    return er

def calculation(currency, amount, currency_rec, er):
    """
    Performs the currency conversion.
    @param currency: The currency being converted from.
    @param amount: The amount being converted.
    @param currency_rec: The currency being converted to.
    @param er: The Pandas DataFrame containing the exchange rates.
    @return: The converted amount.
    """
    if currency == "USD":
        amount_rec = float(amount) * er.at['rates', currency_rec]
        return round(amount_rec, 2)
    elif currency_rec == 'USD':
        amount_rec = float(amount) / er.at['rates', currency]
        return round(amount_rec, 2)
    else:
        amount_in_usd = float(amount) / er.at['rates', currency]
        amount_rec = amount_in_usd * er.loc['rates', currency_rec]
        return round(amount_rec, 2)