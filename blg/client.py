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
    url = 'http://ip-api.com/json/'
    url = url + str(ip)
    response = requests.get(url)
    data = json.loads(response.content)
    if data['status'] == 'success':
        return [data['city'], data['country'], data['isp']]
    else:
        return ['Nan', 'Nan', 'Nan']
        