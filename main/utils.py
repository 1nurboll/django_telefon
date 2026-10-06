import requests
from django.core.cache import cache

def get_usd_rate():
    """1 USD = ? KGS курсын кайтарат (1 саатка кэштелет)"""
    rate = cache.get('usd_rate')
    if rate:
        return rate

    try:
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=5)
        data = response.json()
        rate = data['rates']['KGS']
        cache.set('usd_rate', rate, 3600)  # 1 саат
        return rate
    except Exception:
        return 89.50  # интернет жок болсо камдык курс

  
  
  
  
