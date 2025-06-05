'''
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

# Replace these with your actual credentials from IBM Cloud NLU instance
api_key = 'txpRjG3jOEefggK9Ruh7UX7j9ery_nqNnpQmKy38ZJTt'
service_url = 'https://eu-de.ml.cloud.ibm.com'

# Create the NLU client
nlu = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    iam_apikey=api_key,
    url=service_url
)

# Test text
test_text = "IBM Watson is a powerful AI platform for natural language understanding."

try:
    response = nlu.analyze(
        text=test_text,
        features=Features(keywords=KeywordsOptions(limit=3))
    ).get_result()
    print("Connection successful! Sample keywords extracted:")
    for kw in response['keywords']:
        print("-", kw['text'])
except Exception as e:
    print("Connection failed:", e)
    '''
import google.generativeai as genai

# Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyCcUy-lP6FQ4bgKUwNHQx-zMLrfYSs6-4M"

genai.configure(api_key=GEMINI_API_KEY)

try:
    # Attempt a simple API call to check if the key is working
    model = genai.GenerativeModel('generate_content')
    response = model.generate_content("Say hello.")
    print("Gemini API key is likely working.")
    print("Response:", response.text)

except Exception as e:
    print(f"Error with Gemini API key: {e}")
    print("Please ensure your API key is correct and active.")