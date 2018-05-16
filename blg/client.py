from .models import Client

def store_req(request):
    c = Client(user_agent=request.META['HTTP_USER_AGENT'], ip_address=request.META['REMOTE_ADDR'])
    c.save()