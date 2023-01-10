import requests
from bs4 import BeautifulSoup

# Ask the user for a URL
url = input("Enter the URL of the webpage to scrape: ")

# Use the requests library to retrieve the HTML of the webpage
response = requests.get(url)
html = response.text

# Use the BeautifulSoup library to parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Ask the user what type of data they want to scrape
data_type = input("What type of data do you want to scrape? (e.g. email, custom) ")

# Extract the information from the webpage
if data_type == 'email':
    email_addresses = []
    for link in soup.find_all('a'):
        email = link.get('href')
        if email and 'mailto:' in email:
            email_addresses.append(email.replace('mailto:', ''))
    print(email_addresses)
    
elif data_type == 'custom':
    # Ask the user for a custom word to scrape
    custom_word = input("Enter the custom word you want to scrape: ")
    custom_word_count = len(soup(text=lambda text: custom_word in text))
    print(f'{custom_word_count} occurrences of the word "{custom_word}" were found on the webpage.')
else:
    print("Sorry, I can't scrape that type of data.")