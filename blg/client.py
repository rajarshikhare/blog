from .models import Client
import requests
import json
import time


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def store_req(request):
    ip_addr = get_client_ip(request)
    city, country, isp = get_location(ip_addr)
    c = Client(user_agent=request.META['HTTP_USER_AGENT'], ip_address=ip_addr, time=time.ctime(), city=city, country=country, isp=isp)
    c.save()

def get_location(ip):
    url = 'https://api.ipdata.co/'
    url = url + str(ip)
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        return [data['city'], data['country_name'], data['organisation']]
    else:
        return ['Nan', 'Nan', 'Nan']
        