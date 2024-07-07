import requests # type: ignore

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code)
    print(response.text)
    print(type(response.text))
    categories = response.json()
    for category in categories:
        print(category['name'])