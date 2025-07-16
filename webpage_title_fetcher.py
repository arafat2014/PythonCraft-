import requests
from bs4 import BeautifulSoup

def get_webpage_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title.string)

# Example
# get_webpage_title('https://www.python.org')
