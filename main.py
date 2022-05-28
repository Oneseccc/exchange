import requests

url = 'https://api.exchangerate.host/convert'
currency = input("What currency do you want to exchange from USD : ")

amount = input("How much you want to exchange : ")
payload = {"from": "USD", "to": currency, "amount": amount, "result": ()}
response = requests.get(url, params=payload)
data = response.json()

print("\033[1;32;2m Total : ", data["result"], '\033[0m', '\n ===========================================================')

ask = input(' do you want to check for stock market ? (type ; (yes/no) : ')

if ask == 'yes':
    stock = input("What stock do you want to check :  ")

    url = "https://https.p.rapidapi.com/" + str(stock)
    key = {
        "X-RapidAPI-Host": "realstonks.p.rapidapi.com",
        "X-RapidAPI-Key": "182cbfaecamsha44fa92a6038f55p1c9a53jsne7e1583a13ab"
    }

    response = requests.get(url, headers=key)
    data = response.json()

    print("\033[1;32;2m Price :", data["price"])
    print("Total Volume :", data["total_vol"], '\033[0m ', '\n ===========================================================')

else:
    quit()