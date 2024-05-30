import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = "MYNYCRRT8QLXDCMX"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "64f688eea0c04abbbb1a10912af786c1"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "AC5b1e45410410d7e8bc19252f49448339"
auth_token = "1988ae4936580b2ad36f7e9399fe4b02"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_API_ENDPOINT, params=parameters)
today_date = date.today()
yesterday_date = today_date - timedelta(days=1)
day_before_yesterday_date = today_date - timedelta(days=2)
yesterday_closing_stock = float(response.json()["Time Series (Daily)"][str(yesterday_date)]["4. close"])
day_before_yesterday_closing_stock = float(
    response.json()["Time Series (Daily)"][str(day_before_yesterday_date)]["4. close"])
stock_percentage_difference = abs(
    yesterday_closing_stock - day_before_yesterday_closing_stock) * 100 / day_before_yesterday_closing_stock

if stock_percentage_difference > 0.1:

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "from": str(yesterday_date),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(NEWS_API_ENDPOINT, params=news_parameters)
    news_articles = news_response.json()["articles"][:3]

    for article in news_articles:
        # STEP 3: Use https://www.twilio.com Send a seperate message with the percentage change and each article's
        # title and description to your phone number.
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: 🔺{round(stock_percentage_difference, 1)}%\n"
                 f"Headline: {article["title"]}\n"
                 f"Brief: {article["description"]}",
            from_="+13653639452",
            to="+15194444770"
        )

# Optional: Format the SMS message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey have 
gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash. 
or "TSLA: 🔻5% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F 
filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
