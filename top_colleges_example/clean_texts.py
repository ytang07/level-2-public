import requests
import json

from text_api_config import apikey

headers = {
    "Content-Type": "application/json",
    "apikey": apikey
}
text_url = "https://app.thetextapi.com/text/"
sim_sentences_url = text_url + "similarity_by_sentences"

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

# remove the most common sentences and see what they are
with open(caltech, "r") as f:
    text_caltech = f.read()
with open(columbia, "r") as f:
    text_columbia = f.read()
body = {
    "texts": [text_caltech, text_columbia]
}
response = requests.post(sim_sentences_url, headers=headers, json=body)
_dict = json.loads(response.text)
repeats = _dict["repeat sentences"]
repeats.remove(' ')
new_caltech = _dict["doc1 cleaned"]
new_columbia = _dict["doc2 cleaned"]
with open(caltech, "w") as f:
    f.write(new_caltech)
with open(columbia, "w") as f:
    f.write(new_columbia)

# remove all repeat sentences from other docs
# save each one as a cleaned text file
for university in university_files[2:]:
    with open(university, "r") as f:
        text = f.read()
    for sent in repeats:
        text = text.replace(sent, "")
    texts = text.split("Campus safety data were")
    with open(university, "w") as f:
        f.write(texts[0])