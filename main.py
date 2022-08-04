from pprint import pprint
import requests
r = requests.get('https://raw.githubusercontent.com/LizardByte/uno/gh-pages/github/repos.json')
data = r.json()
pprint(data)
