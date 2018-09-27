from bs4 import BeautifulSoup
import requests
from html import unescape
import json
import statistics
import re
from extruct.jsonld import JsonLdExtractor

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"}

resp = requests.get('https://www.balkaneu.com/opinionpeaceful-border-correction-between-kosovo-and-serbia/', headers = headers).content
text = BeautifulSoup(resp).text
date = re.search('[a-zA-Z\.]* \d?\d, \d{4}|\d{4}[-\.]\d\d[-\.]\d\d|\d\d?[-\.]\d\d?[-\.]\d{4}|[a-zA-Z]* \d\d?, [a-zA-Z]* \d{4}|\d\d? [a-zA-Z]* \d{4}', text)
print(date.group(0))
