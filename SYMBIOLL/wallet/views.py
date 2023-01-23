from django.shortcuts import render
from .models import Wallet, Transaction
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm



def sign_in(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserForm()

    context={'form': form}
    
    template='wallet/sign_in.html'

    return render(request, template, context)










# Create your views here.
