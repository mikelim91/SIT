# import requests
# import json

# # Set your API key and the URL endpoint
# api_key = 'ttHIQh3TnkhMa0SEOSN4wXRuUi3HowNRGnqTSAwqHpB1tKfyzH'  # Replace this with your actual API key
# url = 'https://api.petfinder.com/v2/animals'

# # Set up the headers with your API key
# headers = {
#     'Authorization': f'Bearer {api_key}'
# }

# # Set any parameters for the request
# params = {
#     'type': 'dog',
#     'page': 2
# }

# # Make the GET request
# response = requests.get(url, headers=headers, params=params)

# # Check if the request was successful
# if response.status_code == 200:
#     # Get the response data as JSON
#     data = response.json()
#     # Now you can print it out, examine it, or save it
#     print(json.dumps(data, indent=4))
# else:
#     print('Failed to retrieve data:', response.status_code)
    
    
import petpy    
import requests

# The URL for the Petfinder API endpoint
url = 'https://api.petfinder.com/v2/animals'

# Your Petfinder API key
api_key = 'ttHIQh3TnkhMa0SEOSN4wXRuUi3HowNRGnqTSAwqHpB1tKfyzH'

# Set up the headers with your API key
headers = {
    'Authorization': 'Bearer {}'.format(api_key)
}

# Parameters for the GET request
params = {
    'type': 'dog',
    'page': 2
}

# Send the GET request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the response data
    data = response.json()
    # Do something with the data, like printing it
    print(data)
else:
    print('Failed to retrieve data:', response.status_code)

pf = petpy.Petfinder(key='ttHIQh3TnkhMa0SEOSN4wXRuUi3HowNRGnqTSAwqHpB1tKfyzH',secret='jbC7olhI4fzgc8K3PADGDytKCYF4Svs0ULXVqCsj')
