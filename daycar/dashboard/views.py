from django.shortcuts import render
from home.models import Encar,Kcar
# from models import Encar,Kcar
# Create your views here.
def main(request):
    info = Encar.objects.filter(id=1)
    return render(request, "index_dash.html", {'info':info})