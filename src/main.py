import numpy as np
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
from flask import Flask, url_for, jsonify, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

base_url_1 = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
base_url_2 = '&interval=1min&apikey=CF77SW8EH662BQKK'


class InputForm(Form):
    ticker = StringField('ticker', validators=[InputRequired()])
    tickercount = IntegerField('tickercount', validators=[InputRequired()])
    submit = SubmitField('Submit')


def get_potato_price():
    data = requests.get('https://www.expatistan.com/price/potatoes/los-angeles')
    soup = BeautifulSoup(data.text, 'html.parser')
    match = soup.find('span', class_='city-1').contents[0]
    return match


def get_ticker_price(ticker):
    url = base_url_1 + ticker + base_url_2
    req = requests.request('GET', url)
    if req.status_code == 200:
        print("Get request successful")
        data = req.json()['Time Series (1min)']
        data = next(iter(data.values()))
        price = data['4. close']
        return price
    else:
        print("Get request unsuccessful")


@app.route('/')
def index():
    form = InputForm()
    if form.validate_on_submit():
        return redirect(url_for('redirect'))
    return render_template('index.html', form=form)


@app.route('/redirect', methods=['POST'])
def redirect():
    form = InputForm()
    ticker = str(request.form['ticker'].upper())
    tickercount = request.form['tickercount']

    price = float(get_ticker_price(ticker)) * float(tickercount)
    potatoprice = get_potato_price()
    potatopricefloat = float(potatoprice.replace("$", ""))
    tradingurl = "https://www.tradingview.com/symbols/NASDAQ-" + ticker
    ratio = price / potatopricefloat
    price = int(price)
    ratio = int(ratio)
    bigpotato = int(ratio) * ("🥔")
    return render_template('redirect.html', bigpotato=bigpotato, ratio=ratio, potatoprice=potatoprice, price=price, ticker=ticker, tickercount=tickercount, form=form)


if __name__ == "__main__":
    app.run(port=8063, debug=True)
