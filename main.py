import requests
from bs4 import BeautifulSoup
from langdetect import detect

def get_website_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string
    else:
        return f"Failed to retrieve website: {response.status_code}"


def website_language():
    url = "https://www.google.com"
    response = requests.get(url)
    language =  detect(response.text)
    print("The website language is:", language)
    return language


def random():
    return 1+1



if __name__ == "__main__":
    title = get_website_title('https://www.google.com')
    print(title)
    website_language()


