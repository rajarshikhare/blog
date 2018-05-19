from .models import Client
import requests
import json
import time
from mailjet_rest import Client as clt


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
    send_mail(city, country, isp)
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


def send_mail(city, country, isp):

    html_part = '<h3>' + 'CITY : ' + city + '<br>COUNTRY: ' + country + '<br>ISP: ' + isp + '</h3>' 
    api_key = '1b0caf4efe008cfec2c383f9c416ba34'
    api_secret = 'cab5f6da8cf628ac848edf7f60f3d70d'
    mailjet = clt(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": "rajarshi.vaibhav@gmail.com",
                    "Name": "Rajarshi"
                },
                "To": [
                    {
                        "Email": "rajarshi.vaibhav@gmail.com",
                        "Name": "Rajarshi khare"
                    }
                ],
                "Subject": "Somebody Just looged in!!",
                "TextPart": "Somebody Just logged in!!",
                "HTMLPart": html_part
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
        