import requests
from fastapi import FastAPI

app = FastAPI()

@app.get('/advice')
def daily_advice():
    slip = requests.get('https://api.adviceslip.com/advice')
    daily_slip = slip.json()
    advice = daily_slip['slip']['advice']
    return {'daily advice': advice}

