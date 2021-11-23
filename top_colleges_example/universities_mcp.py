import requests
import json

from text_api_config import apikey

headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
text_url = "https://app.thetextapi.com/text/"
mps_url = text_url + "most_positive_sentences"
mns_url = text_url + "most_negative_sentences"
mcps_url = text_url + "most_common_phrases"
summarize_url = text_url + "summarize"
sim_sentences_url = text_url + "similarity_by_sentences"

mps_filename = "mps_universities.json"
mns_filename = "mns_universities.json"
mcps_filename = "mcps_universities.json"
summaries_filename = "university_summaries.json"

caltech = "california-institute-of-technology-1131.txt"
columbia = "columbia-university-2707.txt"
duke = "duke-university-2920.txt"
harvard = "harvard-university-2155.txt"
mit = "massachusetts-institute-of-technology-2178.txt"
princeton = "princeton-university-2627.txt"
stanford = "stanford-university-1305.txt"
uchicago = "university-of-chicago-1774.txt"
penn = "university-of-pennsylvania-3378.txt"
yale = "yale-university-1426.txt"

university_files = [caltech, columbia, duke, harvard, mit, princeton, stanford, uchicago, penn, yale]

mps = {}
mns = {}
mcps = {}
summaries = {}
for university in university_files:
    with open(university, "r") as f:
        text = f.read()
    text = text.replace("\n", "")
    text = text.replace("#", "")
    text = text.replace("Students", "")
    text = text.replace("student satisfaction", "")
    body = {
        "text": text
    }
    # response = requests.post(url=mps_url, headers=headers, json=body)
    # _dict = json.loads(response.text)
    # mps[university] = _dict["most positive sentences"]
    
    # response = requests.post(url=mns_url, headers=headers, json=body)
    # _dict = json.loads(response.text)
    # mns[university] = _dict["most negative sentences"]
    
    response = requests.post(url=mcps_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    mcps[university] = _dict["most common phrases"]
    
    response = requests.post(url=summarize_url, headers=headers, json=body)
    _dict = json.loads(response.text)
    summaries[university] = _dict["summary"]

# with open(mps_filename, "w") as f:
#     json.dump(mps, f)

# with open(mns_filename, "w") as f:
#     json.dump(mns, f)

with open(mcps_filename, "w") as f:
    json.dump(mcps, f)

with open(summaries_filename, "w") as f:
    json.dump(summaries, f)