import os
import json
import http.client
import re

def keywords_from_string(text):
    document = {
        'language': 'en',
        'id': 'id',
        'text': text}

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': os.environ['TEXT_ANALYSIS_API_KEY'],
    }

    numbers = re.findall(r'\d[\d,.]+', text)

    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?", json.dumps({"documents": [document]}), headers)
    response = conn.getresponse()
    data = json.loads(response.read())

    #  This join/split combo proves that I am truely the spawn of satan #hackathon
    keywords = " ".join(data['documents'][0]['keyPhrases'] + numbers).split(" ")
    return keywords


def keywords_from_article(article_text):
    paragraphs = [paragraph for paragraph in article_text.splitlines() if len(paragraph) > 0]

    documents = []
    for i in range(len(paragraphs)):
        documents.append({
            'language': 'en',
            'id': str(i),
            'text': paragraphs[i]})

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': os.environ['TEXT_ANALYSIS_API_KEY'],
    }

    paragraph_numbers = [re.findall(r'\d[\d,.]+', paragraph) for paragraph in paragraphs]

    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases", json.dumps({"documents": documents}), headers)
    response = conn.getresponse()
    data = json.loads(response.read())

    sorted_documents = sorted(data['documents'], key=lambda d: int(d['id']))
    #  This join/split combo proves that I am truely the spawn of satan #hackathon
    phrase_lines = [" ".join(z[0]['keyPhrases'] + z[1]).split(" ") for z in zip(sorted_documents, paragraph_numbers)]
    return phrase_lines
