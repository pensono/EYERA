import os
from os.path import basename
import json
import http.client
import urllib
from glob import glob

def extract_file(filename):
    paragraphs = [paragraph for paragraph in open(filename + '.txt', 'r').readlines() if len(paragraph) > 0]

    documents = []
    for i in range(len(paragraphs)):
        documents.append({
            'language': 'en',
            'id': str(i),
            'text': paragraphs[i]})

    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': os.environ['API_KEY'],
    }

    params = urllib.urlencode({
    })

    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, json.dumps({"documents": documents}), headers)
    response = conn.getresponse()
    data = json.loads(response.read())

    sorted_documents = sorted(data['documents'], key=lambda d: int(d['id']))
    phrase_lines = [",".join(doc['keyPhrases']) for doc in sorted_documents]
    open(filename + ".keywords", 'w').write("\n".join(phrase_lines).encode('utf-8'))

for file in glob("data/*.txt"):
    print("Extracting " + file)
    extract_file(file.split('.')[0])