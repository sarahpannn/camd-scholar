import googleapiclient
from googleapiclient.discovery import build
from SECRETS import API_KEY, CSE_ID
import json

# Set your API key
API_KEY = API_KEY

# Create a custom search engine (CSE) ID
CSE_ID = CSE_ID

# Create a service object for interacting with the API
service = build('customsearch', 'v1', developerKey=API_KEY)


def get_search_results(keyword, num_results, file_name):
    # Make the API request
    response = service.cse().list(
        q=keyword,
        cx=CSE_ID,
        num=num_results
    ).execute()

    # Extract the search results
    items = response['items']
    
    with open(file_name, 'w') as f:
        json.dump(items, f)
    
    for item in items:
        print(item.keys())



def main():
    keyword = 'ai alignment'
    num_results = 10  # Specify the number of results you want to retrieve

    get_search_results(keyword, num_results, 'prelim_results.json')
    
if __name__ == '__main__':
    main()
