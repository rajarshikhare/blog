from .models import Client
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
    c = Client(user_agent=request.META['HTTP_USER_AGENT'], ip_address=ip_addr, time=time.ctime())
    c.save()