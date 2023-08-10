from fastapi import FastAPI
from utils.script import request, preprocessing, calculation

app = FastAPI()

@app.get("/")
def home():
    """
    Home endpoint to display a welcome message.
    """
    return {"message": "Welcome to the Currency Conversion API!"}

@app.get("/exchange_rates")
def get_exchange_rates():
    """
    Endpoint to get the exchange rates.
    """
    response = request()
    exchange_rates = preprocessing(response)
    return exchange_rates

@app.get("/convert")
def convert_currency(currency_give: str, amount_give: float, currency_receive: str):
    """
    Endpoint to convert currency.
    """
    response = request()
    exchange_rates = preprocessing(response)
    amount_receive = calculation(currency_give, amount_give, currency_receive, exchange_rates)
    result = {
        "currency_give": currency_give,
        "amount_give": amount_give,
        "currency_receive": currency_receive,
        "amount_receive": amount_receive
    }
    return result
