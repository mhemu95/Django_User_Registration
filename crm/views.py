from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:sigin')
def home(request):

    return render(request, 'crm/crm_home.html')