#Created    by Erik Rutyna -    March 8, 2020
#Last Edit  by Erik Rutyna -    March 8, 2020

import requests

# Setup required variables
API_KEY = "BD3A7B2B7D703839E084AD22D383CB02"
ENDPOINT = "http://api.steampowered.com/IEconDOTA2_570/GetGameItems/v1"

# Make request to server
response = requests.get(ENDPOINT,
                        params=dict(key=API_KEY, language="en"))

# Check results
print(response.json()['result'])