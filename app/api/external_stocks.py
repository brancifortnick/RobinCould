from flask import Blueprint, redirect
import requests


external_stocks = Blueprint('external_stocks', __name__)


# /api/stocks/:ticker
@external_stocks.route('/<ticker>')
def get_single_stock(ticker):
    httpResponse = requests.get(
        "https: // api.polygon.io/v2/aggs/ticker/" + ticker)
    pythonData = httpResponse.json()
    print(f' ticker + {ticker}')
    return pythonData


# returned object
# {
#     "adjusted": true,
#     "next_url": "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/1578114000000/2020-01-10?cursor=bGltaXQ9MiZzb3J0PWFzYw",
#     "queryCount": 2,
#     "request_id": "6a7e466379af0a71039d60cc78e72282",
#     "results": [
#         {
#             "c": 75.0875,
#             "h": 75.15,
#             "l": 73.7975,
#             "n": 1,
#             "o": 74.06,
#             "t": 1577941200000,
#             "v": 135647456,
#             "vw": 74.6099
#         },
#         {
#             "c": 74.3575,
#             "h": 75.145,
#             "l": 74.125,
#             "n": 1,
#             "o": 74.2875,
#             "t": 1578027600000,
#             "v": 146535512,
#             "vw": 74.7026
#         }
#     ],
#     "resultsCount": 2,
#     "status": "OK",
#     "ticker": "AAPL"
# }
