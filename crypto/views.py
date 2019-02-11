from django.shortcuts import render


# Create your views here.

def home(request):
    import requests  # pip install requests
    import json
    # Price api
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')
    price = json.loads(price_request.content)

    # News api
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render (request, 'home.html', {'api':api, 'price':price})

# def home(request):
#     import requests  # pip install requests
#     import json
#     api_request = requests.get('http://nutrimaker.quintuslabs.in/api/slider_images/')
#     api = json.loads(api_request.content)
#     return render (request, 'home.html', {'api':api})

def prices(request):
    if request.method == 'POST':
        import requests  # pip install requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote +'&tsyms=USD')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})
    else:
        not_found = 'Enter a crypto currency symbol into the form above.....'
        return render(request, 'prices.html',{'not_found': not_found})