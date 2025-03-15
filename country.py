import requests

def get_country_details(url):
    response = requests.get(url)
    data = response.json()
    country_data = data[0]
    print(f"Name: {country_data['name']['common']}")
    print(country_data)

def main():
    country = input("Enter Country: ").lower()
    url = f"https://restcountries.com/v3.1/name/{country}"
    get_country_details(url)

if __name__ == "__main__":
    main()