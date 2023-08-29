from fastapi import FastAPI, HTTPException
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
    The line `response = request()` is calling the `request()` function from the `utils.script`
    module. This function is responsible for making a request to an external API to retrieve the
    exchange rates. The response from the API is stored in the `response` variable.
    """
    response = request()
    return response.json()


@app.get("/convert")
def convert_currency(currency_give: str, amount_give: float, currency_receive: str):
    """
    Endpoint to convert currency.
    """
    response = request()
    exchange_rates = preprocessing(response)
    if (currency_give.upper() not in exchange_rates.columns) or (currency_receive.upper() not in exchange_rates.columns):
        raise HTTPException(status_code=404, detail="Not correct currency code. Please, check out the supported currencies at the previous endpoint.")
    amount_receive = calculation(currency_give, amount_give, currency_receive, exchange_rates)
    return {
        "currency_give": currency_give.upper(),
        "amount_give": abs(amount_give),
        "currency_receive": currency_receive.upper(),
        "amount_receive": abs(amount_receive),
    }


