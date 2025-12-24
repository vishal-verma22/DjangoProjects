from django.shortcuts import render
import requests

def get_Live_price(request):
    if request.method == 'POST':
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for i in data:
                print(i['id'])
                # print(i['name'])
                print(i['current_price'])
            msg = "success"
            return render(request, "home.html", {"message": data})
        else:
            msg = "API request failed"
            return render(request, "home.html", {"message": msg})
    else:
        return render(request, "home.html")
