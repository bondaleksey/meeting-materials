import requests

url = "https://www.mathnet.ru/"

response = requests.get('https://www.booking.com', timeout=5)

items = response.headers.items()

headers = [f'{key}: {header}' for key, header in items]

formatted_headers = '\n'.join(headers)

with open('headers.txt', 'w', encoding='utf-8') as file:
    file.write(formatted_headers)