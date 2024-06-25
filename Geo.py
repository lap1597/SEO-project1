import requests
import pprint

def get_geolocation(api_key, ip_address):
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    api_key = "870a3e4f506c4354ac76f4bf6c2051b3" 

    while True:
        ip_address = input("Enter an IP address (or 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            break

        geolocation_data = get_geolocation(api_key, ip_address)
        if geolocation_data:
            pprint.pprint(geolocation_data)
        else:
            print("Failed to retrieve data. Please check the IP address and try again.")

if __name__ == "__main__":
    main()

