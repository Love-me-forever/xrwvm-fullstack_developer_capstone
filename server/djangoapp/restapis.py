import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Network exception occurred: {}".format(e))


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print("Unexpected error: {}".format(e))
        print("Network exception occurred")


def sentiment_analyzer(text):
    sentiment_analyzer_url = "https://sentianalyzer.1o1dc12ocmut.us-south.codeengine.appdomain.cloud/"
    request_url = sentiment_analyzer_url + "analyze/" + text
    payload = "Your text to analyze here"

    response = requests.get(request_url)
    if response.status_code == 200:
        result = response.json() 
        print("Sentiment analysis result: {}".format(result))
        sentiment = result.get("sentiment", "No sentiment found")
        print("Sentiment analysis result: {}".format(sentiment))
    else:
        print("Error: {}".format(response.status_code))


def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except Exception as e:
        print("Network exception occurred: {}".format(e))

