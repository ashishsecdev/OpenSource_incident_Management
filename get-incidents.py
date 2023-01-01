import requests
import json

r = requests.get('http://127.0.0.1:8000/incidents')

if r.status_code == 200:
    incidents = r.json()
    print(json.dumps(incidents, indent=2)) #Don't think much explaination is required.
else:
    print('Error getting incidents')
